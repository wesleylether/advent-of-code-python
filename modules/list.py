from collections import UserList


from typing import TypeVar, Generic, Iterator

T = TypeVar("T")


class List(Generic[T], UserList[T]):
    def iter(self) -> Iterator[T]:
        return iter(self)

    def swap_items(self, i: int, j: int) -> "List[T]":
        self[i], self[j] = self[j], self[i]
        return self
