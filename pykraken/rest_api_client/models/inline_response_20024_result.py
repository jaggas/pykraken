from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InlineResponse20024Result")


@attr.s(auto_attribs=True)
class InlineResponse20024Result:
    """
    Attributes:
        delete (Union[Unset, bool]): Whether deletion was successful
        cancel (Union[Unset, bool]): Whether cancellation was successful
    """

    delete: Union[Unset, bool] = UNSET
    cancel: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delete = self.delete
        cancel = self.cancel

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if delete is not UNSET:
            field_dict["delete"] = delete
        if cancel is not UNSET:
            field_dict["cancel"] = cancel

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        delete = d.pop("delete", UNSET)

        cancel = d.pop("cancel", UNSET)

        inline_response_20024_result = cls(
            delete=delete,
            cancel=cancel,
        )

        inline_response_20024_result.additional_properties = d
        return inline_response_20024_result

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
