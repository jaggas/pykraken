from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.get_trade_balance_response_200_result import GetTradeBalanceResponse200Result
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTradeBalanceResponse200")


@attr.s(auto_attribs=True)
class GetTradeBalanceResponse200:
    """
    Attributes:
        result (Union[Unset, GetTradeBalanceResponse200Result]): Account Balance
        error (Union[Unset, List[str]]):
    """

    result: Union[Unset, GetTradeBalanceResponse200Result] = UNSET
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
        result: Union[Unset, GetTradeBalanceResponse200Result]
        if isinstance(_result, Unset):
            result = UNSET
        else:
            result = GetTradeBalanceResponse200Result.from_dict(_result)

        error = cast(List[str], d.pop("error", UNSET))

        get_trade_balance_response_200 = cls(
            result=result,
            error=error,
        )

        get_trade_balance_response_200.additional_properties = d
        return get_trade_balance_response_200

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
