from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.get_open_orders_response_200_open_orders import GetOpenOrdersResponse200OpenOrders
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetOpenOrdersResponse200")


@attr.s(auto_attribs=True)
class GetOpenOrdersResponse200:
    """
    Example:
        {'error': [], 'result': {'open': {'OQCLML-BW3P3-BUCMWZ': {'refid': None, 'userref': 0, 'status': 'open',
            'opentm': 1616666559.8974, 'starttm': 0, 'expiretm': 0, 'descr': {'pair': 'XBTUSD', 'type': 'buy', 'ordertype':
            'limit', 'price': '30010.0', 'price2': '0', 'leverage': 'none', 'order': 'buy 1.25000000 XBTUSD @ limit
            30010.0', 'close': ''}, 'vol': '1.25000000', 'vol_exec': '0.37500000', 'cost': '11253.7', 'fee': '0.00000',
            'price': '30010.0', 'stopprice': '0.00000', 'limitprice': '0.00000', 'misc': '', 'oflags': 'fciq', 'trades':
            ['TCCCTY-WE2O6-P3NB37']}, 'OB5VMB-B4U2U-DK2WRW': {'refid': None, 'userref': 120, 'status': 'open', 'opentm':
            1616665899.5699, 'starttm': 0, 'expiretm': 0, 'descr': {'pair': 'XBTUSD', 'type': 'buy', 'ordertype': 'limit',
            'price': '14500.0', 'price2': '0', 'leverage': '5:1', 'order': 'buy 0.27500000 XBTUSD @ limit 14500.0 with 5:1
            leverage', 'close': ''}, 'vol': '0.27500000', 'vol_exec': '0.00000000', 'cost': '0.00000', 'fee': '0.00000',
            'price': '0.00000', 'stopprice': '0.00000', 'limitprice': '0.00000', 'misc': '', 'oflags': 'fciq'},
            'OXHXGL-F5ICS-6DIC67': {'refid': None, 'userref': 120, 'status': 'open', 'opentm': 1616665894.0036, 'starttm':
            0, 'expiretm': 0, 'descr': {'pair': 'XBTUSD', 'type': 'buy', 'ordertype': 'limit', 'price': '17500.0', 'price2':
            '0', 'leverage': '5:1', 'order': 'buy 0.27500000 XBTUSD @ limit 17500.0 with 5:1 leverage', 'close': ''}, 'vol':
            '0.27500000', 'vol_exec': '0.00000000', 'cost': '0.00000', 'fee': '0.00000', 'price': '0.00000', 'stopprice':
            '0.00000', 'limitprice': '0.00000', 'misc': '', 'oflags': 'fciq'}, 'OLQCVY-B27XU-MBPCL5': {'refid': None,
            'userref': 251, 'status': 'open', 'opentm': 1616665556.7646, 'starttm': 0, 'expiretm': 0, 'descr': {'pair':
            'XBTUSD', 'type': 'buy', 'ordertype': 'limit', 'price': '23500.0', 'price2': '0', 'leverage': 'none', 'order':
            'buy 0.27500000 XBTUSD @ limit 23500.0', 'close': ''}, 'vol': '0.27500000', 'vol_exec': '0.00000000', 'cost':
            '0.00000', 'fee': '0.00000', 'price': '0.00000', 'stopprice': '0.00000', 'limitprice': '0.00000', 'misc': '',
            'oflags': 'fciq'}, 'OQCGAF-YRMIQ-AMJTNJ': {'refid': None, 'userref': 0, 'status': 'open', 'opentm':
            1616665511.0373, 'starttm': 0, 'expiretm': 0, 'descr': {'pair': 'XBTUSD', 'type': 'buy', 'ordertype': 'stop-
            loss-limit', 'price': '24500.0', 'price2': '0', 'leverage': 'none', 'order': 'buy 1.25000000 XBTUSD @ limit
            24500.0', 'close': ''}, 'vol': '1.25000000', 'vol_exec': '0.00000000', 'cost': '0.00000', 'fee': '0.00000',
            'price': '0.00000', 'stopprice': '0.00000', 'limitprice': '0.00000', 'misc': '', 'oflags': 'fciq', 'trigger':
            'index'}}}}

    Attributes:
        result (Union[Unset, GetOpenOrdersResponse200OpenOrders]): Open Orders
        error (Union[Unset, List[str]]):
    """

    result: Union[Unset, GetOpenOrdersResponse200OpenOrders] = UNSET
    error: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.result, Unset):
            result = self.result.to_dict()

        error: Union[Unset, List[str]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _result = d.pop("result", UNSET)
        result: Union[Unset, GetOpenOrdersResponse200OpenOrders]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = GetOpenOrdersResponse200OpenOrders.from_dict(_result)

        error = cast(List[str], d.pop("error", UNSET))

        get_open_orders_response_200 = cls(
            result=result,
            error=error,
        )

        get_open_orders_response_200.additional_properties = d
        return get_open_orders_response_200

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
