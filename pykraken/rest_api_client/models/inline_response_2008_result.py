from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="InlineResponse2008Result")


@attr.s(auto_attribs=True)
class InlineResponse2008Result:
    """
    Attributes:
        last (Union[Unset, int]): ID to be used as since when polling for new spread data
    """

    last: Union[Unset, int] = UNSET
    additional_properties: Dict[str, List[Union[int, str]]] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last = self.last

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = []
            for additional_property_item_data in prop:

                additional_property_item = additional_property_item_data

                field_dict[prop_name].append(additional_property_item)

        field_dict.update({})
        if last is not UNSET:
            field_dict["last"] = last

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        last = d.pop("last", UNSET)

        inline_response_2008_result = cls(
            last=last,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = []
            _additional_property = prop_dict
            for additional_property_item_data in _additional_property:

                def _parse_additional_property_item(data: object) -> Union[int, str]:
                    return cast(Union[int, str], data)

                additional_property_item = _parse_additional_property_item(additional_property_item_data)

                additional_property.append(additional_property_item)

            additional_properties[prop_name] = additional_property

        inline_response_2008_result.additional_properties = additional_properties
        return inline_response_2008_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> List[Union[int, str]]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: List[Union[int, str]]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
