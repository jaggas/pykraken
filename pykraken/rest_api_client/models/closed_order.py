from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.closed_order_descr import ClosedOrderDescr
from ..models.closed_order_status import ClosedOrderStatus
from ..models.closed_order_trigger import ClosedOrderTrigger
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClosedOrder")


@attr.s(auto_attribs=True)
class ClosedOrder:
    """Closed order

    Attributes:
        refid (Union[Unset, str]): Referral order transaction ID that created this order
        userref (Union[Unset, str]): User reference id
        status (Union[Unset, ClosedOrderStatus]): Status of order
              * pending - order pending book entry
              * open - open order
              * closed - closed order
              * canceled - order canceled
              * expired - order expired
        opentm (Union[Unset, float]): Unix timestamp of when order was placed
        starttm (Union[Unset, float]): Unix timestamp of order start time (or 0 if not set)
        expiretm (Union[Unset, float]): Unix timestamp of order end time (or 0 if not set)
        descr (Union[Unset, ClosedOrderDescr]): Order description info
        vol (Union[Unset, str]): Volume of order (base currency)
        vol_exec (Union[Unset, str]): Volume executed (base currency)
        cost (Union[Unset, str]): Total cost (quote currency unless)
        fee (Union[Unset, str]): Total fee (quote currency)
        price (Union[Unset, str]): Average price (quote currency)
        stopprice (Union[Unset, str]): Stop price (quote currency)
        limitprice (Union[Unset, str]): Triggered limit price (quote currency, when limit based order type triggered)
        trigger (Union[Unset, ClosedOrderTrigger]): Price signal used to trigger "stop-loss"
            "take-profit" "stop-loss-limit"
            "take-profit-limit" orders.
              * `last` is the implied trigger if this field is not set.
             Default: ClosedOrderTrigger.LAST.
        misc (Union[Unset, str]): Comma delimited list of miscellaneous info

              * `stopped` triggered by stop price
              * `touched` triggered by touch price
              * `liquidated` liquidation
              * `partial` partial fill
        oflags (Union[Unset, str]): Comma delimited list of order flags

              * `post` post-only order (available when ordertype = limit)
              * `fcib` prefer fee in base currency (default if selling)
              * `fciq` prefer fee in quote currency (default if buying, mutually exclusive with `fcib`)
              * `nompp` disable [market price protection](https://support.kraken.com/hc/en-us/articles/201648183-Market-
            Price-Protection) for market orders
        trades (Union[Unset, List[str]]): List of trade IDs related to order (if trades info requested and data
            available)
        closetm (Union[Unset, float]): Unix timestamp of when order was closed
        reason (Union[Unset, str]): Additional info on status (if any)
    """

    refid: Union[Unset, str] = UNSET
    userref: Union[Unset, str] = UNSET
    status: Union[Unset, ClosedOrderStatus] = UNSET
    opentm: Union[Unset, float] = UNSET
    starttm: Union[Unset, float] = UNSET
    expiretm: Union[Unset, float] = UNSET
    descr: Union[Unset, ClosedOrderDescr] = UNSET
    vol: Union[Unset, str] = UNSET
    vol_exec: Union[Unset, str] = UNSET
    cost: Union[Unset, str] = UNSET
    fee: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    stopprice: Union[Unset, str] = UNSET
    limitprice: Union[Unset, str] = UNSET
    trigger: Union[Unset, ClosedOrderTrigger] = ClosedOrderTrigger.LAST
    misc: Union[Unset, str] = UNSET
    oflags: Union[Unset, str] = UNSET
    trades: Union[Unset, List[str]] = UNSET
    closetm: Union[Unset, float] = UNSET
    reason: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refid = self.refid
        userref = self.userref
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        opentm = self.opentm
        starttm = self.starttm
        expiretm = self.expiretm
        descr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descr, Unset):
            descr = self.descr.to_dict()

        vol = self.vol
        vol_exec = self.vol_exec
        cost = self.cost
        fee = self.fee
        price = self.price
        stopprice = self.stopprice
        limitprice = self.limitprice
        trigger: Union[Unset, str] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        misc = self.misc
        oflags = self.oflags
        trades: Union[Unset, List[str]] = UNSET
        if not isinstance(self.trades, Unset):
            trades = self.trades

        closetm = self.closetm
        reason = self.reason

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refid is not UNSET:
            field_dict["refid"] = refid
        if userref is not UNSET:
            field_dict["userref"] = userref
        if status is not UNSET:
            field_dict["status"] = status
        if opentm is not UNSET:
            field_dict["opentm"] = opentm
        if starttm is not UNSET:
            field_dict["starttm"] = starttm
        if expiretm is not UNSET:
            field_dict["expiretm"] = expiretm
        if descr is not UNSET:
            field_dict["descr"] = descr
        if vol is not UNSET:
            field_dict["vol"] = vol
        if vol_exec is not UNSET:
            field_dict["vol_exec"] = vol_exec
        if cost is not UNSET:
            field_dict["cost"] = cost
        if fee is not UNSET:
            field_dict["fee"] = fee
        if price is not UNSET:
            field_dict["price"] = price
        if stopprice is not UNSET:
            field_dict["stopprice"] = stopprice
        if limitprice is not UNSET:
            field_dict["limitprice"] = limitprice
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if misc is not UNSET:
            field_dict["misc"] = misc
        if oflags is not UNSET:
            field_dict["oflags"] = oflags
        if trades is not UNSET:
            field_dict["trades"] = trades
        if closetm is not UNSET:
            field_dict["closetm"] = closetm
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        refid = d.pop("refid", UNSET)

        userref = d.pop("userref", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ClosedOrderStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ClosedOrderStatus(_status)

        opentm = d.pop("opentm", UNSET)

        starttm = d.pop("starttm", UNSET)

        expiretm = d.pop("expiretm", UNSET)

        _descr = d.pop("descr", UNSET)
        descr: Union[Unset, ClosedOrderDescr]
        if isinstance(_descr, Unset):
            descr = UNSET
        else:
            descr = ClosedOrderDescr.from_dict(_descr)

        vol = d.pop("vol", UNSET)

        vol_exec = d.pop("vol_exec", UNSET)

        cost = d.pop("cost", UNSET)

        fee = d.pop("fee", UNSET)

        price = d.pop("price", UNSET)

        stopprice = d.pop("stopprice", UNSET)

        limitprice = d.pop("limitprice", UNSET)

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, ClosedOrderTrigger]
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = ClosedOrderTrigger(_trigger)

        misc = d.pop("misc", UNSET)

        oflags = d.pop("oflags", UNSET)

        trades = cast(List[str], d.pop("trades", UNSET))

        closetm = d.pop("closetm", UNSET)

        reason = d.pop("reason", UNSET)

        closed_order = cls(
            refid=refid,
            userref=userref,
            status=status,
            opentm=opentm,
            starttm=starttm,
            expiretm=expiretm,
            descr=descr,
            vol=vol,
            vol_exec=vol_exec,
            cost=cost,
            fee=fee,
            price=price,
            stopprice=stopprice,
            limitprice=limitprice,
            trigger=trigger,
            misc=misc,
            oflags=oflags,
            trades=trades,
            closetm=closetm,
            reason=reason,
        )

        closed_order.additional_properties = d
        return closed_order

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
