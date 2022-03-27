from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DepositMethod")


@attr.s(auto_attribs=True)
class DepositMethod:
    """Deposit method

    Attributes:
        method (Union[Unset, str]): Name of deposit method
        limit (Union[Unset, Any]): Maximum net amount that can be deposited right now, or false if no limit
        fee (Union[Unset, str]): Amount of fees that will be paid
        address_setup_fee (Union[Unset, str]): Whether or not method has an address setup fee
        gen_address (Union[Unset, bool]): Whether new addresses can be generated for this method.
    """

    method: Union[Unset, str] = UNSET
    limit: Union[Unset, Any] = UNSET
    fee: Union[Unset, str] = UNSET
    address_setup_fee: Union[Unset, str] = UNSET
    gen_address: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method = self.method
        limit = self.limit
        fee = self.fee
        address_setup_fee = self.address_setup_fee
        gen_address = self.gen_address

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if limit is not UNSET:
            field_dict["limit"] = limit
        if fee is not UNSET:
            field_dict["fee"] = fee
        if address_setup_fee is not UNSET:
            field_dict["address-setup-fee"] = address_setup_fee
        if gen_address is not UNSET:
            field_dict["gen-address"] = gen_address

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        method = d.pop("method", UNSET)

        limit = d.pop("limit", UNSET)

        fee = d.pop("fee", UNSET)

        address_setup_fee = d.pop("address-setup-fee", UNSET)

        gen_address = d.pop("gen-address", UNSET)

        deposit_method = cls(
            method=method,
            limit=limit,
            fee=fee,
            address_setup_fee=address_setup_fee,
            gen_address=gen_address,
        )

        deposit_method.additional_properties = d
        return deposit_method

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
