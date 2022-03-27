from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.staking_transaction_info_status import StakingTransactionInfoStatus
from ..models.staking_transaction_info_type import StakingTransactionInfoType
from ..types import UNSET, Unset

T = TypeVar("T", bound="StakingTransactionInfo")


@attr.s(auto_attribs=True)
class StakingTransactionInfo:
    """
    Attributes:
        refid (Union[Unset, str]): The reference ID of the transaction.
        type (Union[Unset, StakingTransactionInfoType]): The type of transaction.
        asset (Union[Unset, str]): Asset code/name
        amount (Union[Unset, str]): The transaction amount
        time (Union[Unset, str]): Unix timestamp when the transaction was initiated.
        bond_start (Union[Unset, int]): Unix timestamp from the start of bond period (applicable only to `bonding`
            transactions).
        bond_end (Union[Unset, int]): Unix timestamp of the end of bond period (applicable only to `bonding`
            transactions).
        status (Union[Unset, StakingTransactionInfoStatus]): Transaction status
    """

    refid: Union[Unset, str] = UNSET
    type: Union[Unset, StakingTransactionInfoType] = UNSET
    asset: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    time: Union[Unset, str] = UNSET
    bond_start: Union[Unset, int] = UNSET
    bond_end: Union[Unset, int] = UNSET
    status: Union[Unset, StakingTransactionInfoStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        refid = self.refid
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        asset = self.asset
        amount = self.amount
        time = self.time
        bond_start = self.bond_start
        bond_end = self.bond_end
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if refid is not UNSET:
            field_dict["refid"] = refid
        if type is not UNSET:
            field_dict["type"] = type
        if asset is not UNSET:
            field_dict["asset"] = asset
        if amount is not UNSET:
            field_dict["amount"] = amount
        if time is not UNSET:
            field_dict["time"] = time
        if bond_start is not UNSET:
            field_dict["bond_start"] = bond_start
        if bond_end is not UNSET:
            field_dict["bond_end"] = bond_end
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        refid = d.pop("refid", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, StakingTransactionInfoType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = StakingTransactionInfoType(_type)

        asset = d.pop("asset", UNSET)

        amount = d.pop("amount", UNSET)

        time = d.pop("time", UNSET)

        bond_start = d.pop("bond_start", UNSET)

        bond_end = d.pop("bond_end", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, StakingTransactionInfoStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StakingTransactionInfoStatus(_status)

        staking_transaction_info = cls(
            refid=refid,
            type=type,
            asset=asset,
            amount=amount,
            time=time,
            bond_start=bond_start,
            bond_end=bond_end,
            status=status,
        )

        staking_transaction_info.additional_properties = d
        return staking_transaction_info

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
