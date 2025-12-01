import inspect
import os
from pathlib import Path

import requests
import yaml
from colorama import Fore
from dotenv import load_dotenv

from modules.helpers import get_root
from modules.timer import Timer

load_dotenv()

timer = Timer()


def test(year, day, func, parse_func=None):
    part_name = func.__name__
    tests = get_test_data(year, day, part_name)

    for test in tests:
        args = test.get("args", [])
        kwargs = test.get("kwargs", {})
        timer.start_timer()
        if parse_func is None:
            parsed = test["data"]
        else:
            parsed = parse_func(test["data"], *args, **kwargs)

        answer = func(parsed, *args, **kwargs)
        if isinstance(answer, tuple):
            test_answer = answer[-1]
        else:
            test_answer = answer
        assert test_answer == test["answer"], print(
            Fore.RED + f"Expected {answer}, got {test["answer"]}" + Fore.RESET
        )

        print_title(year, day, part_name.replace("part_", "Test ").title(), Fore.GREEN)
        print_data(answer)


def solve(func, parse_func=None, *args, **kwargs):
    year, day = get_year_and_day()
    data = get_data(year, day)

    test(year, day, func, parse_func)

    timer.start_timer()
    if parse_func is None:
        parsed = data
    else:
        parsed = parse_func(data, *args, **kwargs)
    answer = func(parsed, *args, **kwargs)

    print_title(year, day, func.__name__.replace("part_", "Part ").title())
    print_data(answer)


def print_title(year, day, title, color=Fore.CYAN):
    print(color + f"{year} • {day} • {title}: " + Fore.RESET)


def print_data(data):
    if isinstance(data, tuple):
        for i, p in enumerate(data):
            if i == len(data) - 1:
                print(f"{p}" + Fore.WHITE + f" - {timer.end_timer()}\n" + Fore.RESET)
            else:
                print(p)
    else:
        print(f"{data}" + Fore.WHITE + f" - {timer.end_timer()}\n" + Fore.RESET)


def get_data(year, day) -> str | None:
    input_file = get_root() / "input" / str(year) / f"{day}.txt"
    if not input_file.exists():
        print(f"Inputbestand {input_file} bestaat niet. Downloaden...")

        url = f"https://adventofcode.com/{year}/day/{int(day)}/input"

        headers = {"Cookie": f"session={os.getenv('SESSION')}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            input_file.parent.mkdir(parents=True, exist_ok=True)

            with open(input_file, "w") as f:
                f.write(response.text.strip())
        else:
            raise Exception(
                f"Fout bij het downloaden van inputbestand: {response.status_code}"
            )

    with open(input_file, "r") as f:
        return f.read()


def get_test_data(year, day, part):
    file = get_root() / "input" / str(year) / f"{day}.yaml"

    if not file.exists():
        return []

    with open(file, "r") as f:
        data = yaml.safe_load(f)

        if part not in data:
            return []

        return data[part]


def get_year_and_day():
    caller_frame = inspect.stack()[2]
    caller_file = caller_frame.filename
    caller_path = Path(caller_file).resolve()

    year = caller_path.parent.name
    day = caller_path.stem

    return year, day
