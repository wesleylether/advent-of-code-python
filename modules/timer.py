import time

from colorama import Fore


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
            return f"{int(round(duration / 1_000, ndigits=0))}µs"
        elif duration > 1_000_000_000:
            return f"{round(duration / 1_000_000_000.0, 2)}s"
        else:
            return f"{round(duration / 1_000_000.0, 2)}ms"
