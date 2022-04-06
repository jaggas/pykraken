from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_orders_info_response_200_result_open_order_descr_ordertype import (
    GetOrdersInfoResponse200ResultOpenOrderDescrOrdertype,
)
from ..models.get_orders_info_response_200_result_open_order_descr_type import (
    GetOrdersInfoResponse200ResultOpenOrderDescrType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOrdersInfoResponse200ResultOpenOrderDescr")


@attr.s(auto_attribs=True)
class GetOrdersInfoResponse200ResultOpenOrderDescr:
    """Order description info

    Attributes:
        pair (Union[Unset, str]): Asset pair
        type (Union[Unset, GetOrdersInfoResponse200ResultOpenOrderDescrType]): Order side
              * buy - buy side
              * sell - sell side
        ordertype (Union[Unset, GetOrdersInfoResponse200ResultOpenOrderDescrOrdertype]):
        price (Union[Unset, str]): primary price
        price2 (Union[Unset, str]): Secondary price
        leverage (Union[Unset, str]): Amount of leverage
        order (Union[Unset, str]): Order description
        close (Union[Unset, str]): Conditional close order description (if conditional close set)
    """

    pair: Union[Unset, str] = UNSET
    type: Union[Unset, GetOrdersInfoResponse200ResultOpenOrderDescrType] = UNSET
    ordertype: Union[Unset, GetOrdersInfoResponse200ResultOpenOrderDescrOrdertype] = UNSET
    price: Union[Unset, str] = UNSET
    price2: Union[Unset, str] = UNSET
    leverage: Union[Unset, str] = UNSET
    order: Union[Unset, str] = UNSET
    close: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        pair = self.pair
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        ordertype: Union[Unset, str] = UNSET
        if not isinstance(self.ordertype, Unset):
            ordertype = self.ordertype.value

        price = self.price
        price2 = self.price2
        leverage = self.leverage
        order = self.order
        close = self.close

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pair is not UNSET:
            field_dict["pair"] = pair
        if type is not UNSET:
            field_dict["type"] = type
        if ordertype is not UNSET:
            field_dict["ordertype"] = ordertype
        if price is not UNSET:
            field_dict["price"] = price
        if price2 is not UNSET:
            field_dict["price2"] = price2
        if leverage is not UNSET:
            field_dict["leverage"] = leverage
        if order is not UNSET:
            field_dict["order"] = order
        if close is not UNSET:
            field_dict["close"] = close

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        pair = d.pop("pair", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, GetOrdersInfoResponse200ResultOpenOrderDescrType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GetOrdersInfoResponse200ResultOpenOrderDescrType(_type)

        _ordertype = d.pop("ordertype", UNSET)
        ordertype: Union[Unset, GetOrdersInfoResponse200ResultOpenOrderDescrOrdertype]
        if isinstance(_ordertype, Unset):
            ordertype = UNSET
        else:
            ordertype = GetOrdersInfoResponse200ResultOpenOrderDescrOrdertype(_ordertype)

        price = d.pop("price", UNSET)

        price2 = d.pop("price2", UNSET)

        leverage = d.pop("leverage", UNSET)

        order = d.pop("order", UNSET)

        close = d.pop("close", UNSET)

        get_orders_info_response_200_result_open_order_descr = cls(
            pair=pair,
            type=type,
            ordertype=ordertype,
            price=price,
            price2=price2,
            leverage=leverage,
            order=order,
            close=close,
        )

        get_orders_info_response_200_result_open_order_descr.additional_properties = d
        return get_orders_info_response_200_result_open_order_descr

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
