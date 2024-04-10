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
from pydantic.v1 import BaseModel
from finbourne_access.models.date_quality import DateQuality

class EffectiveDateHasQuality(BaseModel):
    """
    EffectiveDateHasQuality
    """
    quality: Optional[DateQuality] = None
    __properties = ["quality"]

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
    def from_json(cls, json_str: str) -> EffectiveDateHasQuality:
        """Create an instance of EffectiveDateHasQuality from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EffectiveDateHasQuality:
        """Create an instance of EffectiveDateHasQuality from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EffectiveDateHasQuality.parse_obj(obj)

        _obj = EffectiveDateHasQuality.parse_obj({
            "quality": obj.get("quality")
        })
        return _obj
