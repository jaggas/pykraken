from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_ledgers_info_request_body_type import GetLedgersInfoRequestBodyType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLedgersInfoRequestBody")


@attr.s(auto_attribs=True)
class GetLedgersInfoRequestBody:
    """
    Attributes:
        nonce (int): Nonce used in construction of `API-Sign` header
        asset (Union[Unset, str]): Comma delimited list of assets to restrict output to Default: 'all'.
        aclass (Union[Unset, str]): Asset class Default: 'currency'.
        type (Union[Unset, GetLedgersInfoRequestBodyType]): Type of ledger to retrieve Default:
            GetLedgersInfoRequestBodyType.ALL.
        start (Union[Unset, int]): Starting unix timestamp or ledger ID of results (exclusive)
        end (Union[Unset, int]): Ending unix timestamp or ledger ID of results (inclusive)
        ofs (Union[Unset, int]): Result offset for pagination
    """

    nonce: int
    asset: Union[Unset, str] = "all"
    aclass: Union[Unset, str] = "currency"
    type: Union[Unset, GetLedgersInfoRequestBodyType] = GetLedgersInfoRequestBodyType.ALL
    start: Union[Unset, int] = UNSET
    end: Union[Unset, int] = UNSET
    ofs: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nonce = self.nonce
        asset = self.asset
        aclass = self.aclass
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

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
        if asset is not UNSET:
            field_dict["asset"] = asset
        if aclass is not UNSET:
            field_dict["aclass"] = aclass
        if type is not UNSET:
            field_dict["type"] = type
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

        asset = d.pop("asset", UNSET)

        aclass = d.pop("aclass", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, GetLedgersInfoRequestBodyType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = GetLedgersInfoRequestBodyType(_type)

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        ofs = d.pop("ofs", UNSET)

        get_ledgers_info_request_body = cls(
            nonce=nonce,
            asset=asset,
            aclass=aclass,
            type=type,
            start=start,
            end=end,
            ofs=ofs,
        )

        get_ledgers_info_request_body.additional_properties = d
        return get_ledgers_info_request_body

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
