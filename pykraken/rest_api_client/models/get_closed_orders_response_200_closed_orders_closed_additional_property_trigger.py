from enum import Enum


class GetClosedOrdersResponse200ClosedOrdersClosedAdditionalPropertyTrigger(str, Enum):
    LAST = "last"
    INDEX = "index"

    def __str__(self) -> str:
        return str(self.value)
