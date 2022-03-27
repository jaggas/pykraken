from enum import Enum


class WithdrawalStatus(str, Enum):
    INITIAL = "Initial"
    PENDING = "Pending"
    SETTLED = "Settled"
    SUCCESS = "Success"
    FAILURE = "Failure"

    def __str__(self) -> str:
        return str(self.value)
