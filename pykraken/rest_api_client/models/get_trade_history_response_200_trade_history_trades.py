from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.trade import Trade

T = TypeVar("T", bound="GetTradeHistoryResponse200TradeHistoryTrades")


@attr.s(auto_attribs=True)
class GetTradeHistoryResponse200TradeHistoryTrades:
    """Trade info"""

    additional_properties: Dict[str, Trade] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_trade_history_response_200_trade_history_trades = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = Trade.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_trade_history_response_200_trade_history_trades.additional_properties = additional_properties
        return get_trade_history_response_200_trade_history_trades

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Trade:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Trade) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
