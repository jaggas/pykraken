from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AssetInfo")


@attr.s(auto_attribs=True)
class AssetInfo:
    """
    Attributes:
        aclass (Union[Unset, str]): Asset class
        altname (Union[Unset, str]): Alternate name
        decimals (Union[Unset, int]): Scaling decimal for record keeping
        display_decimals (Union[Unset, int]): Scaling decimal for output display
    """

    aclass: Union[Unset, str] = UNSET
    altname: Union[Unset, str] = UNSET
    decimals: Union[Unset, int] = UNSET
    display_decimals: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aclass = self.aclass
        altname = self.altname
        decimals = self.decimals
        display_decimals = self.display_decimals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aclass is not UNSET:
            field_dict["aclass"] = aclass
        if altname is not UNSET:
            field_dict["altname"] = altname
        if decimals is not UNSET:
            field_dict["decimals"] = decimals
        if display_decimals is not UNSET:
            field_dict["display_decimals"] = display_decimals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aclass = d.pop("aclass", UNSET)

        altname = d.pop("altname", UNSET)

        decimals = d.pop("decimals", UNSET)

        display_decimals = d.pop("display_decimals", UNSET)

        asset_info = cls(
            aclass=aclass,
            altname=altname,
            decimals=decimals,
            display_decimals=display_decimals,
        )

        asset_info.additional_properties = d
        return asset_info

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
