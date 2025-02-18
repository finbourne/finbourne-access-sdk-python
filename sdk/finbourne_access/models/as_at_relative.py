# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictInt 
from finbourne_access.models.date_unit import DateUnit
from finbourne_access.models.point_in_time_specification import PointInTimeSpecification
from finbourne_access.models.relative_to_date_time import RelativeToDateTime

class AsAtRelative(BaseModel):
    """
    AsAtRelative
    """
    var_date: Optional[PointInTimeSpecification] = Field(None, alias="date")
    adjustment: Optional[StrictInt] = None
    unit: Optional[DateUnit] = None
    relative_to_date_time: Optional[RelativeToDateTime] = Field(None, alias="relativeToDateTime")
    __properties = ["date", "adjustment", "unit", "relativeToDateTime"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AsAtRelative:
        """Create an instance of AsAtRelative from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AsAtRelative:
        """Create an instance of AsAtRelative from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AsAtRelative.parse_obj(obj)

        _obj = AsAtRelative.parse_obj({
            "var_date": obj.get("date"),
            "adjustment": obj.get("adjustment"),
            "unit": obj.get("unit"),
            "relative_to_date_time": obj.get("relativeToDateTime")
        })
        return _obj
