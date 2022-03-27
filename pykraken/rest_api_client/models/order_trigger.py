from enum import Enum


class OrderTrigger(str, Enum):
    LAST = "last"
    INDEX = "index"

    def __str__(self) -> str:
        return str(self.value)
