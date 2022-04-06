from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InlineResponse20028Result")


@attr.s(auto_attribs=True)
class InlineResponse20028Result:
    """
    Attributes:
        current_time (Union[Unset, str]): Timestamp (RFC3339 format) at which the request was received
        trigger_time (Union[Unset, str]): Timestamp (RFC3339 format) after which all orders will be cancelled, unless
            the timer is extended or disabled
    """

    current_time: Union[Unset, str] = UNSET
    trigger_time: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        current_time = self.current_time
        trigger_time = self.trigger_time

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_time is not UNSET:
            field_dict["currentTime"] = current_time
        if trigger_time is not UNSET:
            field_dict["triggerTime"] = trigger_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        current_time = d.pop("currentTime", UNSET)

        trigger_time = d.pop("triggerTime", UNSET)

        inline_response_20028_result = cls(
            current_time=current_time,
            trigger_time=trigger_time,
        )

        inline_response_20028_result.additional_properties = d
        return inline_response_20028_result

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
