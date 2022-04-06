from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTradeBalanceResponse200Result")


@attr.s(auto_attribs=True)
class GetTradeBalanceResponse200Result:
    """Account Balance

    Attributes:
        eb (Union[Unset, str]): Equivalent balance (combined balance of all currencies)
        tb (Union[Unset, str]): Trade balance (combined balance of all equity currencies)
        m (Union[Unset, str]): Margin amount of open positions
        n (Union[Unset, str]): Unrealized net profit/loss of open positions
        c (Union[Unset, str]): Cost basis of open positions
        v (Union[Unset, str]): Current floating valuation of open positions
        e (Union[Unset, str]): Equity: `trade balance + unrealized net profit/loss`
        mf (Union[Unset, str]): Free margin: `Equity - initial margin (maximum margin available to open new positions)`
        ml (Union[Unset, str]): Margin level: `(equity / initial margin) * 100`
    """

    eb: Union[Unset, str] = UNSET
    tb: Union[Unset, str] = UNSET
    m: Union[Unset, str] = UNSET
    n: Union[Unset, str] = UNSET
    c: Union[Unset, str] = UNSET
    v: Union[Unset, str] = UNSET
    e: Union[Unset, str] = UNSET
    mf: Union[Unset, str] = UNSET
    ml: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        eb = self.eb
        tb = self.tb
        m = self.m
        n = self.n
        c = self.c
        v = self.v
        e = self.e
        mf = self.mf
        ml = self.ml

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if eb is not UNSET:
            field_dict["eb"] = eb
        if tb is not UNSET:
            field_dict["tb"] = tb
        if m is not UNSET:
            field_dict["m"] = m
        if n is not UNSET:
            field_dict["n"] = n
        if c is not UNSET:
            field_dict["c"] = c
        if v is not UNSET:
            field_dict["v"] = v
        if e is not UNSET:
            field_dict["e"] = e
        if mf is not UNSET:
            field_dict["mf"] = mf
        if ml is not UNSET:
            field_dict["ml"] = ml

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        eb = d.pop("eb", UNSET)

        tb = d.pop("tb", UNSET)

        m = d.pop("m", UNSET)

        n = d.pop("n", UNSET)

        c = d.pop("c", UNSET)

        v = d.pop("v", UNSET)

        e = d.pop("e", UNSET)

        mf = d.pop("mf", UNSET)

        ml = d.pop("ml", UNSET)

        get_trade_balance_response_200_result = cls(
            eb=eb,
            tb=tb,
            m=m,
            n=n,
            c=c,
            v=v,
            e=e,
            mf=mf,
            ml=ml,
        )

        get_trade_balance_response_200_result.additional_properties = d
        return get_trade_balance_response_200_result

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
