from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_ledgers_response_200_ledgers_info_ledger import GetLedgersResponse200LedgersInfoLedger
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetLedgersResponse200LedgersInfo")


@attr.s(auto_attribs=True)
class GetLedgersResponse200LedgersInfo:
    """Ledgers Info

    Attributes:
        ledger (Union[Unset, GetLedgersResponse200LedgersInfoLedger]):
        count (Union[Unset, int]): Amount of available ledger info matching criteria
    """

    ledger: Union[Unset, GetLedgersResponse200LedgersInfoLedger] = UNSET
    count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        ledger: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ledger, Unset):
            ledger = self.ledger.to_dict()

        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if ledger is not UNSET:
            field_dict["ledger"] = ledger
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _ledger = d.pop("ledger", UNSET)
        ledger: Union[Unset, GetLedgersResponse200LedgersInfoLedger]
        if isinstance(_ledger, Unset):
            ledger = UNSET
        else:
            ledger = GetLedgersResponse200LedgersInfoLedger.from_dict(_ledger)

        count = d.pop("count", UNSET)

        get_ledgers_response_200_ledgers_info = cls(
            ledger=ledger,
            count=count,
        )

        get_ledgers_response_200_ledgers_info.additional_properties = d
        return get_ledgers_response_200_ledgers_info

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
