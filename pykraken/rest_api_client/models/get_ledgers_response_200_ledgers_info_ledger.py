from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.get_ledgers_response_200_ledgers_info_ledger_additional_property import (
    GetLedgersResponse200LedgersInfoLedgerAdditionalProperty,
)

T = TypeVar("T", bound="GetLedgersResponse200LedgersInfoLedger")


@attr.s(auto_attribs=True)
class GetLedgersResponse200LedgersInfoLedger:
    """ """

    additional_properties: Dict[str, GetLedgersResponse200LedgersInfoLedgerAdditionalProperty] = attr.ib(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_ledgers_response_200_ledgers_info_ledger = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = GetLedgersResponse200LedgersInfoLedgerAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        get_ledgers_response_200_ledgers_info_ledger.additional_properties = additional_properties
        return get_ledgers_response_200_ledgers_info_ledger

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> GetLedgersResponse200LedgersInfoLedgerAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: GetLedgersResponse200LedgersInfoLedgerAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
