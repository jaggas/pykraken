from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.get_ledgers_info_response_200_result_ledger_entry import GetLedgersInfoResponse200ResultLedgerEntry

T = TypeVar("T", bound="GetLedgersInfoResponse200Result")


@attr.s(auto_attribs=True)
class GetLedgersInfoResponse200Result:
    """ """

    additional_properties: Dict[str, GetLedgersInfoResponse200ResultLedgerEntry] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_ledgers_info_response_200_result = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GetLedgersInfoResponse200ResultLedgerEntry.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_ledgers_info_response_200_result.additional_properties = additional_properties
        return get_ledgers_info_response_200_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GetLedgersInfoResponse200ResultLedgerEntry:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: GetLedgersInfoResponse200ResultLedgerEntry) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
