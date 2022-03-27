from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.closed_order import ClosedOrder
from ..models.open_order import OpenOrder

T = TypeVar("T", bound="GetOrdersInfoResponse200Result")


@attr.s(auto_attribs=True)
class GetOrdersInfoResponse200Result:
    """ """

    additional_properties: Dict[str, Union[ClosedOrder, OpenOrder]] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:

        field_dict: Dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():

            if isinstance(prop, OpenOrder):
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

            def _parse_additional_property(data: object) -> Union[ClosedOrder, OpenOrder]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_0 = OpenOrder.from_dict(data)

                    return additional_property_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                additional_property_type_1 = ClosedOrder.from_dict(data)

                return additional_property_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        get_orders_info_response_200_result.additional_properties = additional_properties
        return get_orders_info_response_200_result

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Union[ClosedOrder, OpenOrder]:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Union[ClosedOrder, OpenOrder]) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
