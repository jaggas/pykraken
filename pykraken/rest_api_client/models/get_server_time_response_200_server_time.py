from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetServerTimeResponse200ServerTime")


@attr.s(auto_attribs=True)
class GetServerTimeResponse200ServerTime:
    """
    Attributes:
        unixtime (Union[Unset, int]): Unix timestamp
        rfc1123 (Union[Unset, str]): RFC 1123 time format
    """

    unixtime: Union[Unset, int] = UNSET
    rfc1123: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unixtime = self.unixtime
        rfc1123 = self.rfc1123

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unixtime is not UNSET:
            field_dict["unixtime"] = unixtime
        if rfc1123 is not UNSET:
            field_dict["rfc1123"] = rfc1123

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unixtime = d.pop("unixtime", UNSET)

        rfc1123 = d.pop("rfc1123", UNSET)

        get_server_time_response_200_server_time = cls(
            unixtime=unixtime,
            rfc1123=rfc1123,
        )

        get_server_time_response_200_server_time.additional_properties = d
        return get_server_time_response_200_server_time

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
