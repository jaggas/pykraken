from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetDepositAddressesResponse200DepositAddress")


@attr.s(auto_attribs=True)
class GetDepositAddressesResponse200DepositAddress:
    """Deposit Address

    Attributes:
        address (Union[Unset, str]): Deposit Address
        expiretm (Union[Unset, str]): Expiration time in unix timestamp, or 0 if not expiring
        new (Union[Unset, bool]): Whether or not address has ever been used
    """

    address: Union[Unset, str] = UNSET
    expiretm: Union[Unset, str] = UNSET
    new: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address = self.address
        expiretm = self.expiretm
        new = self.new

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if expiretm is not UNSET:
            field_dict["expiretm"] = expiretm
        if new is not UNSET:
            field_dict["new"] = new

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address = d.pop("address", UNSET)

        expiretm = d.pop("expiretm", UNSET)

        new = d.pop("new", UNSET)

        get_deposit_addresses_response_200_deposit_address = cls(
            address=address,
            expiretm=expiretm,
            new=new,
        )

        get_deposit_addresses_response_200_deposit_address.additional_properties = d
        return get_deposit_addresses_response_200_deposit_address

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
