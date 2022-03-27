from enum import Enum


class GetStatusRecentWithdrawalsResponse200WithdrawalStatusProp(str, Enum):
    CANCEL_PENDING = "cancel-pending"
    CANCELED = "canceled"
    CANCEL_DENIED = "cancel-denied"
    RETURN = "return"
    ONHOLD = "onhold"

    def __str__(self) -> str:
        return str(self.value)
