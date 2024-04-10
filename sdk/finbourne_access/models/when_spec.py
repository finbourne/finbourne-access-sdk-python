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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

class WhenSpec(BaseModel):
    """
    WhenSpec
    """
    activate: datetime = Field(...)
    deactivate: Optional[datetime] = None
    __properties = ["activate", "deactivate"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> WhenSpec:
        """Create an instance of WhenSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if deactivate (nullable) is None
        # and __fields_set__ contains the field
        if self.deactivate is None and "deactivate" in self.__fields_set__:
            _dict['deactivate'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WhenSpec:
        """Create an instance of WhenSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WhenSpec.parse_obj(obj)

        _obj = WhenSpec.parse_obj({
            "activate": obj.get("activate"),
            "deactivate": obj.get("deactivate")
        })
        return _obj
