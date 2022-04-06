from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLedgerInfoRequestBody")


@attr.s(auto_attribs=True)
class GetLedgerInfoRequestBody:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        id (Union[Unset, str]): Comma delimited list of ledger IDs to query info about (20 maximum)
        trades (Union[Unset, bool]): Whether or not to include trades related to position in output
    """

    nonce: int
    id: Union[Unset, str] = UNSET
    trades: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        id = self.id
        trades = self.trades

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if trades is not UNSET:
            field_dict["trades"] = trades

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        id = d.pop("id", UNSET)

        trades = d.pop("trades", UNSET)

        get_ledger_info_request_body = cls(
            nonce=nonce,
            id=id,
            trades=trades,
        )

        get_ledger_info_request_body.additional_properties = d
        return get_ledger_info_request_body

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
