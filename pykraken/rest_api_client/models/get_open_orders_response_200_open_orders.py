from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_open_orders_response_200_open_orders_open import GetOpenOrdersResponse200OpenOrdersOpen
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOpenOrdersResponse200OpenOrders")


@attr.s(auto_attribs=True)
class GetOpenOrdersResponse200OpenOrders:
    """Open Orders

    Attributes:
        open_ (Union[Unset, GetOpenOrdersResponse200OpenOrdersOpen]):
    """

    open_: Union[Unset, GetOpenOrdersResponse200OpenOrdersOpen] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        open_: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.open_, Unset):
            open_ = self.open_.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if open_ is not UNSET:
            field_dict["open"] = open_

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _open_ = d.pop("open", UNSET)
        open_: Union[Unset, GetOpenOrdersResponse200OpenOrdersOpen]
        if isinstance(_open_, Unset):
            open_ = UNSET
        else:
            open_ = GetOpenOrdersResponse200OpenOrdersOpen.from_dict(_open_)

        get_open_orders_response_200_open_orders = cls(
            open_=open_,
        )

        get_open_orders_response_200_open_orders.additional_properties = d
        return get_open_orders_response_200_open_orders

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
