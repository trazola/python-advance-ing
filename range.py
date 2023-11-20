from dataclasses import dataclass
from typing import Self

@dataclass
class CustomRange:
    start: int
    end: int

    def __post_init__(self) -> None:
        self.current_value = self._first_number_in_range

    @property
    def _first_number_in_range(self) -> int:
        return self.start - 1 

    def __iter__(self) -> Self:
        return self
    
    def __next__(self) -> int:
        if self.current_value == self.end:
            self.current_value = self._first_number_in_range
            raise StopIteration
        self.current_value += 1
        return self.current_value

custom_range = CustomRange(start=1, end=3)
list(custom_range)
