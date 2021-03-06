from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.get_server_time_response_200_server_time import GetServerTimeResponse200ServerTime
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetServerTimeResponse200")


@attr.s(auto_attribs=True)
class GetServerTimeResponse200:
    """Success response

    Attributes:
        result (Union[Unset, GetServerTimeResponse200ServerTime]):
        error (Union[Unset, List[str]]):
    """

    result: Union[Unset, GetServerTimeResponse200ServerTime] = UNSET
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
        result: Union[Unset, GetServerTimeResponse200ServerTime]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = GetServerTimeResponse200ServerTime.from_dict(_result)

        error = cast(List[str], d.pop("error", UNSET))

        get_server_time_response_200 = cls(
            result=result,
            error=error,
        )

        get_server_time_response_200.additional_properties = d
        return get_server_time_response_200

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
