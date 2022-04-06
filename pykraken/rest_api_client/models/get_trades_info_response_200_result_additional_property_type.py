from enum import Enum


class GetTradesInfoResponse200ResultAdditionalPropertyType(str, Enum):
    BUY = "buy"
    SELL = "sell"

    def __str__(self) -> str:
        return str(self.value)
