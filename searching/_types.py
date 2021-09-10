from __future__ import annotations

from typing import Iterable, Protocol, TypeVar, overload, runtime_checkable

T = TypeVar("T")


@runtime_checkable
class Indexable(Iterable[T], Protocol[T]):
    @overload
    def __getitem__(self, key: int) -> T:
        ...

    @overload
    def __getitem__(self, key: slice) -> Indexable[T]:
        ...


@runtime_checkable
class SizedIndexable(Indexable[T], Protocol[T]):
    def __len__(self) -> int:
        ...
