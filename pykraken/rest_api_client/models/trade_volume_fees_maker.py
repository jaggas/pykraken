from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.trade_volume_fees_maker_additional_property import TradeVolumeFeesMakerAdditionalProperty

T = TypeVar("T", bound="TradeVolumeFeesMaker")


@attr.s(auto_attribs=True)
class TradeVolumeFeesMaker:
    """ """

    additional_properties: Dict[str, TradeVolumeFeesMakerAdditionalProperty] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        trade_volume_fees_maker = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = TradeVolumeFeesMakerAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        trade_volume_fees_maker.additional_properties = additional_properties
        return trade_volume_fees_maker

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> TradeVolumeFeesMakerAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: TradeVolumeFeesMakerAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
