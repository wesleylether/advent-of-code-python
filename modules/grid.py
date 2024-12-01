class Grid:
    def __init__(self, width, height, default=None):
        self.width = width
        self.height = height
        self.grid = [[default for _ in range(width)] for _ in range(height)]
        self.current = (0, 0)

    def __str__(self):
        return "\n".join("".join(str(cell) for cell in row) for row in self.grid)

    def __getitem__(self, key):
        x, y = key
        return self.grid[y][x]

    def __setitem__(self, key, value):
        x, y = key
        self.grid[y][x] = value

    def __iter__(self):
        self.current = (0, 0)
        return self

    def __next__(self):
        if self.current[1] >= self.height:
            raise StopIteration
        x, y = self.current
        value = self.grid[y][x]
        if x + 1 < self.width:
            self.current = (x + 1, y)
        else:
            self.current = (0, y + 1)
        return value

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
