from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.get_trade_volume_response_200_trade_volume_fees_maker_additional_property_fees_maker_additional_property import (
    GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFeesMakerAdditionalProperty,
)

T = TypeVar("T", bound="GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFeesMaker")


@attr.s(auto_attribs=True)
class GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFeesMaker:
    """ """

    additional_properties: Dict[
        str, GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFeesMakerAdditionalProperty
    ] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_trade_volume_response_200_trade_volume_fees_maker_additional_property_fees_maker = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFeesMakerAdditionalProperty.from_dict(
                    prop_dict
                )
            )

            additional_properties[prop_name] = additional_property

        get_trade_volume_response_200_trade_volume_fees_maker_additional_property_fees_maker.additional_properties = (
            additional_properties
        )
        return get_trade_volume_response_200_trade_volume_fees_maker_additional_property_fees_maker

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFeesMakerAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self,
        key: str,
        value: GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFeesMakerAdditionalProperty,
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
