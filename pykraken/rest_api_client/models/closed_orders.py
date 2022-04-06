from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.closed_orders_closed import ClosedOrdersClosed
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClosedOrders")


@attr.s(auto_attribs=True)
class ClosedOrders:
    """Closed Orders

    Attributes:
        closed (Union[Unset, ClosedOrdersClosed]):
        count (Union[Unset, int]): Amount of available order info matching criteria
    """

    closed: Union[Unset, ClosedOrdersClosed] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        closed: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.closed, Unset):
            closed = self.closed.to_dict()

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if closed is not UNSET:
            field_dict["closed"] = closed
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _closed = d.pop("closed", UNSET)
        closed: Union[Unset, ClosedOrdersClosed]
        if isinstance(_closed, Unset):
            closed = UNSET
        else:
            closed = ClosedOrdersClosed.from_dict(_closed)

        count = d.pop("count", UNSET)

        closed_orders = cls(
            closed=closed,
            count=count,
        )

        closed_orders.additional_properties = d
        return closed_orders

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
