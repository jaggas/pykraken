from enum import Enum


class GetClosedOrdersRequestBodyClosetime(str, Enum):
    OPEN = "open"
    CLOSE = "close"
    BOTH = "both"

    def __str__(self) -> str:
        return str(self.value)
