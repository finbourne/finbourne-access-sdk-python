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
from pydantic import BaseModel, Field, constr, validator

class IfIdentityScopeExpression(BaseModel):
    """
    IfIdentityScopeExpression
    """
    scope_name: constr(strict=True, min_length=1) = Field(..., alias="scopeName")
    __properties = ["scopeName"]

    @validator('scope_name')
    def scope_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?=.*[a-zA-Z])[\w][\w +-]{2,100}$", value):
            raise ValueError(r"must validate the regular expression /^(?=.*[a-zA-Z])[\w][\w +-]{2,100}$/")
        return value

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
    def from_json(cls, json_str: str) -> IfIdentityScopeExpression:
        """Create an instance of IfIdentityScopeExpression from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IfIdentityScopeExpression:
        """Create an instance of IfIdentityScopeExpression from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IfIdentityScopeExpression.parse_obj(obj)

        _obj = IfIdentityScopeExpression.parse_obj({
            "scope_name": obj.get("scopeName")
        })
        return _obj
