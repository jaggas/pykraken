from enum import Enum


class GetClosedOrdersResponse200ClosedOrdersClosedAdditionalPropertyDescrType(str, Enum):
    BUY = "buy"
    SELL = "sell"

    def __str__(self) -> str:
        return str(self.value)
