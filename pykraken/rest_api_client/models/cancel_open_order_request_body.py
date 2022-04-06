from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

T = TypeVar("T", bound="CancelOpenOrderRequestBody")


@attr.s(auto_attribs=True)
class CancelOpenOrderRequestBody:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        txid (Union[int, str]): Open order transaction ID (txid) or user reference (userref)
    """

    nonce: int
    txid: Union[int, str]
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce

        txid = self.txid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
                "txid": txid,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        def _parse_txid(data: object) -> Union[int, str]:
            return cast(Union[int, str], data)

        txid = _parse_txid(d.pop("txid"))

        cancel_open_order_request_body = cls(
            nonce=nonce,
            txid=txid,
        )

        cancel_open_order_request_body.additional_properties = d
        return cancel_open_order_request_body

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
