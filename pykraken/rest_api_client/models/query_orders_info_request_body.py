from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="QueryOrdersInfoRequestBody")


@attr.s(auto_attribs=True)
class QueryOrdersInfoRequestBody:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        txid (str): Comma delimited list of transaction IDs to query info about (50 maximum)
        trades (Union[Unset, bool]): Whether or not to include trades related to position in output
        userref (Union[Unset, int]): Restrict results to given user reference id
    """

    nonce: int
    txid: str
    trades: Union[Unset, bool] = False
    userref: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        txid = self.txid
        trades = self.trades
        userref = self.userref

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "txid": txid,
            }
        )
        if trades is not UNSET:
            field_dict["trades"] = trades
        if userref is not UNSET:
            field_dict["userref"] = userref

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        txid = d.pop("txid")

        trades = d.pop("trades", UNSET)

        userref = d.pop("userref", UNSET)

        query_orders_info_request_body = cls(
            nonce=nonce,
            txid=txid,
            trades=trades,
            userref=userref,
        )

        query_orders_info_request_body.additional_properties = d
        return query_orders_info_request_body

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