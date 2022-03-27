from enum import Enum


class StakingTransactionInfoType(str, Enum):
    BONDING = "bonding"
    REWARD = "reward"
    UNBONDING = "unbonding"

    def __str__(self) -> str:
        return str(self.value)
