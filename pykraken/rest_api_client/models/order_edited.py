from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.order_edited_descr import OrderEditedDescr
from ..models.order_edited_status import OrderEditedStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderEdited")


@attr.s(auto_attribs=True)
class OrderEdited:
    """New order response

    Attributes:
        descr (Union[Unset, OrderEditedDescr]): Order description info
        txid (Union[Unset, List[str]]): New transaction ID
        newuserref (Union[Unset, str]): New userref if passed with the request
        olduserref (Union[Unset, str]): Original userref if passed with the request
        orders_cancelled (Union[Unset, int]): Number of orders cancelled
        originaltxid (Union[Unset, str]): Original transaction ID
        status (Union[Unset, OrderEditedStatus]): Status of the order (Ok or Err)
        volume (Union[Unset, str]): Updated volume
        price (Union[Unset, str]): Updated price
        price2 (Union[Unset, str]): Updated price2
        error_message (Union[Unset, str]): Error message if unsuccessful
    """

    descr: Union[Unset, OrderEditedDescr] = UNSET
    txid: Union[Unset, List[str]] = UNSET
    newuserref: Union[Unset, str] = UNSET
    olduserref: Union[Unset, str] = UNSET
    orders_cancelled: Union[Unset, int] = UNSET
    originaltxid: Union[Unset, str] = UNSET
    status: Union[Unset, OrderEditedStatus] = UNSET
    volume: Union[Unset, str] = UNSET
    price: Union[Unset, str] = UNSET
    price2: Union[Unset, str] = UNSET
    error_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        descr: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.descr, Unset):
            descr = self.descr.to_dict()

        txid: Union[Unset, List[str]] = UNSET
        if not isinstance(self.txid, Unset):
            txid = self.txid

        newuserref = self.newuserref
        olduserref = self.olduserref
        orders_cancelled = self.orders_cancelled
        originaltxid = self.originaltxid
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        volume = self.volume
        price = self.price
        price2 = self.price2
        error_message = self.error_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if descr is not UNSET:
            field_dict["descr"] = descr
        if txid is not UNSET:
            field_dict["txid"] = txid
        if newuserref is not UNSET:
            field_dict["newuserref"] = newuserref
        if olduserref is not UNSET:
            field_dict["olduserref"] = olduserref
        if orders_cancelled is not UNSET:
            field_dict["orders_cancelled"] = orders_cancelled
        if originaltxid is not UNSET:
            field_dict["originaltxid"] = originaltxid
        if status is not UNSET:
            field_dict["status"] = status
        if volume is not UNSET:
            field_dict["volume"] = volume
        if price is not UNSET:
            field_dict["price"] = price
        if price2 is not UNSET:
            field_dict["price2"] = price2
        if error_message is not UNSET:
            field_dict["error_message"] = error_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _descr = d.pop("descr", UNSET)
        descr: Union[Unset, OrderEditedDescr]
        if isinstance(_descr, Unset):
            descr = UNSET
        else:
            descr = OrderEditedDescr.from_dict(_descr)

        txid = cast(List[str], d.pop("txid", UNSET))

        newuserref = d.pop("newuserref", UNSET)

        olduserref = d.pop("olduserref", UNSET)

        orders_cancelled = d.pop("orders_cancelled", UNSET)

        originaltxid = d.pop("originaltxid", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, OrderEditedStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = OrderEditedStatus(_status)

        volume = d.pop("volume", UNSET)

        price = d.pop("price", UNSET)

        price2 = d.pop("price2", UNSET)

        error_message = d.pop("error_message", UNSET)

        order_edited = cls(
            descr=descr,
            txid=txid,
            newuserref=newuserref,
            olduserref=olduserref,
            orders_cancelled=orders_cancelled,
            originaltxid=originaltxid,
            status=status,
            volume=volume,
            price=price,
            price2=price2,
            error_message=error_message,
        )

        order_edited.additional_properties = d
        return order_edited

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
