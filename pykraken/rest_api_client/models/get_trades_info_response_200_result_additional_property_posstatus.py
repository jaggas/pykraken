from enum import Enum


class GetTradesInfoResponse200ResultAdditionalPropertyPosstatus(str, Enum):
    OPEN = "open"
    CLOSED = "closed"

    def __str__(self) -> str:
        return str(self.value)
