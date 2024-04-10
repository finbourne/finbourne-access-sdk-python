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
from pydantic.v1 import BaseModel, Field, StrictStr, constr
from finbourne_access.models.operator import Operator

class MetadataExpression(BaseModel):
    """
    MetadataExpression
    """
    metadata_key: constr(strict=True, min_length=1) = Field(..., alias="metadataKey")
    operator: Operator = Field(...)
    text_value: Optional[StrictStr] = Field(None, alias="textValue")
    __properties = ["metadataKey", "operator", "textValue"]

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
    def from_json(cls, json_str: str) -> MetadataExpression:
        """Create an instance of MetadataExpression from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if text_value (nullable) is None
        # and __fields_set__ contains the field
        if self.text_value is None and "text_value" in self.__fields_set__:
            _dict['textValue'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MetadataExpression:
        """Create an instance of MetadataExpression from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MetadataExpression.parse_obj(obj)

        _obj = MetadataExpression.parse_obj({
            "metadata_key": obj.get("metadataKey"),
            "operator": obj.get("operator"),
            "text_value": obj.get("textValue")
        })
        return _obj
