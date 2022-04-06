from enum import Enum


class InlineResponse20037RewardsType(str, Enum):
    PERCENTAGE = "percentage"

    def __str__(self) -> str:
        return str(self.value)
