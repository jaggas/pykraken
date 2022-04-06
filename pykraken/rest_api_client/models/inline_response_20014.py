from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.inline_response_20014_result import InlineResponse20014Result
from ..types import UNSET, Unset

T = TypeVar("T", bound="InlineResponse20014")


@attr.s(auto_attribs=True)
class InlineResponse20014:
    """
    Attributes:
        result (Union[Unset, InlineResponse20014Result]):
        error (Union[Unset, List[str]]):
    """

    result: Union[Unset, InlineResponse20014Result] = UNSET
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
        result: Union[Unset, InlineResponse20014Result]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = InlineResponse20014Result.from_dict(_result)

        error = cast(List[str], d.pop("error", UNSET))

        inline_response_20014 = cls(
            result=result,
            error=error,
        )

        inline_response_20014.additional_properties = d
        return inline_response_20014

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
