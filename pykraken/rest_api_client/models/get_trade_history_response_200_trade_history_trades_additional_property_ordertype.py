from enum import Enum


class GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyOrdertype(str, Enum):
    MARKET = "market"
    LIMIT = "limit"
    STOP_LOSS = "stop-loss"
    TAKE_PROFIT = "take-profit"
    STOP_LOSS_LIMIT = "stop-loss-limit"
    TAKE_PROFIT_LIMIT = "take-profit-limit"
    SETTLE_POSITION = "settle-position"

    def __str__(self) -> str:
        return str(self.value)
