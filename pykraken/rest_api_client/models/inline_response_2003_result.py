from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.asset_pair import AssetPair

T = TypeVar("T", bound="InlineResponse2003Result")


@attr.s(auto_attribs=True)
class InlineResponse2003Result:
    """Pair names and their info"""

    additional_properties: Dict[str, AssetPair] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        inline_response_2003_result = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = AssetPair.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        inline_response_2003_result.additional_properties = additional_properties
        return inline_response_2003_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> AssetPair:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: AssetPair) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
