from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.inline_response_20037_lock import InlineResponse20037Lock
from ..models.inline_response_20037_minimum_amount import InlineResponse20037MinimumAmount
from ..models.inline_response_20037_rewards import InlineResponse20037Rewards
from ..types import UNSET, Unset

T = TypeVar("T", bound="StakingAssetInformation")


@attr.s(auto_attribs=True)
class StakingAssetInformation:
    """
    Attributes:
        asset (str): Asset code/name
        staking_asset (str): Staking asset code/name
        rewards (InlineResponse20037Rewards): Describes the rewards earned while staking.
        method (Union[Unset, str]): Unique ID of the staking option (used in Stake/Unstake operations)
        on_chain (Union[Unset, bool]): Whether the staking operation is on-chain or not. Default: True.
        can_stake (Union[Unset, bool]): Whether the user will be able to stake this asset. Default: True.
        can_unstake (Union[Unset, bool]): Whether the user will be able to unstake this asset. Default: True.
        minimum_amount (Union[Unset, InlineResponse20037MinimumAmount]): Minimium amounts for staking/unstaking.
        lock (Union[Unset, InlineResponse20037Lock]): Describes the locking periods and percentages for
            staking/unstaking operations.
        enabled_for_user (Union[Unset, bool]):  Default: True.
        disabled (Union[Unset, bool]):
    """

    asset: str
    staking_asset: str
    rewards: InlineResponse20037Rewards
    method: Union[Unset, str] = UNSET
    on_chain: Union[Unset, bool] = True
    can_stake: Union[Unset, bool] = True
    can_unstake: Union[Unset, bool] = True
    minimum_amount: Union[Unset, InlineResponse20037MinimumAmount] = UNSET
    lock: Union[Unset, InlineResponse20037Lock] = UNSET
    enabled_for_user: Union[Unset, bool] = True
    disabled: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        asset = self.asset
        staking_asset = self.staking_asset
        rewards = self.rewards.to_dict()

        method = self.method
        on_chain = self.on_chain
        can_stake = self.can_stake
        can_unstake = self.can_unstake
        minimum_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.minimum_amount, Unset):
            minimum_amount = self.minimum_amount.to_dict()

        lock: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.lock, Unset):
            lock = self.lock.to_dict()

        enabled_for_user = self.enabled_for_user
        disabled = self.disabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "asset": asset,
                "staking_asset": staking_asset,
                "rewards": rewards,
            }
        )
        if method is not UNSET:
            field_dict["method"] = method
        if on_chain is not UNSET:
            field_dict["on_chain"] = on_chain
        if can_stake is not UNSET:
            field_dict["can_stake"] = can_stake
        if can_unstake is not UNSET:
            field_dict["can_unstake"] = can_unstake
        if minimum_amount is not UNSET:
            field_dict["minimum_amount"] = minimum_amount
        if lock is not UNSET:
            field_dict["lock"] = lock
        if enabled_for_user is not UNSET:
            field_dict["enabled_for_user"] = enabled_for_user
        if disabled is not UNSET:
            field_dict["disabled"] = disabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        asset = d.pop("asset")

        staking_asset = d.pop("staking_asset")

        rewards = InlineResponse20037Rewards.from_dict(d.pop("rewards"))

        method = d.pop("method", UNSET)

        on_chain = d.pop("on_chain", UNSET)

        can_stake = d.pop("can_stake", UNSET)

        can_unstake = d.pop("can_unstake", UNSET)

        _minimum_amount = d.pop("minimum_amount", UNSET)
        minimum_amount: Union[Unset, InlineResponse20037MinimumAmount]
        if isinstance(_minimum_amount, Unset):
            minimum_amount = UNSET
        else:
            minimum_amount = InlineResponse20037MinimumAmount.from_dict(_minimum_amount)

        _lock = d.pop("lock", UNSET)
        lock: Union[Unset, InlineResponse20037Lock]
        if isinstance(_lock, Unset):
            lock = UNSET
        else:
            lock = InlineResponse20037Lock.from_dict(_lock)

        enabled_for_user = d.pop("enabled_for_user", UNSET)

        disabled = d.pop("disabled", UNSET)

        staking_asset_information = cls(
            asset=asset,
            staking_asset=staking_asset,
            rewards=rewards,
            method=method,
            on_chain=on_chain,
            can_stake=can_stake,
            can_unstake=can_unstake,
            minimum_amount=minimum_amount,
            lock=lock,
            enabled_for_user=enabled_for_user,
            disabled=disabled,
        )

        staking_asset_information.additional_properties = d
        return staking_asset_information

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
