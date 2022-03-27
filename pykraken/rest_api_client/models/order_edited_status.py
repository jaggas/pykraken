from enum import Enum


class OrderEditedStatus(str, Enum):
    OK = "ok"
    ERR = "err"

    def __str__(self) -> str:
        return str(self.value)
