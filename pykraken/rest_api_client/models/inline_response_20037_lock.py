from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.staking_lock_info import StakingLockInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="InlineResponse20037Lock")


@attr.s(auto_attribs=True)
class InlineResponse20037Lock:
    """Describes the locking periods and percentages for staking/unstaking operations.

    Attributes:
        unstaking (Union[Unset, List[StakingLockInfo]]):
        staking (Union[Unset, List[StakingLockInfo]]):
        lockup (Union[Unset, List[StakingLockInfo]]):
    """

    unstaking: Union[Unset, List[StakingLockInfo]] = UNSET
    staking: Union[Unset, List[StakingLockInfo]] = UNSET
    lockup: Union[Unset, List[StakingLockInfo]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        unstaking: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.unstaking, Unset):
            unstaking = []
            for unstaking_item_data in self.unstaking:
                unstaking_item = unstaking_item_data.to_dict()

                unstaking.append(unstaking_item)

        staking: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.staking, Unset):
            staking = []
            for staking_item_data in self.staking:
                staking_item = staking_item_data.to_dict()

                staking.append(staking_item)

        lockup: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.lockup, Unset):
            lockup = []
            for lockup_item_data in self.lockup:
                lockup_item = lockup_item_data.to_dict()

                lockup.append(lockup_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unstaking is not UNSET:
            field_dict["unstaking"] = unstaking
        if staking is not UNSET:
            field_dict["staking"] = staking
        if lockup is not UNSET:
            field_dict["lockup"] = lockup

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        unstaking = []
        _unstaking = d.pop("unstaking", UNSET)
        for unstaking_item_data in _unstaking or []:
            unstaking_item = StakingLockInfo.from_dict(unstaking_item_data)

            unstaking.append(unstaking_item)

        staking = []
        _staking = d.pop("staking", UNSET)
        for staking_item_data in _staking or []:
            staking_item = StakingLockInfo.from_dict(staking_item_data)

            staking.append(staking_item)

        lockup = []
        _lockup = d.pop("lockup", UNSET)
        for lockup_item_data in _lockup or []:
            lockup_item = StakingLockInfo.from_dict(lockup_item_data)

            lockup.append(lockup_item)

        inline_response_20037_lock = cls(
            unstaking=unstaking,
            staking=staking,
            lockup=lockup,
        )

        inline_response_20037_lock.additional_properties = d
        return inline_response_20037_lock

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
