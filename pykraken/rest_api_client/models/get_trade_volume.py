from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTradeVolume")


@attr.s(auto_attribs=True)
class GetTradeVolume:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        pair (Union[Unset, str]): Comma delimited list of asset pairs to get fee info on (optional)
        fee_info (Union[Unset, bool]): Whether or not to include fee info in results (optional)
    """

    nonce: int
    pair: Union[Unset, str] = UNSET
    fee_info: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        pair = self.pair
        fee_info = self.fee_info

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
            }
        )
        if pair is not UNSET:
            field_dict["pair"] = pair
        if fee_info is not UNSET:
            field_dict["fee-info"] = fee_info

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        pair = d.pop("pair", UNSET)

        fee_info = d.pop("fee-info", UNSET)

        get_trade_volume = cls(
            nonce=nonce,
            pair=pair,
            fee_info=fee_info,
        )

        get_trade_volume.additional_properties = d
        return get_trade_volume

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
