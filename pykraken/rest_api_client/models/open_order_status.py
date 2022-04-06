from enum import Enum


class OpenOrderStatus(str, Enum):
    PENDING = "pending"
    OPEN = "open"
    CLOSED = "closed"
    CANCELED = "canceled"
    EXPIRED = "expired"

    def __str__(self) -> str:
        return str(self.value)
