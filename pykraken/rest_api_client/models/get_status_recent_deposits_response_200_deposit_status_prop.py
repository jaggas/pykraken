from enum import Enum


class GetStatusRecentDepositsResponse200DepositStatusProp(str, Enum):
    RETURN = "return"
    ONHOLD = "onhold"

    def __str__(self) -> str:
        return str(self.value)
