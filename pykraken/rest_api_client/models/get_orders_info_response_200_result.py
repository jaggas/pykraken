from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_orders_info_response_200_result_closed_order import GetOrdersInfoResponse200ResultClosedOrder
from ..models.get_orders_info_response_200_result_open_order import GetOrdersInfoResponse200ResultOpenOrder

T = TypeVar("T", bound="GetOrdersInfoResponse200Result")


@attr.s(auto_attribs=True)
class GetOrdersInfoResponse200Result:
    """ """

    additional_properties: Dict[
        str, Union[GetOrdersInfoResponse200ResultClosedOrder, GetOrdersInfoResponse200ResultOpenOrder]
    ] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():

            if isinstance(prop, GetOrdersInfoResponse200ResultOpenOrder):
                field_dict[prop_name] = prop.to_dict()

            else:
                field_dict[prop_name] = prop.to_dict()

        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        get_orders_info_response_200_result = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> Union[GetOrdersInfoResponse200ResultClosedOrder, GetOrdersInfoResponse200ResultOpenOrder]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = GetOrdersInfoResponse200ResultOpenOrder.from_dict(data)

                    return additional_property_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_1 = GetOrdersInfoResponse200ResultClosedOrder.from_dict(data)

                return additional_property_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        get_orders_info_response_200_result.additional_properties = additional_properties
        return get_orders_info_response_200_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(
        self, key: str
    ) -> Union[GetOrdersInfoResponse200ResultClosedOrder, GetOrdersInfoResponse200ResultOpenOrder]:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: Union[GetOrdersInfoResponse200ResultClosedOrder, GetOrdersInfoResponse200ResultOpenOrder]
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
