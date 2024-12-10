from enum import Enum


class Direction(Enum):
    North = 0
    NorthEast = 1
    East = 2
    SouthEast = 3
    South = 4
    SouthWest = 5
    West = 6
    NorthWest = 7

    def __str__(self):
        return self.name


class Orientation(Enum):
    Horizontal = 0
    Vertical = 1
    Diagonal = 2

    def __str__(self):
        return self.name
