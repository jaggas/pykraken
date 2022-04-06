from enum import Enum


class GetTradesHistoryRequestBodyType(str, Enum):
    ALL = "all"
    ANY_POSITION = "any position"
    CLOSED_POSITION = "closed position"
    CLOSING_POSITION = "closing position"
    NO_POSITION = "no position"

    def __str__(self) -> str:
        return str(self.value)
