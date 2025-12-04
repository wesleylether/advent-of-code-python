import operator
from collections import UserList
from functools import reduce
from itertools import starmap, accumulate, combinations, permutations
from math import prod
from statistics import median

from typing import TypeVar, Generic, Iterator

T = TypeVar("T")


class List(Generic[T], UserList[T]):
    _SENTINEL = object()

    def enumerate(self) -> Iterator[T]:
        return enumerate(self)

    def filter(self, func) -> "List[T]":
        return List(filter(func, self))

    def iter(self) -> Iterator[T]:
        return iter(self)

    def length(self) -> int:
        return len(self)

    def map(self, func) -> "List[T]":
        return List(map(func, self))

    def star_map(self, func) -> "List[T]":
        return List(starmap(func, self))

    def map_each(self, func) -> "List[List[T]]":
        return self.map(lambda i: List(map(func, i)))

    def star_map_each(self, func) -> "List[List[T]]":
        return self.map(lambda i: List(starmap(func, i)))

    def reduce(self, func, initial=None):
        return reduce(func, self, initial)

    def swap_items(self, i: int, j: int) -> "List[T]":
        self[i], self[j] = self[j], self[i]
        return self

    def find(self, func) -> T:
        return next(filter(func, self), self._SENTINEL)

    def any(self, func) -> bool:
        return any(map(func, self))

    def all(self, func) -> bool:
        return all(map(func, self))

    def none(self, func) -> bool:
        return not any(map(func, self))

    def window(self, size: int) -> "List[List[T]]":
        return List([self[i : i + size] for i in range(len(self) - size + 1)])

    def chunk(self, size: int) -> "List[List[T]]":
        return List([self[i : i + size] for i in range(0, len(self), size)])

    def accumulate(self, func=operator.add, initial=_SENTINEL) -> "List[T]":
        if initial is self._SENTINEL:
            return List(accumulate(self, func))

        return List(accumulate(self, func, initial=initial))

    def sum(self, initial=_SENTINEL) -> int:
        if initial is self._SENTINEL:
            return sum(self)

        return sum(self, initial)  # type: ignore

    def prod(self, initial=_SENTINEL) -> int:
        if initial is self._SENTINEL:
            return prod(self)

        return prod(self, start=initial)  # type: ignore

    def min(self):
        return min(self)

    def max(self):
        return max(self)

    def mean(self):
        return self.sum() / len(self)

    def median(self):
        return median(self)

    def flatten(self) -> "List[T]":
        return List(
            reduce(
                operator.add,
                map(lambda i: i.flatten() if isinstance(i, List) else [i], self),
                [],
            )
        )

    def deepcopy(self) -> "List[T]":
        from copy import deepcopy

        return List(deepcopy(self.data))

    def transpose(self) -> "List[T]":
        return List(zip(*self)).map(List)

    def reverse(self) -> "List[T]":
        return List(reversed(self))

    def permutations(self, r: int) -> "List[List[T]]":
        return List([List(i) for i in permutations(self, r)])

    def combinations(self, r: int) -> "List[List[T]]":
        return List([List(i) for i in combinations(self, r)])
