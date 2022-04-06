from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.position_ordertype import PositionOrdertype
from ..models.position_posstatus import PositionPosstatus
from ..models.position_type import PositionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Position")


@attr.s(auto_attribs=True)
class Position:
    """Position info

    Attributes:
        ordertxid (Union[Unset, str]): Order ID responsible for the position
        posstatus (Union[Unset, PositionPosstatus]): Position status
        pair (Union[Unset, str]): Asset pair
        time (Union[Unset, float]): Unix timestamp of trade
        type (Union[Unset, PositionType]): Order side
              * buy - buy side
              * sell - sell side
        ordertype (Union[Unset, PositionOrdertype]):
        cost (Union[Unset, str]): Opening cost of position (in quote currency)
        fee (Union[Unset, str]): Opening fee of position (in quote currency)
        vol (Union[Unset, str]): Position opening size (in base currency)
        vol_closed (Union[Unset, str]): Quantity closed (in base currency)
        margin (Union[Unset, str]): Initial margin consumed (in quote currency)
        value (Union[Unset, str]): Current value of remaining position (if `docalcs` requested)
        net (Union[Unset, str]): Unrealised P&L of remaining position (if `docalcs` requested)
        terms (Union[Unset, str]): Funding cost and term of position
        rollovertm (Union[Unset, str]): Timestamp of next margin rollover fee
        misc (Union[Unset, str]): Comma delimited list of add'l info
        oflags (Union[Unset, str]): Comma delimited list of opening order flags
    """

    ordertxid: Union[Unset, str] = UNSET
    posstatus: Union[Unset, PositionPosstatus] = UNSET
    pair: Union[Unset, str] = UNSET
    time: Union[Unset, float] = UNSET
    type: Union[Unset, PositionType] = UNSET
    ordertype: Union[Unset, PositionOrdertype] = UNSET
    cost: Union[Unset, str] = UNSET
    fee: Union[Unset, str] = UNSET
    vol: Union[Unset, str] = UNSET
    vol_closed: Union[Unset, str] = UNSET
    margin: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    net: Union[Unset, str] = UNSET
    terms: Union[Unset, str] = UNSET
    rollovertm: Union[Unset, str] = UNSET
    misc: Union[Unset, str] = UNSET
    oflags: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ordertxid = self.ordertxid
        posstatus: Union[Unset, str] = UNSET
        if not isinstance(self.posstatus, Unset):
            posstatus = self.posstatus.value

        pair = self.pair
        time = self.time
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        ordertype: Union[Unset, str] = UNSET
        if not isinstance(self.ordertype, Unset):
            ordertype = self.ordertype.value

        cost = self.cost
        fee = self.fee
        vol = self.vol
        vol_closed = self.vol_closed
        margin = self.margin
        value = self.value
        net = self.net
        terms = self.terms
        rollovertm = self.rollovertm
        misc = self.misc
        oflags = self.oflags

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ordertxid is not UNSET:
            field_dict["ordertxid"] = ordertxid
        if posstatus is not UNSET:
            field_dict["posstatus"] = posstatus
        if pair is not UNSET:
            field_dict["pair"] = pair
        if time is not UNSET:
            field_dict["time"] = time
        if type is not UNSET:
            field_dict["type"] = type
        if ordertype is not UNSET:
            field_dict["ordertype"] = ordertype
        if cost is not UNSET:
            field_dict["cost"] = cost
        if fee is not UNSET:
            field_dict["fee"] = fee
        if vol is not UNSET:
            field_dict["vol"] = vol
        if vol_closed is not UNSET:
            field_dict["vol_closed"] = vol_closed
        if margin is not UNSET:
            field_dict["margin"] = margin
        if value is not UNSET:
            field_dict["value"] = value
        if net is not UNSET:
            field_dict["net"] = net
        if terms is not UNSET:
            field_dict["terms"] = terms
        if rollovertm is not UNSET:
            field_dict["rollovertm"] = rollovertm
        if misc is not UNSET:
            field_dict["misc"] = misc
        if oflags is not UNSET:
            field_dict["oflags"] = oflags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        ordertxid = d.pop("ordertxid", UNSET)

        _posstatus = d.pop("posstatus", UNSET)
        posstatus: Union[Unset, PositionPosstatus]
        if isinstance(_posstatus, Unset):
            posstatus = UNSET
        else:
            posstatus = PositionPosstatus(_posstatus)

        pair = d.pop("pair", UNSET)

        time = d.pop("time", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, PositionType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = PositionType(_type)

        _ordertype = d.pop("ordertype", UNSET)
        ordertype: Union[Unset, PositionOrdertype]
        if isinstance(_ordertype, Unset):
            ordertype = UNSET
        else:
            ordertype = PositionOrdertype(_ordertype)

        cost = d.pop("cost", UNSET)

        fee = d.pop("fee", UNSET)

        vol = d.pop("vol", UNSET)

        vol_closed = d.pop("vol_closed", UNSET)

        margin = d.pop("margin", UNSET)

        value = d.pop("value", UNSET)

        net = d.pop("net", UNSET)

        terms = d.pop("terms", UNSET)

        rollovertm = d.pop("rollovertm", UNSET)

        misc = d.pop("misc", UNSET)

        oflags = d.pop("oflags", UNSET)

        position = cls(
            ordertxid=ordertxid,
            posstatus=posstatus,
            pair=pair,
            time=time,
            type=type,
            ordertype=ordertype,
            cost=cost,
            fee=fee,
            vol=vol,
            vol_closed=vol_closed,
            margin=margin,
            value=value,
            net=net,
            terms=terms,
            rollovertm=rollovertm,
            misc=misc,
            oflags=oflags,
        )

        position.additional_properties = d
        return position

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
