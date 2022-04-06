from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.inline_response_20037_rewards_type import InlineResponse20037RewardsType
from ..types import UNSET, Unset

T = TypeVar("T", bound="InlineResponse20037Rewards")


@attr.s(auto_attribs=True)
class InlineResponse20037Rewards:
    """Describes the rewards earned while staking.

    Attributes:
        reward (Union[Unset, str]): Reward earned while staking
        type (Union[Unset, InlineResponse20037RewardsType]): Reward type
    """

    reward: Union[Unset, str] = UNSET
    type: Union[Unset, InlineResponse20037RewardsType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reward = self.reward
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reward is not UNSET:
            field_dict["reward"] = reward
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reward = d.pop("reward", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, InlineResponse20037RewardsType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = InlineResponse20037RewardsType(_type)

        inline_response_20037_rewards = cls(
            reward=reward,
            type=type,
        )

        inline_response_20037_rewards.additional_properties = d
        return inline_response_20037_rewards

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
