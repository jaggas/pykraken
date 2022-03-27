from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.get_status_recent_deposits_response_200_deposit import GetStatusRecentDepositsResponse200Deposit
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetStatusRecentDepositsResponse200")


@attr.s(auto_attribs=True)
class GetStatusRecentDepositsResponse200:
    """
    Example:
        {'error': [], 'result': [{'method': 'Bitcoin', 'aclass': 'currency', 'asset': 'XXBT', 'refid': 'QGBCOYA-
            UNP53O-F2JDNS', 'txid': '6544b41b607d8b2512baf801755a3a87b6890eacdb451be8a94059fb11f0a8d9', 'info':
            '2Myd4eaAW96ojk38A2uDK4FbioCayvkEgVq', 'amount': '0.78125000', 'fee': '0.0000000000', 'time': 1546992722,
            'status': 'Success'}, {'method': 'Bitcoin', 'aclass': 'currency', 'asset': 'XXBT', 'refid':
            'QGBHU3O-73ARA5-IFCFZT', 'txid': 'fe12122222fe7fb1bc756a10ecd25f93015e959810ff1daf56535b9b01a803af', 'info':
            '2Myd4eaAW96ojk38A2uDK4FbioCayvkEgVq', 'amount': '0.78125000', 'time': 1546992722, 'status': 'Settled'}]}

    Attributes:
        result (Union[Unset, List[GetStatusRecentDepositsResponse200Deposit]]):
        error (Union[Unset, List[str]]):
    """

    result: Union[Unset, List[GetStatusRecentDepositsResponse200Deposit]] = UNSET
    error: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.result, Unset):
            result = []
            for result_item_data in self.result:
                result_item = result_item_data.to_dict()

                result.append(result_item)

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
        result = []
        _result = d.pop("result", UNSET)
        for result_item_data in _result or []:
            result_item = GetStatusRecentDepositsResponse200Deposit.from_dict(result_item_data)

            result.append(result_item)

        error = cast(List[str], d.pop("error", UNSET))

        get_status_recent_deposits_response_200 = cls(
            result=result,
            error=error,
        )

        get_status_recent_deposits_response_200.additional_properties = d
        return get_status_recent_deposits_response_200

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
