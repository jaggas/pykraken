from enum import Enum


class GetOpenOrdersResponse200OpenOrdersOpenAdditionalPropertyDescrType(str, Enum):
    BUY = "buy"
    SELL = "sell"

    def __str__(self) -> str:
        return str(self.value)
