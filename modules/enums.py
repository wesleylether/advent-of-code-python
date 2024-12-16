from enum import Enum


class Direction(Enum):
    Up = (0, -1)
    UpRight = (1, -1)
    Right = (1, 0)
    DownRight = (1, 1)
    Down = (0, 1)
    DownLeft = (-1, 1)
    Left = (-1, 0)
    UpLeft = (-1, -1)

    def __str__(self):
        return self.name


class Navigation(Enum):
    North = (0, -1)
    NorthEast = (1, -1)
    East = (1, 0)
    SouthEast = (1, 1)
    South = (0, 1)
    SouthWest = (-1, 1)
    West = (-1, 0)
    NorthWest = (-1, -1)

    def __str__(self):
        return self.name
