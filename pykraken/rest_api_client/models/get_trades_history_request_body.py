from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_trades_history_request_body_type import GetTradesHistoryRequestBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTradesHistoryRequestBody")


@attr.s(auto_attribs=True)
class GetTradesHistoryRequestBody:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        type (Union[Unset, GetTradesHistoryRequestBodyType]): Type of trade Default:
            GetTradesHistoryRequestBodyType.ALL.
        trades (Union[Unset, bool]): Whether or not to include trades related to position in output
        start (Union[Unset, int]): Starting unix timestamp or trade tx ID of results (exclusive)
        end (Union[Unset, int]): Ending unix timestamp or trade tx ID of results (inclusive)
        ofs (Union[Unset, int]): Result offset for pagination
    """

    nonce: int
    type: Union[Unset, GetTradesHistoryRequestBodyType] = GetTradesHistoryRequestBodyType.ALL
    trades: Union[Unset, bool] = False
    start: Union[Unset, int] = UNSET
    end: Union[Unset, int] = UNSET
    ofs: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        trades = self.trades
        start = self.start
        end = self.end
        ofs = self.ofs

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "nonce": nonce,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if trades is not UNSET:
            field_dict["trades"] = trades
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if ofs is not UNSET:
            field_dict["ofs"] = ofs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nonce = d.pop("nonce")

        _type = d.pop("type", UNSET)
        type: Union[Unset, GetTradesHistoryRequestBodyType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GetTradesHistoryRequestBodyType(_type)

        trades = d.pop("trades", UNSET)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        ofs = d.pop("ofs", UNSET)

        get_trades_history_request_body = cls(
            nonce=nonce,
            type=type,
            trades=trades,
            start=start,
            end=end,
            ofs=ofs,
        )

        get_trades_history_request_body.additional_properties = d
        return get_trades_history_request_body

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
