from enum import Enum


class GetOpenOrdersResponse200OpenOrdersOpenAdditionalPropertyTrigger(str, Enum):
    LAST = "last"
    INDEX = "index"

    def __str__(self) -> str:
        return str(self.value)
