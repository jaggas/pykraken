from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_trade_history_response_200_trade_history_trades import GetTradeHistoryResponse200TradeHistoryTrades
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTradeHistoryResponse200TradeHistory")


@attr.s(auto_attribs=True)
class GetTradeHistoryResponse200TradeHistory:
    """Trade History

    Attributes:
        trades (Union[Unset, GetTradeHistoryResponse200TradeHistoryTrades]): Trade info
        count (Union[Unset, int]): Amount of available trades matching criteria
    """

    trades: Union[Unset, GetTradeHistoryResponse200TradeHistoryTrades] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        trades: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.trades, Unset):
            trades = self.trades.to_dict()

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if trades is not UNSET:
            field_dict["trades"] = trades
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _trades = d.pop("trades", UNSET)
        trades: Union[Unset, GetTradeHistoryResponse200TradeHistoryTrades]
        if isinstance(_trades, Unset):
            trades = UNSET
        else:
            trades = GetTradeHistoryResponse200TradeHistoryTrades.from_dict(_trades)

        count = d.pop("count", UNSET)

        get_trade_history_response_200_trade_history = cls(
            trades=trades,
            count=count,
        )

        get_trade_history_response_200_trade_history.additional_properties = d
        return get_trade_history_response_200_trade_history

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
