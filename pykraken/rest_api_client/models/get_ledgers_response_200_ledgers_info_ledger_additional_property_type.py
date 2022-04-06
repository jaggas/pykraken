from enum import Enum


class GetLedgersResponse200LedgersInfoLedgerAdditionalPropertyType(str, Enum):
    TRADE = "trade"
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"
    MARGIN = "margin"
    ROLLOVER = "rollover"
    SPEND = "spend"
    RECEIVE = "receive"
    SETTLED = "settled"
    ADJUSTMENT = "adjustment"

    def __str__(self) -> str:
        return str(self.value)
