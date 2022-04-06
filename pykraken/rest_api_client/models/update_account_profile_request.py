from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateAccountProfileRequest")


@attr.s(auto_attribs=True)
class UpdateAccountProfileRequest:
    """Update Account Profile Request Body

    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        asset (Union[Unset, str]): Base asset to determine balance Default: 'ZUSD'.
    """

    nonce: int
    asset: Union[Unset, str] = "ZUSD"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        asset = self.asset

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
            }
        )
        if asset is not UNSET:
            field_dict["asset"] = asset

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        asset = d.pop("asset", UNSET)

        update_account_profile_request = cls(
            nonce=nonce,
            asset=asset,
        )

        update_account_profile_request.additional_properties = d
        return update_account_profile_request

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
