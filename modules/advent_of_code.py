import inspect
import os
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()


def answer_part_one(answer):
    print(f"Part 1:\n{answer}\n")


def answer_part_two(answer):
    print(f"Part 2:\n{answer}\n")


def get_input():
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    caller_path = Path(caller_file).resolve()

    year = caller_path.parent.name
    day_file = caller_path.stem

    input_file = Path(f"../input/{year}/{day_file}.txt")

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


class Timer:
    def __init__(self):
        self.start_time = None

    def start_timer(self):
        self.start_time = time.time_ns()

    def end_timer(self):
        if self.start_time is None:
            return print("Timer is niet gestart")

        end_time = time.time_ns()
        duration = end_time - self.start_time

        if duration < 1_000_000:
            print(f"Time: {round(duration / 1_000, 3)}µs")
        elif duration > 1_000_000_000:
            print(f"Time: {round(duration / 1_000_000_000.0, 3)}s")
        else:
            print(f"Time: {round(duration / 1_000_000.0, 3)}ms")
