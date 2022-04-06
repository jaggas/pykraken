from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.trade_history_trades import TradeHistoryTrades
from ..types import UNSET, Unset

T = TypeVar("T", bound="TradeHistory")


@attr.s(auto_attribs=True)
class TradeHistory:
    """Trade History

    Attributes:
        trades (Union[Unset, TradeHistoryTrades]): Trade info
        count (Union[Unset, int]): Amount of available trades matching criteria
    """

    trades: Union[Unset, TradeHistoryTrades] = UNSET
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
        trades: Union[Unset, TradeHistoryTrades]
        if isinstance(_trades, Unset):
            trades = UNSET
        else:
            trades = TradeHistoryTrades.from_dict(_trades)

        count = d.pop("count", UNSET)

        trade_history = cls(
            trades=trades,
            count=count,
        )

        trade_history.additional_properties = d
        return trade_history

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