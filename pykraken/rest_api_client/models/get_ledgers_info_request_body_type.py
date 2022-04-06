from enum import Enum


class GetLedgersInfoRequestBodyType(str, Enum):
    ALL = "all"
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"
    TRADE = "trade"
    MARGIN = "margin"

    def __str__(self) -> str:
        return str(self.value)
