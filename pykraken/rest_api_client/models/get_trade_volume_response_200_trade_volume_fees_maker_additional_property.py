from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_trade_volume_response_200_trade_volume_fees_maker_additional_property_fees import (
    GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFees,
)
from ..models.get_trade_volume_response_200_trade_volume_fees_maker_additional_property_fees_maker import (
    GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFeesMaker,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalProperty")


@attr.s(auto_attribs=True)
class GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalProperty:
    """
    Attributes:
        currency (Union[Unset, str]): Volume currency
        volume (Union[Unset, str]): Current discount volume
        fees (Union[Unset, GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFees]):
        fees_maker (Union[Unset, GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFeesMaker]):
    """

    currency: Union[Unset, str] = UNSET
    volume: Union[Unset, str] = UNSET
    fees: Union[Unset, GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFees] = UNSET
    fees_maker: Union[Unset, GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFeesMaker] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        currency = self.currency
        volume = self.volume
        fees: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fees, Unset):
            fees = self.fees.to_dict()

        fees_maker: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.fees_maker, Unset):
            fees_maker = self.fees_maker.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if currency is not UNSET:
            field_dict["currency"] = currency
        if volume is not UNSET:
            field_dict["volume"] = volume
        if fees is not UNSET:
            field_dict["fees"] = fees
        if fees_maker is not UNSET:
            field_dict["fees_maker"] = fees_maker

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        currency = d.pop("currency", UNSET)

        volume = d.pop("volume", UNSET)

        _fees = d.pop("fees", UNSET)
        fees: Union[Unset, GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFees]
        if isinstance(_fees, Unset):
            fees = UNSET
        else:
            fees = GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFees.from_dict(_fees)

        _fees_maker = d.pop("fees_maker", UNSET)
        fees_maker: Union[Unset, GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFeesMaker]
        if isinstance(_fees_maker, Unset):
            fees_maker = UNSET
        else:
            fees_maker = GetTradeVolumeResponse200TradeVolumeFeesMakerAdditionalPropertyFeesMaker.from_dict(_fees_maker)

        get_trade_volume_response_200_trade_volume_fees_maker_additional_property = cls(
            currency=currency,
            volume=volume,
            fees=fees,
            fees_maker=fees_maker,
        )

        get_trade_volume_response_200_trade_volume_fees_maker_additional_property.additional_properties = d
        return get_trade_volume_response_200_trade_volume_fees_maker_additional_property

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
