class Grid:
    def __init__(self, width, height, default=None, overlap=False):
        self.width = width
        self.height = height
        self.default = default
        self.overlap = overlap
        self.grid = [[default for _ in range(width)] for _ in range(height)]
        self.current = (0, 0)

    @classmethod
    def with_string(cls, string):
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

    def get_neighbors(self, x, y):
        neighbors = []
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                    neighbors.append((x + dx, y + dy))
        return neighbors

    def get_adjacent(self, x, y):
        adjacent = []
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                    adjacent.append(self.grid[y + dy][x + dx])
        return adjacent

    def count_value(self, value):
        return sum(1 for cell in self if cell == value)

    def sum_values(self):
        return sum(cell for cell in self if cell is not None)
