from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.add_standard_order_request_body_closeordertype import AddStandardOrderRequestBodyCloseordertype
from ..models.add_standard_order_request_body_ordertype import AddStandardOrderRequestBodyOrdertype
from ..models.add_standard_order_request_body_timeinforce import AddStandardOrderRequestBodyTimeinforce
from ..models.add_standard_order_request_body_trigger import AddStandardOrderRequestBodyTrigger
from ..models.add_standard_order_request_body_type import AddStandardOrderRequestBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddStandardOrderRequestBody")


@attr.s(auto_attribs=True)
class AddStandardOrderRequestBody:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        ordertype (AddStandardOrderRequestBodyOrdertype): Order type
        type (AddStandardOrderRequestBodyType): Order direction (buy/sell)
        pair (str): Asset pair `id` or `altname`
        userref (Union[Unset, int]): User reference id

            `userref` is an optional user-specified integer id that can be associated with any number of orders. Many
            clients choose a `userref` corresponding to a unique integer id generated by their systems (e.g. a timestamp).
            However, because we don't enforce uniqueness on our side, it can also be used to easily group orders by pair,
            side, strategy, etc. This allows clients to more readily cancel or query information about orders in a
            particular group, with fewer API calls by using `userref` instead of our `txid`, where supported.
        volume (Union[Unset, str]): Order quantity in terms of the base asset
            > Note: Volume can be specified as `0` for closing margin orders to automatically fill the requisite quantity.
        price (Union[Unset, str]): Price

            * Limit price for `limit` orders
            * Trigger price for `stop-loss`, `stop-loss-limit`, `take-profit` and `take-profit-limit` orders
        price2 (Union[Unset, str]): Secondary Price

            * Limit price for `stop-loss-limit` and `take-profit-limit` orders

            >  Note: Either `price` or `price2` can be preceded by `+`, `-`, or `#` to specify the order price as an offset
            relative to the last traded price. `+` adds the amount to, and `-` subtracts the amount from the last traded
            price. `#` will either add or subtract the amount to the last traded price, depending on the direction and order
            type used. Relative prices can be suffixed with a `%` to signify the relative amount as a percentage.
        trigger (Union[Unset, AddStandardOrderRequestBodyTrigger]): Price signal used to trigger `stop-loss`, `stop-
            loss-limit`, `take-profit` and `take-profit-limit` orders.
            >  Note: This `trigger` type will as well be used for associated conditional close orders.
             Default: AddStandardOrderRequestBodyTrigger.LAST.
        leverage (Union[Unset, str]): Amount of leverage desired (default = none)
        oflags (Union[Unset, str]): Comma delimited list of order flags

              * `post` post-only order (available when ordertype = limit)
              * `fcib` prefer fee in base currency (default if selling)
              * `fciq` prefer fee in quote currency (default if buying, mutually exclusive with `fcib`)
              * `nompp` disable [market price protection](https://support.kraken.com/hc/en-us/articles/201648183-Market-
            Price-Protection) for market orders
        timeinforce (Union[Unset, AddStandardOrderRequestBodyTimeinforce]): Time-in-force of the order to specify how
            long it should remain in the order book before being cancelled. GTC (Good-'til-cancelled) is default if the
            parameter is omitted. IOC (immediate-or-cancel) will immediately execute the amount possible and cancel any
            remaining balance rather than resting in the book. GTD (good-'til-date), if specified, must coincide with a
            desired `expiretm`.
             Default: AddStandardOrderRequestBodyTimeinforce.GTC.
        starttm (Union[Unset, str]): Scheduled start time. Can be specified as an absolute timestamp or as a number of
            seconds in the future.
              * `0` now (default)
              * `+<n>` schedule start time <n> seconds from now
              * `<n>` = unix timestamp of start time
        expiretm (Union[Unset, str]): Expiration time
              * `0` no expiration (default)
              * `+<n>` = expire <n> seconds from now, minimum 5 seconds
              * `<n>` = unix timestamp of expiration time
        closeordertype (Union[Unset, AddStandardOrderRequestBodyCloseordertype]): Conditional close order type.
            > Note: [Conditional close orders](https://support.kraken.com/hc/en-us/articles/360038640052-Conditional-Close)
            are triggered by execution of the primary order in the same quantity and opposite direction, but once triggered
            are __independent orders__ that may reduce or increase net position.
        closeprice (Union[Unset, str]): Conditional close order `price`
        closeprice2 (Union[Unset, str]): Conditional close order `price2`
        deadline (Union[Unset, str]): RFC3339 timestamp (e.g. 2021-04-01T00:18:45Z) after which the matching engine
            should reject the new order request, in presence of latency or order queueing. min now() + 5 seconds, max now()
            + 60 seconds.
        validate (Union[Unset, bool]): Validate inputs only. Do not submit order.
    """

    nonce: int
    ordertype: AddStandardOrderRequestBodyOrdertype
    type: AddStandardOrderRequestBodyType
    pair: str
    userref: Union[Unset, int] = UNSET
    volume: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    price2: Union[Unset, str] = UNSET
    trigger: Union[Unset, AddStandardOrderRequestBodyTrigger] = AddStandardOrderRequestBodyTrigger.LAST
    leverage: Union[Unset, str] = UNSET
    oflags: Union[Unset, str] = UNSET
    timeinforce: Union[Unset, AddStandardOrderRequestBodyTimeinforce] = AddStandardOrderRequestBodyTimeinforce.GTC
    starttm: Union[Unset, str] = UNSET
    expiretm: Union[Unset, str] = UNSET
    closeordertype: Union[Unset, AddStandardOrderRequestBodyCloseordertype] = UNSET
    closeprice: Union[Unset, str] = UNSET
    closeprice2: Union[Unset, str] = UNSET
    deadline: Union[Unset, str] = UNSET
    validate: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        ordertype = self.ordertype.value

        type = self.type.value

        pair = self.pair
        userref = self.userref
        volume = self.volume
        price = self.price
        price2 = self.price2
        trigger: Union[Unset, str] = UNSET
        if not isinstance(self.trigger, Unset):
            trigger = self.trigger.value

        leverage = self.leverage
        oflags = self.oflags
        timeinforce: Union[Unset, str] = UNSET
        if not isinstance(self.timeinforce, Unset):
            timeinforce = self.timeinforce.value

        starttm = self.starttm
        expiretm = self.expiretm
        closeordertype: Union[Unset, str] = UNSET
        if not isinstance(self.closeordertype, Unset):
            closeordertype = self.closeordertype.value

        closeprice = self.closeprice
        closeprice2 = self.closeprice2
        deadline = self.deadline
        validate = self.validate

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "ordertype": ordertype,
                "type": type,
                "pair": pair,
            }
        )
        if userref is not UNSET:
            field_dict["userref"] = userref
        if volume is not UNSET:
            field_dict["volume"] = volume
        if price is not UNSET:
            field_dict["price"] = price
        if price2 is not UNSET:
            field_dict["price2"] = price2
        if trigger is not UNSET:
            field_dict["trigger"] = trigger
        if leverage is not UNSET:
            field_dict["leverage"] = leverage
        if oflags is not UNSET:
            field_dict["oflags"] = oflags
        if timeinforce is not UNSET:
            field_dict["timeinforce"] = timeinforce
        if starttm is not UNSET:
            field_dict["starttm"] = starttm
        if expiretm is not UNSET:
            field_dict["expiretm"] = expiretm
        if closeordertype is not UNSET:
            field_dict["close[ordertype]"] = closeordertype
        if closeprice is not UNSET:
            field_dict["close[price]"] = closeprice
        if closeprice2 is not UNSET:
            field_dict["close[price2]"] = closeprice2
        if deadline is not UNSET:
            field_dict["deadline"] = deadline
        if validate is not UNSET:
            field_dict["validate"] = validate

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        ordertype = AddStandardOrderRequestBodyOrdertype(d.pop("ordertype"))

        type = AddStandardOrderRequestBodyType(d.pop("type"))

        pair = d.pop("pair")

        userref = d.pop("userref", UNSET)

        volume = d.pop("volume", UNSET)

        price = d.pop("price", UNSET)

        price2 = d.pop("price2", UNSET)

        _trigger = d.pop("trigger", UNSET)
        trigger: Union[Unset, AddStandardOrderRequestBodyTrigger]
        if isinstance(_trigger, Unset):
            trigger = UNSET
        else:
            trigger = AddStandardOrderRequestBodyTrigger(_trigger)

        leverage = d.pop("leverage", UNSET)

        oflags = d.pop("oflags", UNSET)

        _timeinforce = d.pop("timeinforce", UNSET)
        timeinforce: Union[Unset, AddStandardOrderRequestBodyTimeinforce]
        if isinstance(_timeinforce, Unset):
            timeinforce = UNSET
        else:
            timeinforce = AddStandardOrderRequestBodyTimeinforce(_timeinforce)

        starttm = d.pop("starttm", UNSET)

        expiretm = d.pop("expiretm", UNSET)

        _closeordertype = d.pop("close[ordertype]", UNSET)
        closeordertype: Union[Unset, AddStandardOrderRequestBodyCloseordertype]
        if isinstance(_closeordertype, Unset):
            closeordertype = UNSET
        else:
            closeordertype = AddStandardOrderRequestBodyCloseordertype(_closeordertype)

        closeprice = d.pop("close[price]", UNSET)

        closeprice2 = d.pop("close[price2]", UNSET)

        deadline = d.pop("deadline", UNSET)

        validate = d.pop("validate", UNSET)

        add_standard_order_request_body = cls(
            nonce=nonce,
            ordertype=ordertype,
            type=type,
            pair=pair,
            userref=userref,
            volume=volume,
            price=price,
            price2=price2,
            trigger=trigger,
            leverage=leverage,
            oflags=oflags,
            timeinforce=timeinforce,
            starttm=starttm,
            expiretm=expiretm,
            closeordertype=closeordertype,
            closeprice=closeprice,
            closeprice2=closeprice2,
            deadline=deadline,
            validate=validate,
        )

        add_standard_order_request_body.additional_properties = d
        return add_standard_order_request_body

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