from enum import Enum


class OpenOrderTrigger(str, Enum):
    LAST = "last"
    INDEX = "index"

    def __str__(self) -> str:
        return str(self.value)
