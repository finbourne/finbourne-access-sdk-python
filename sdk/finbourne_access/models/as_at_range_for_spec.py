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


from typing import Any, Dict
from pydantic.v1 import StrictStr, Field, BaseModel, Field 
from finbourne_access.models.as_at_predicate_contract import AsAtPredicateContract

class AsAtRangeForSpec(BaseModel):
    """
    AsAtRangeForSpec
    """
    var_from: AsAtPredicateContract = Field(..., alias="from")
    to: AsAtPredicateContract = Field(...)
    __properties = ["from", "to"]

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
    def from_json(cls, json_str: str) -> AsAtRangeForSpec:
        """Create an instance of AsAtRangeForSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of var_from
        if self.var_from:
            _dict['from'] = self.var_from.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to
        if self.to:
            _dict['to'] = self.to.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AsAtRangeForSpec:
        """Create an instance of AsAtRangeForSpec from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AsAtRangeForSpec.parse_obj(obj)

        _obj = AsAtRangeForSpec.parse_obj({
            "var_from": AsAtPredicateContract.from_dict(obj.get("from")) if obj.get("from") is not None else None,
            "to": AsAtPredicateContract.from_dict(obj.get("to")) if obj.get("to") is not None else None
        })
        return _obj
