from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.withdrawal_status import WithdrawalStatus
from ..models.withdrawal_status_prop import WithdrawalStatusProp
from ..types import UNSET, Unset

T = TypeVar("T", bound="Withdrawal")


@attr.s(auto_attribs=True)
class Withdrawal:
    """Withdrawal

    Attributes:
        method (Union[Unset, str]): Name of withdrawal method
        aclass (Union[Unset, str]): Asset class
        asset (Union[Unset, str]): Asset
        refid (Union[Unset, str]): Reference ID
        txid (Union[Unset, str]): Method transaction ID
        info (Union[Unset, str]): Method transaction information
        amount (Union[Unset, str]): Amount withdrawn
        fee (Union[Unset, Any]): Fees paid
        time (Union[Unset, int]): Unix timestamp when request was made
        status (Union[Unset, WithdrawalStatus]): Status of withdraw<br>
            <sup><sub>For information about the status, please refer to the [IFEX financial transaction
            states](https://github.com/globalcitizen/ifex-protocol/blob/master/draft-ifex-00.txt#L837).</sup></sub>
        status_prop (Union[Unset, WithdrawalStatusProp]): Addition status properties <sup><sub>(if
            available)</sup></sub><br>
              * `cancel-pending` cancelation requested
              * `canceled` canceled
              * `cancel-denied` cancelation requested but was denied
              * `return` a return transaction initiated by Kraken; it cannot be canceled
              * `onhold` withdrawal is on hold pending review
    """

    method: Union[Unset, str] = UNSET
    aclass: Union[Unset, str] = UNSET
    asset: Union[Unset, str] = UNSET
    refid: Union[Unset, str] = UNSET
    txid: Union[Unset, str] = UNSET
    info: Union[Unset, str] = UNSET
    amount: Union[Unset, str] = UNSET
    fee: Union[Unset, Any] = UNSET
    time: Union[Unset, int] = UNSET
    status: Union[Unset, WithdrawalStatus] = UNSET
    status_prop: Union[Unset, WithdrawalStatusProp] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        method = self.method
        aclass = self.aclass
        asset = self.asset
        refid = self.refid
        txid = self.txid
        info = self.info
        amount = self.amount
        fee = self.fee
        time = self.time
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_prop: Union[Unset, str] = UNSET
        if not isinstance(self.status_prop, Unset):
            status_prop = self.status_prop.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if method is not UNSET:
            field_dict["method"] = method
        if aclass is not UNSET:
            field_dict["aclass"] = aclass
        if asset is not UNSET:
            field_dict["asset"] = asset
        if refid is not UNSET:
            field_dict["refid"] = refid
        if txid is not UNSET:
            field_dict["txid"] = txid
        if info is not UNSET:
            field_dict["info"] = info
        if amount is not UNSET:
            field_dict["amount"] = amount
        if fee is not UNSET:
            field_dict["fee"] = fee
        if time is not UNSET:
            field_dict["time"] = time
        if status is not UNSET:
            field_dict["status"] = status
        if status_prop is not UNSET:
            field_dict["status-prop"] = status_prop

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        method = d.pop("method", UNSET)

        aclass = d.pop("aclass", UNSET)

        asset = d.pop("asset", UNSET)

        refid = d.pop("refid", UNSET)

        txid = d.pop("txid", UNSET)

        info = d.pop("info", UNSET)

        amount = d.pop("amount", UNSET)

        fee = d.pop("fee", UNSET)

        time = d.pop("time", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, WithdrawalStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = WithdrawalStatus(_status)

        _status_prop = d.pop("status-prop", UNSET)
        status_prop: Union[Unset, WithdrawalStatusProp]
        if isinstance(_status_prop, Unset):
            status_prop = UNSET
        else:
            status_prop = WithdrawalStatusProp(_status_prop)

        withdrawal = cls(
            method=method,
            aclass=aclass,
            asset=asset,
            refid=refid,
            txid=txid,
            info=info,
            amount=amount,
            fee=fee,
            time=time,
            status=status,
            status_prop=status_prop,
        )

        withdrawal.additional_properties = d
        return withdrawal

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
