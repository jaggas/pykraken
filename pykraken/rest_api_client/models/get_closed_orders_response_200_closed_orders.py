from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_closed_orders_response_200_closed_orders_closed import GetClosedOrdersResponse200ClosedOrdersClosed
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetClosedOrdersResponse200ClosedOrders")


@attr.s(auto_attribs=True)
class GetClosedOrdersResponse200ClosedOrders:
    """Closed Orders

    Attributes:
        closed (Union[Unset, GetClosedOrdersResponse200ClosedOrdersClosed]):
        count (Union[Unset, int]): Amount of available order info matching criteria
    """

    closed: Union[Unset, GetClosedOrdersResponse200ClosedOrdersClosed] = UNSET
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
        closed: Union[Unset, GetClosedOrdersResponse200ClosedOrdersClosed]
        if isinstance(_closed, Unset):
            closed = UNSET
        else:
            closed = GetClosedOrdersResponse200ClosedOrdersClosed.from_dict(_closed)

        count = d.pop("count", UNSET)

        get_closed_orders_response_200_closed_orders = cls(
            closed=closed,
            count=count,
        )

        get_closed_orders_response_200_closed_orders.additional_properties = d
        return get_closed_orders_response_200_closed_orders

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
