import inspect
import os
from pathlib import Path

import requests
from colorama import Fore
from dotenv import load_dotenv

from modules.timer import Timer

load_dotenv()

timer = Timer()


def solve_one(func, *args, **kwargs):
    timer.start_timer()
    print(Fore.WHITE + f"Part 1: " + Fore.GREEN + f"{func(*args, **kwargs)}" + Fore.RESET)
    timer.end_timer()


def solve_two(func, *args, **kwargs):
    timer.start_timer()
    print(Fore.WHITE + f"Part 2: " + Fore.GREEN + f"{func(*args, **kwargs)}" + Fore.RESET)
    timer.end_timer()


def get_input(example=False):
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    caller_path = Path(caller_file).resolve()

    year = caller_path.parent.name
    day_file = caller_path.stem

    input_file = Path(f"../input/{year}/{day_file}{"-example" if example else ""}.txt")

    if not input_file.exists():
        print(f"Inputbestand {input_file} bestaat niet. Downloaden...")

        url = f"https://adventofcode.com/{year}/day/{int(day_file)}/input"

        headers = {"Cookie": f"session={os.getenv('SESSION')}"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            input_file.parent.mkdir(parents=True, exist_ok=True)

            with open(input_file, "w") as f:
                f.write(response.text.strip())
        else:
            raise Exception(f"Fout bij het downloaden van inputbestand: {response.status_code}")

    with open(input_file, "r") as f:
        return f.read()
