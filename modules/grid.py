from enum import Flag, auto

from modules.enums import Orientation


class GridOrientation(Flag):
    Horizontal = auto()
    Vertical = auto()
    Diagonal = auto()

    Up = auto()
    Down = auto()
    Left = auto()
    Right = auto()
    UpLeft = auto()
    UpRight = auto()
    DownLeft = auto()
    DownRight = auto()


class Grid:
    def __init__(self, width, height, default=None, overlap=False):
        self.width = width
        self.height = height
        self.default = default
        self.overlap = overlap
        self.grid = [[default for _ in range(width)] for _ in range(height)]
        self.current = (0, 0)

    @classmethod
    def from_string(cls, string):
        lines = string.splitlines()
        height = len(lines)
        width = max(len(line) for line in lines)
        grid = cls(width, height)
        grid.init_with_string(string)
        return grid

    def init_with_string(self, string):
        for y, row in enumerate(string.splitlines()):
            for x, cell in enumerate(row):
                self.grid[y][x] = cell

    def __str__(self):
        return "\n".join("".join(str(cell) for cell in row) for row in self.grid)

    def __getitem__(self, key):
        x, y = key

        if not self.overlap:
            if x < 0 or y < 0 or x >= self.width or y >= self.height:
                raise IndexError

        return self.grid[y][x]

    def __setitem__(self, key, value):
        x, y = key
        self.grid[y][x] = value

    def __iter__(self):
        self.current = (-1, 0)
        return self

    def __next__(self):
        self.current = (self.current[0] + 1, self.current[1])

        if self.current[0] >= self.width:
            self.current = (0, self.current[1] + 1)

        if self.current[1] >= self.height:
            raise StopIteration

        x, y = self.current
        return self.grid[y][x]

    def get_neighbors(
        self,
        x,
        y,
        orientations: GridOrientation = GridOrientation.Horizontal
        | GridOrientation.Vertical
        | GridOrientation.Diagonal,
    ):
        neighbors = set()
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue

                if orientations & GridOrientation.Horizontal and dy == 0 and dx != 0:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        neighbors.add(((x + dx, y + dy), self.grid[y + dy][x + dx]))

                if orientations & GridOrientation.Vertical and dx == 0 and dy != 0:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        neighbors.add(((x + dx, y + dy), self.grid[y + dy][x + dx]))

                if orientations & GridOrientation.Diagonal and dx != 0 and dy != 0:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        neighbors.add(((x + dx, y + dy), self.grid[y + dy][x + dx]))

                if orientations & GridOrientation.Up and dy == -1 and dx == 0:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        neighbors.add(((x + dx, y + dy), self.grid[y + dy][x + dx]))

                if orientations & GridOrientation.Down and dy == 1 and dx == 0:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        neighbors.add(((x + dx, y + dy), self.grid[y + dy][x + dx]))

                if orientations & GridOrientation.Left and dx == -1 and dy == 0:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        neighbors.add(((x + dx, y + dy), self.grid[y + dy][x + dx]))

                if orientations & GridOrientation.Right and dx == 1 and dy == 0:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        neighbors.add(((x + dx, y + dy), self.grid[y + dy][x + dx]))

                if orientations & GridOrientation.UpLeft and dx == -1 and dy == -1:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        neighbors.add(((x + dx, y + dy), self.grid[y + dy][x + dx]))

                if orientations & GridOrientation.UpRight and dx == 1 and dy == -1:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        neighbors.add(((x + dx, y + dy), self.grid[y + dy][x + dx]))

                if orientations & GridOrientation.DownLeft and dx == -1 and dy == 1:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        neighbors.add(((x + dx, y + dy), self.grid[y + dy][x + dx]))

                if orientations & GridOrientation.DownRight and dx == 1 and dy == 1:
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        neighbors.add(((x + dx, y + dy), self.grid[y + dy][x + dx]))

        return neighbors

    def get_adjacent(
        self,
        x,
        y,
        orientations: GridOrientation = GridOrientation.Horizontal
        | GridOrientation.Vertical
        | GridOrientation.Diagonal,
    ):
        return [item[1] for item in self.get_neighbors(x, y, orientations)]

    def search(self, value):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == value:
                    return x, y
        return None

    def search_all(self, value):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == value:
                    yield x, y
        return None

    def count(self, value):
        return sum(1 for cell in self if cell == value)

    def count_value(self, value):
        return sum(1 for cell in self if cell == value)

    def sum_values(self):
        return sum(cell for cell in self if cell is not None)
