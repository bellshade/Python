from __future__ import annotations

import Iterable
import overload
import Protocol
import runtime_checkable
import TypeVar

T = TypeVar("T")


@runtime_checkable
class SizedIndexable(Iterable[T], Protocol[T]):
    @overload
    def __getitem__(self, key: int) -> T:
        ...

    @overload
    def __getitem__(self, key: slice) -> SizedIndexable[T]:
        ...

    def __len__(self) -> int:
        ...
