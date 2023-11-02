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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictStr, conlist
from finbourne_access.models.key_value_pair_of_string_to_string import KeyValuePairOfStringToString

class HowSpec(BaseModel):
    """
    HowSpec
    """
    type: Optional[StrictStr] = None
    parameters: Optional[conlist(KeyValuePairOfStringToString)] = None
    __properties = ["type", "parameters"]

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
    def from_json(cls, json_str: str) -> HowSpec:
        """Create an instance of HowSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in parameters (list)
        _items = []
        if self.parameters:
            for _item in self.parameters:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parameters'] = _items
        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict['type'] = None

        # set to None if parameters (nullable) is None
        # and __fields_set__ contains the field
        if self.parameters is None and "parameters" in self.__fields_set__:
            _dict['parameters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HowSpec:
        """Create an instance of HowSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HowSpec.parse_obj(obj)

        _obj = HowSpec.parse_obj({
            "type": obj.get("type"),
            "parameters": [KeyValuePairOfStringToString.from_dict(_item) for _item in obj.get("parameters")] if obj.get("parameters") is not None else None
        })
        return _obj
