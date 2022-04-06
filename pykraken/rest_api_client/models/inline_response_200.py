from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.server_time import ServerTime
from ..types import UNSET, Unset

T = TypeVar("T", bound="InlineResponse200")


@attr.s(auto_attribs=True)
class InlineResponse200:
    """Success response

    Attributes:
        result (Union[Unset, ServerTime]):
        error (Union[Unset, List[str]]):
    """

    result: Union[Unset, ServerTime] = UNSET
    error: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        error: Union[Unset, List[str]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, ServerTime]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = ServerTime.from_dict(_result)

        error = cast(List[str], d.pop("error", UNSET))

        inline_response_200 = cls(
            result=result,
            error=error,
        )

        inline_response_200.additional_properties = d
        return inline_response_200

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