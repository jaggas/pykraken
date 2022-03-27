from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.add_order_response_200_order_added_descr import AddOrderResponse200OrderAddedDescr
from ..types import UNSET, Unset

T = TypeVar("T", bound="AddOrderResponse200OrderAdded")


@attr.s(auto_attribs=True)
class AddOrderResponse200OrderAdded:
    """
    Attributes:
        descr (Union[Unset, AddOrderResponse200OrderAddedDescr]): Order description info
        txid (Union[Unset, List[str]]): Transaction IDs for order
            <br><sup><sub>(if order was added successfully)</sup></sub>
    """

    descr: Union[Unset, AddOrderResponse200OrderAddedDescr] = UNSET
    txid: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        descr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descr, Unset):
            descr = self.descr.to_dict()

        txid: Union[Unset, List[str]] = UNSET
        if not isinstance(self.txid, Unset):
            txid = self.txid

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if descr is not UNSET:
            field_dict["descr"] = descr
        if txid is not UNSET:
            field_dict["txid"] = txid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _descr = d.pop("descr", UNSET)
        descr: Union[Unset, AddOrderResponse200OrderAddedDescr]
        if isinstance(_descr, Unset):
            descr = UNSET
        else:
            descr = AddOrderResponse200OrderAddedDescr.from_dict(_descr)

        txid = cast(List[str], d.pop("txid", UNSET))

        add_order_response_200_order_added = cls(
            descr=descr,
            txid=txid,
        )

        add_order_response_200_order_added.additional_properties = d
        return add_order_response_200_order_added

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
