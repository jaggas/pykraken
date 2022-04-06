from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.get_trade_history_response_200_trade_history_trades_additional_property_ordertype import (
    GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyOrdertype,
)
from ..models.get_trade_history_response_200_trade_history_trades_additional_property_posstatus import (
    GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyPosstatus,
)
from ..models.get_trade_history_response_200_trade_history_trades_additional_property_type import (
    GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTradeHistoryResponse200TradeHistoryTradesAdditionalProperty")


@attr.s(auto_attribs=True)
class GetTradeHistoryResponse200TradeHistoryTradesAdditionalProperty:
    """
    Attributes:
        ordertxid (Union[Unset, str]): Order responsible for execution of trade
        pair (Union[Unset, str]): Asset pair
        time (Union[Unset, float]): Unix timestamp of trade
        type (Union[Unset, GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyType]): Order side
              * buy - buy side
              * sell - sell side
        ordertype (Union[Unset, GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyOrdertype]):
        price (Union[Unset, str]): Average price order was executed at (quote currency)
        cost (Union[Unset, str]): Total cost of order (quote currency)
        fee (Union[Unset, str]): Total fee (quote currency)
        vol (Union[Unset, str]): Volume (base currency)
        margin (Union[Unset, str]): Initial margin (quote currency)
        misc (Union[Unset, str]): Comma delimited list of miscellaneous info:
            * `closing` &mdash; Trade closes all or part of a position
        posstatus (Union[Unset, GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyPosstatus]): Position
            status (open/closed) <br><sub><sup>Only present if trade opened a position</sub></sup>
        cprice (Union[Unset, Any]): Average price of closed portion of position (quote currency)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
        ccost (Union[Unset, Any]): Total cost of closed portion of position (quote currency)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
        cfee (Union[Unset, Any]): Total fee of closed portion of position (quote currency)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
        cvol (Union[Unset, Any]): Total fee of closed portion of position (quote currency)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
        cmargin (Union[Unset, Any]): Total margin freed in closed portion of position (quote currency)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
        net (Union[Unset, Any]): Net profit/loss of closed portion of position (quote currency, quote currency scale)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
        trades (Union[Unset, List[str]]): List of closing trades for position (if available)
            <br><sub><sup>Only present if trade opened a position</sub></sup>
    """

    ordertxid: Union[Unset, str] = UNSET
    pair: Union[Unset, str] = UNSET
    time: Union[Unset, float] = UNSET
    type: Union[Unset, GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyType] = UNSET
    ordertype: Union[Unset, GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyOrdertype] = UNSET
    price: Union[Unset, str] = UNSET
    cost: Union[Unset, str] = UNSET
    fee: Union[Unset, str] = UNSET
    vol: Union[Unset, str] = UNSET
    margin: Union[Unset, str] = UNSET
    misc: Union[Unset, str] = UNSET
    posstatus: Union[Unset, GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyPosstatus] = UNSET
    cprice: Union[Unset, Any] = UNSET
    ccost: Union[Unset, Any] = UNSET
    cfee: Union[Unset, Any] = UNSET
    cvol: Union[Unset, Any] = UNSET
    cmargin: Union[Unset, Any] = UNSET
    net: Union[Unset, Any] = UNSET
    trades: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ordertxid = self.ordertxid
        pair = self.pair
        time = self.time
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        ordertype: Union[Unset, str] = UNSET
        if not isinstance(self.ordertype, Unset):
            ordertype = self.ordertype.value

        price = self.price
        cost = self.cost
        fee = self.fee
        vol = self.vol
        margin = self.margin
        misc = self.misc
        posstatus: Union[Unset, str] = UNSET
        if not isinstance(self.posstatus, Unset):
            posstatus = self.posstatus.value

        cprice = self.cprice
        ccost = self.ccost
        cfee = self.cfee
        cvol = self.cvol
        cmargin = self.cmargin
        net = self.net
        trades: Union[Unset, List[str]] = UNSET
        if not isinstance(self.trades, Unset):
            trades = self.trades

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ordertxid is not UNSET:
            field_dict["ordertxid"] = ordertxid
        if pair is not UNSET:
            field_dict["pair"] = pair
        if time is not UNSET:
            field_dict["time"] = time
        if type is not UNSET:
            field_dict["type"] = type
        if ordertype is not UNSET:
            field_dict["ordertype"] = ordertype
        if price is not UNSET:
            field_dict["price"] = price
        if cost is not UNSET:
            field_dict["cost"] = cost
        if fee is not UNSET:
            field_dict["fee"] = fee
        if vol is not UNSET:
            field_dict["vol"] = vol
        if margin is not UNSET:
            field_dict["margin"] = margin
        if misc is not UNSET:
            field_dict["misc"] = misc
        if posstatus is not UNSET:
            field_dict["posstatus"] = posstatus
        if cprice is not UNSET:
            field_dict["cprice"] = cprice
        if ccost is not UNSET:
            field_dict["ccost"] = ccost
        if cfee is not UNSET:
            field_dict["cfee"] = cfee
        if cvol is not UNSET:
            field_dict["cvol"] = cvol
        if cmargin is not UNSET:
            field_dict["cmargin"] = cmargin
        if net is not UNSET:
            field_dict["net"] = net
        if trades is not UNSET:
            field_dict["trades"] = trades

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ordertxid = d.pop("ordertxid", UNSET)

        pair = d.pop("pair", UNSET)

        time = d.pop("time", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyType(_type)

        _ordertype = d.pop("ordertype", UNSET)
        ordertype: Union[Unset, GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyOrdertype]
        if isinstance(_ordertype, Unset):
            ordertype = UNSET
        else:
            ordertype = GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyOrdertype(_ordertype)

        price = d.pop("price", UNSET)

        cost = d.pop("cost", UNSET)

        fee = d.pop("fee", UNSET)

        vol = d.pop("vol", UNSET)

        margin = d.pop("margin", UNSET)

        misc = d.pop("misc", UNSET)

        _posstatus = d.pop("posstatus", UNSET)
        posstatus: Union[Unset, GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyPosstatus]
        if isinstance(_posstatus, Unset):
            posstatus = UNSET
        else:
            posstatus = GetTradeHistoryResponse200TradeHistoryTradesAdditionalPropertyPosstatus(_posstatus)

        cprice = d.pop("cprice", UNSET)

        ccost = d.pop("ccost", UNSET)

        cfee = d.pop("cfee", UNSET)

        cvol = d.pop("cvol", UNSET)

        cmargin = d.pop("cmargin", UNSET)

        net = d.pop("net", UNSET)

        trades = cast(List[str], d.pop("trades", UNSET))

        get_trade_history_response_200_trade_history_trades_additional_property = cls(
            ordertxid=ordertxid,
            pair=pair,
            time=time,
            type=type,
            ordertype=ordertype,
            price=price,
            cost=cost,
            fee=fee,
            vol=vol,
            margin=margin,
            misc=misc,
            posstatus=posstatus,
            cprice=cprice,
            ccost=ccost,
            cfee=cfee,
            cvol=cvol,
            cmargin=cmargin,
            net=net,
            trades=trades,
        )

        get_trade_history_response_200_trade_history_trades_additional_property.additional_properties = d
        return get_trade_history_response_200_trade_history_trades_additional_property

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
