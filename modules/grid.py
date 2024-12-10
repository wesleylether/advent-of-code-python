from enum import Flag, auto, Enum


class GridValueType(Enum):
    String = auto()
    Int = auto()
    List = auto()
    Tuple = auto()
    Dict = auto()
    Set = auto()
    Float = auto()
    Bool = auto()
    NoneType = auto()


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
    def from_string(cls, string, grid_type: GridValueType = GridValueType.String):
        lines = string.splitlines()
        height = len(lines)
        width = max(len(line) for line in lines)
        grid = cls(width, height)
        grid.init_with_string(string, grid_type)
        return grid

    def init_with_string(self, string, grid_type: GridValueType):
        for y, row in enumerate(string.splitlines()):
            for x, cell in enumerate(row):
                match grid_type:
                    case GridValueType.String:
                        self.grid[y][x] = str(cell)
                    case GridValueType.Int:
                        self.grid[y][x] = int(cell)
                    case _:
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
        return self.grid[y][x], (x, y)

    def values(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                yield cell

    def get_neighbors(
        self,
        position,
        orientations: GridOrientation = GridOrientation.Horizontal
        | GridOrientation.Vertical
        | GridOrientation.Diagonal,
    ):
        x, y = position
        neighbors = set()
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue

                if (
                    (orientations & GridOrientation.Horizontal and dy == 0 and dx != 0)
                    or (orientations & GridOrientation.Vertical and dx == 0 and dy != 0)
                    or (orientations & GridOrientation.Diagonal and dx != 0 and dy != 0)
                    or (orientations & GridOrientation.Up and dy == -1 and dx == 0)
                    or (orientations & GridOrientation.Down and dy == 1 and dx == 0)
                    or (orientations & GridOrientation.Left and dx == -1 and dy == 0)
                    or (orientations & GridOrientation.Right and dx == 1 and dy == 0)
                    or (orientations & GridOrientation.UpLeft and dx == -1 and dy == -1)
                    or (orientations & GridOrientation.UpRight and dx == 1 and dy == -1)
                    or (orientations & GridOrientation.DownLeft and dx == -1 and dy == 1)
                    or (orientations & GridOrientation.DownRight and dx == 1 and dy == 1)
                ):
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        neighbors.add((self.grid[y + dy][x + dx], (x + dx, y + dy)))

        return neighbors

    def get_adjacent(
        self,
        position,
        orientations: GridOrientation = GridOrientation.Horizontal
        | GridOrientation.Vertical
        | GridOrientation.Diagonal,
    ):
        return [item[0] for item in self.get_neighbors(position, orientations)]

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
        return sum(1 for cell in self if cell[0] == value)

    def count_value(self, value):
        return sum(1 for cell in self if cell[0] == value)

    def sum_values(self):
        return sum(cell[0] for cell in self if cell is not None)
