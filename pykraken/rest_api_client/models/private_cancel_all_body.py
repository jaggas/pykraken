from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PrivateCancelAllBody")


@attr.s(auto_attribs=True)
class PrivateCancelAllBody:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
    """

    nonce: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        private_cancel_all_body = cls(
            nonce=nonce,
        )

        private_cancel_all_body.additional_properties = d
        return private_cancel_all_body

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