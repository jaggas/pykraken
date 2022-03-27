from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrderBook")


@attr.s(auto_attribs=True)
class OrderBook:
    """Asset Pair Order Book Entries

    Attributes:
        asks (Union[Unset, List[Union[int, str]]]): Ask side array of entries `[<price>, <volume>, <timestamp>]`
        bid (Union[Unset, List[Union[int, str]]]): Bid side array of entries `[<price>, <volume>, <timestamp>]`
    """

    asks: Union[Unset, List[Union[int, str]]] = UNSET
    bid: Union[Unset, List[Union[int, str]]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asks: Union[Unset, List[Union[int, str]]] = UNSET
        if not isinstance(self.asks, Unset):
            asks = []
            for asks_item_data in self.asks:

                asks_item = asks_item_data

                asks.append(asks_item)

        bid: Union[Unset, List[Union[int, str]]] = UNSET
        if not isinstance(self.bid, Unset):
            bid = []
            for bid_item_data in self.bid:

                bid_item = bid_item_data

                bid.append(bid_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if asks is not UNSET:
            field_dict["asks"] = asks
        if bid is not UNSET:
            field_dict["bid"] = bid

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asks = []
        _asks = d.pop("asks", UNSET)
        for asks_item_data in _asks or []:

            def _parse_asks_item(data: object) -> Union[int, str]:
                return cast(Union[int, str], data)

            asks_item = _parse_asks_item(asks_item_data)

            asks.append(asks_item)

        bid = []
        _bid = d.pop("bid", UNSET)
        for bid_item_data in _bid or []:

            def _parse_bid_item(data: object) -> Union[int, str]:
                return cast(Union[int, str], data)

            bid_item = _parse_bid_item(bid_item_data)

            bid.append(bid_item)

        order_book = cls(
            asks=asks,
            bid=bid,
        )

        order_book.additional_properties = d
        return order_book

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
