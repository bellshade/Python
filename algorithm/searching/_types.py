from __future__ import annotations

from typing import Iterable, Protocol, TypeVar, overload, runtime_checkable

T = TypeVar("T")


@runtime_checkable
class SizedIndexable(Iterable[T], Protocol[T]):
    @overload
    def __getitem__(self, key: slice) -> SizedIndexable[T]: ...

    def __len__(self) -> int: ...
