from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderCancelled")


@attr.s(auto_attribs=True)
class OrderCancelled:
    """
    Attributes:
        count (Union[Unset, int]): Number of orders cancelled.
        pending (Union[Unset, bool]): if set, order(s) is/are pending cancellation
    """

    count: Union[Unset, int] = UNSET
    pending: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        pending = self.pending

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if pending is not UNSET:
            field_dict["pending"] = pending

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        pending = d.pop("pending", UNSET)

        order_cancelled = cls(
            count=count,
            pending=pending,
        )

        order_cancelled.additional_properties = d
        return order_cancelled

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
