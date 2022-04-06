from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="InlineResponse20037MinimumAmount")


@attr.s(auto_attribs=True)
class InlineResponse20037MinimumAmount:
    """Minimium amounts for staking/unstaking.

    Attributes:
        unstaking (str):  Default: '0'.
        staking (str):  Default: '0'.
    """

    unstaking: str = "0"
    staking: str = "0"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unstaking = self.unstaking
        staking = self.staking

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "unstaking": unstaking,
                "staking": staking,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unstaking = d.pop("unstaking")

        staking = d.pop("staking")

        inline_response_20037_minimum_amount = cls(
            unstaking=unstaking,
            staking=staking,
        )

        inline_response_20037_minimum_amount.additional_properties = d
        return inline_response_20037_minimum_amount

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
