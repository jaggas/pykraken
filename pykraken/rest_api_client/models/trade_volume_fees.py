from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.fee_tier_info import FeeTierInfo

T = TypeVar("T", bound="TradeVolumeFees")


@attr.s(auto_attribs=True)
class TradeVolumeFees:
    """ """

    additional_properties: Dict[str, FeeTierInfo] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trade_volume_fees = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = FeeTierInfo.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        trade_volume_fees.additional_properties = additional_properties
        return trade_volume_fees

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> FeeTierInfo:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: FeeTierInfo) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties