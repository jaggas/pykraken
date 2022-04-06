from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PrivateWithdrawBody")


@attr.s(auto_attribs=True)
class PrivateWithdrawBody:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        asset (str): Asset being withdrawn
        key (str): Withdrawal key name, as set up on your account
        amount (str): Amount to be withdrawn
    """

    nonce: int
    asset: str
    key: str
    amount: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        asset = self.asset
        key = self.key
        amount = self.amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "asset": asset,
                "key": key,
                "amount": amount,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        asset = d.pop("asset")

        key = d.pop("key")

        amount = d.pop("amount")

        private_withdraw_body = cls(
            nonce=nonce,
            asset=asset,
            key=key,
            amount=amount,
        )

        private_withdraw_body.additional_properties = d
        return private_withdraw_body

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
