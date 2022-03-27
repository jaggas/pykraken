from enum import Enum


class GetTradableAssetPairsInfo(str, Enum):
    INFO = "info"
    LEVERAGE = "leverage"
    FEES = "fees"
    MARGIN = "margin"

    def __str__(self) -> str:
        return str(self.value)
