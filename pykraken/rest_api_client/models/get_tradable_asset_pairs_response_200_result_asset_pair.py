from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetTradableAssetPairsResponse200ResultAssetPair")


@attr.s(auto_attribs=True)
class GetTradableAssetPairsResponse200ResultAssetPair:
    """Trading Asset Pair

    Attributes:
        altname (Union[Unset, str]): Alternate pair name
        wsname (Union[Unset, str]): WebSocket pair name (if available)
        aclass_base (Union[Unset, str]): Asset class of base component
        base (Union[Unset, str]): Asset ID of base component
        aclass_quote (Union[Unset, str]): Asset class of quote component
        quote (Union[Unset, str]): Asset ID of quote component
        lot (Union[Unset, str]): Volume lot size
        pair_decimals (Union[Unset, int]): Scaling decimal places for pair
        lot_decimals (Union[Unset, int]): Scaling decimal places for volume
        lot_multiplier (Union[Unset, int]): Amount to multiply lot volume by to get currency volume
        leverage_buy (Union[Unset, List[int]]): Array of leverage amounts available when buying
        leverage_sell (Union[Unset, List[int]]): Array of leverage amounts available when selling
        fees (Union[Unset, List[List[Union[float, int]]]]): Fee schedule array in `[<volume>, <percent fee>]` tuples
        fees_maker (Union[Unset, List[List[Union[float, int]]]]): Maker fee schedule array in `[<volume>, <percent
            fee>]`  tuples (if on maker/taker)
        fee_volume_currency (Union[Unset, str]): Volume discount currency
        margin_call (Union[Unset, int]): Margin call level
        margin_stop (Union[Unset, int]): Stop-out/liquidation margin level
        ordermin (Union[Unset, str]): Minimum order size (in terms of base currency)
    """

    altname: Union[Unset, str] = UNSET
    wsname: Union[Unset, str] = UNSET
    aclass_base: Union[Unset, str] = UNSET
    base: Union[Unset, str] = UNSET
    aclass_quote: Union[Unset, str] = UNSET
    quote: Union[Unset, str] = UNSET
    lot: Union[Unset, str] = UNSET
    pair_decimals: Union[Unset, int] = UNSET
    lot_decimals: Union[Unset, int] = UNSET
    lot_multiplier: Union[Unset, int] = UNSET
    leverage_buy: Union[Unset, List[int]] = UNSET
    leverage_sell: Union[Unset, List[int]] = UNSET
    fees: Union[Unset, List[List[Union[float, int]]]] = UNSET
    fees_maker: Union[Unset, List[List[Union[float, int]]]] = UNSET
    fee_volume_currency: Union[Unset, str] = UNSET
    margin_call: Union[Unset, int] = UNSET
    margin_stop: Union[Unset, int] = UNSET
    ordermin: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        altname = self.altname
        wsname = self.wsname
        aclass_base = self.aclass_base
        base = self.base
        aclass_quote = self.aclass_quote
        quote = self.quote
        lot = self.lot
        pair_decimals = self.pair_decimals
        lot_decimals = self.lot_decimals
        lot_multiplier = self.lot_multiplier
        leverage_buy: Union[Unset, List[int]] = UNSET
        if not isinstance(self.leverage_buy, Unset):
            leverage_buy = self.leverage_buy

        leverage_sell: Union[Unset, List[int]] = UNSET
        if not isinstance(self.leverage_sell, Unset):
            leverage_sell = self.leverage_sell

        fees: Union[Unset, List[List[Union[float, int]]]] = UNSET
        if not isinstance(self.fees, Unset):
            fees = []
            for fees_item_data in self.fees:
                fees_item = []
                for fees_item_item_data in fees_item_data:

                    fees_item_item = fees_item_item_data

                    fees_item.append(fees_item_item)

                fees.append(fees_item)

        fees_maker: Union[Unset, List[List[Union[float, int]]]] = UNSET
        if not isinstance(self.fees_maker, Unset):
            fees_maker = []
            for fees_maker_item_data in self.fees_maker:
                fees_maker_item = []
                for fees_maker_item_item_data in fees_maker_item_data:

                    fees_maker_item_item = fees_maker_item_item_data

                    fees_maker_item.append(fees_maker_item_item)

                fees_maker.append(fees_maker_item)

        fee_volume_currency = self.fee_volume_currency
        margin_call = self.margin_call
        margin_stop = self.margin_stop
        ordermin = self.ordermin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if altname is not UNSET:
            field_dict["altname"] = altname
        if wsname is not UNSET:
            field_dict["wsname"] = wsname
        if aclass_base is not UNSET:
            field_dict["aclass_base"] = aclass_base
        if base is not UNSET:
            field_dict["base"] = base
        if aclass_quote is not UNSET:
            field_dict["aclass_quote"] = aclass_quote
        if quote is not UNSET:
            field_dict["quote"] = quote
        if lot is not UNSET:
            field_dict["lot"] = lot
        if pair_decimals is not UNSET:
            field_dict["pair_decimals"] = pair_decimals
        if lot_decimals is not UNSET:
            field_dict["lot_decimals"] = lot_decimals
        if lot_multiplier is not UNSET:
            field_dict["lot_multiplier"] = lot_multiplier
        if leverage_buy is not UNSET:
            field_dict["leverage_buy"] = leverage_buy
        if leverage_sell is not UNSET:
            field_dict["leverage_sell"] = leverage_sell
        if fees is not UNSET:
            field_dict["fees"] = fees
        if fees_maker is not UNSET:
            field_dict["fees_maker"] = fees_maker
        if fee_volume_currency is not UNSET:
            field_dict["fee_volume_currency"] = fee_volume_currency
        if margin_call is not UNSET:
            field_dict["margin_call"] = margin_call
        if margin_stop is not UNSET:
            field_dict["margin_stop"] = margin_stop
        if ordermin is not UNSET:
            field_dict["ordermin"] = ordermin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        altname = d.pop("altname", UNSET)

        wsname = d.pop("wsname", UNSET)

        aclass_base = d.pop("aclass_base", UNSET)

        base = d.pop("base", UNSET)

        aclass_quote = d.pop("aclass_quote", UNSET)

        quote = d.pop("quote", UNSET)

        lot = d.pop("lot", UNSET)

        pair_decimals = d.pop("pair_decimals", UNSET)

        lot_decimals = d.pop("lot_decimals", UNSET)

        lot_multiplier = d.pop("lot_multiplier", UNSET)

        leverage_buy = cast(List[int], d.pop("leverage_buy", UNSET))

        leverage_sell = cast(List[int], d.pop("leverage_sell", UNSET))

        fees = []
        _fees = d.pop("fees", UNSET)
        for fees_item_data in _fees or []:
            fees_item = []
            _fees_item = fees_item_data
            for fees_item_item_data in _fees_item:

                def _parse_fees_item_item(data: object) -> Union[float, int]:
                    return cast(Union[float, int], data)

                fees_item_item = _parse_fees_item_item(fees_item_item_data)

                fees_item.append(fees_item_item)

            fees.append(fees_item)

        fees_maker = []
        _fees_maker = d.pop("fees_maker", UNSET)
        for fees_maker_item_data in _fees_maker or []:
            fees_maker_item = []
            _fees_maker_item = fees_maker_item_data
            for fees_maker_item_item_data in _fees_maker_item:

                def _parse_fees_maker_item_item(data: object) -> Union[float, int]:
                    return cast(Union[float, int], data)

                fees_maker_item_item = _parse_fees_maker_item_item(fees_maker_item_item_data)

                fees_maker_item.append(fees_maker_item_item)

            fees_maker.append(fees_maker_item)

        fee_volume_currency = d.pop("fee_volume_currency", UNSET)

        margin_call = d.pop("margin_call", UNSET)

        margin_stop = d.pop("margin_stop", UNSET)

        ordermin = d.pop("ordermin", UNSET)

        get_tradable_asset_pairs_response_200_result_asset_pair = cls(
            altname=altname,
            wsname=wsname,
            aclass_base=aclass_base,
            base=base,
            aclass_quote=aclass_quote,
            quote=quote,
            lot=lot,
            pair_decimals=pair_decimals,
            lot_decimals=lot_decimals,
            lot_multiplier=lot_multiplier,
            leverage_buy=leverage_buy,
            leverage_sell=leverage_sell,
            fees=fees,
            fees_maker=fees_maker,
            fee_volume_currency=fee_volume_currency,
            margin_call=margin_call,
            margin_stop=margin_stop,
            ordermin=ordermin,
        )

        get_tradable_asset_pairs_response_200_result_asset_pair.additional_properties = d
        return get_tradable_asset_pairs_response_200_result_asset_pair

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
