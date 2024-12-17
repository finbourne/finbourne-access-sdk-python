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
from pydantic.v1 import BaseModel, Field, Field
from finbourne_access.models.as_at_range_for_spec import AsAtRangeForSpec
from finbourne_access.models.as_at_relative import AsAtRelative
from finbourne_access.models.effective_date_has_quality import EffectiveDateHasQuality
from finbourne_access.models.effective_date_relative import EffectiveDateRelative
from finbourne_access.models.effective_range import EffectiveRange

class ForSpec(BaseModel):
    """
    ForSpec
    """
    as_at_range_for_spec: Optional[AsAtRangeForSpec] = Field(None, alias="asAtRangeForSpec")
    as_at_relative: Optional[AsAtRelative] = Field(None, alias="asAtRelative")
    effective_date_has_quality: Optional[EffectiveDateHasQuality] = Field(None, alias="effectiveDateHasQuality")
    effective_date_relative: Optional[EffectiveDateRelative] = Field(None, alias="effectiveDateRelative")
    effective_range: Optional[EffectiveRange] = Field(None, alias="effectiveRange")
    __properties = ["asAtRangeForSpec", "asAtRelative", "effectiveDateHasQuality", "effectiveDateRelative", "effectiveRange"]

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
    def from_json(cls, json_str: str) -> ForSpec:
        """Create an instance of ForSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of as_at_range_for_spec
        if self.as_at_range_for_spec:
            _dict['asAtRangeForSpec'] = self.as_at_range_for_spec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of as_at_relative
        if self.as_at_relative:
            _dict['asAtRelative'] = self.as_at_relative.to_dict()
        # override the default output from pydantic by calling `to_dict()` of effective_date_has_quality
        if self.effective_date_has_quality:
            _dict['effectiveDateHasQuality'] = self.effective_date_has_quality.to_dict()
        # override the default output from pydantic by calling `to_dict()` of effective_date_relative
        if self.effective_date_relative:
            _dict['effectiveDateRelative'] = self.effective_date_relative.to_dict()
        # override the default output from pydantic by calling `to_dict()` of effective_range
        if self.effective_range:
            _dict['effectiveRange'] = self.effective_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ForSpec:
        """Create an instance of ForSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ForSpec.parse_obj(obj)

        _obj = ForSpec.parse_obj({
            "as_at_range_for_spec": AsAtRangeForSpec.from_dict(obj.get("asAtRangeForSpec")) if obj.get("asAtRangeForSpec") is not None else None,
            "as_at_relative": AsAtRelative.from_dict(obj.get("asAtRelative")) if obj.get("asAtRelative") is not None else None,
            "effective_date_has_quality": EffectiveDateHasQuality.from_dict(obj.get("effectiveDateHasQuality")) if obj.get("effectiveDateHasQuality") is not None else None,
            "effective_date_relative": EffectiveDateRelative.from_dict(obj.get("effectiveDateRelative")) if obj.get("effectiveDateRelative") is not None else None,
            "effective_range": EffectiveRange.from_dict(obj.get("effectiveRange")) if obj.get("effectiveRange") is not None else None
        })
        return _obj
