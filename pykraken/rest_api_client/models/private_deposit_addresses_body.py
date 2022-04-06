from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrivateDepositAddressesBody")


@attr.s(auto_attribs=True)
class PrivateDepositAddressesBody:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        asset (str): Asset being deposited
        method (str): Name of the deposit method
        new (Union[Unset, bool]): Whether or not to generate a new address
    """

    nonce: int
    asset: str
    method: str
    new: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        asset = self.asset
        method = self.method
        new = self.new

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "asset": asset,
                "method": method,
            }
        )
        if new is not UNSET:
            field_dict["new"] = new

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        asset = d.pop("asset")

        method = d.pop("method")

        new = d.pop("new", UNSET)

        private_deposit_addresses_body = cls(
            nonce=nonce,
            asset=asset,
            method=method,
            new=new,
        )

        private_deposit_addresses_body.additional_properties = d
        return private_deposit_addresses_body

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
