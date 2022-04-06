from enum import Enum


class AddStandardOrderRequestBodyTrigger(str, Enum):
    INDEX = "index"
    LAST = "last"

    def __str__(self) -> str:
        return str(self.value)
