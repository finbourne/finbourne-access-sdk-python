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
from pydantic.v1 import BaseModel, Field, constr, validator

class RequestedActionKey(BaseModel):
    """
    A fully qualified action identifier  # noqa: E501
    """
    entity_code: constr(strict=True, max_length=100, min_length=3) = Field(..., alias="entityCode", description="The type of the resource on which the activity would be performed")
    scope: constr(strict=True, max_length=100, min_length=3) = Field(..., description="The scope/provider/vendor of the activity")
    activity: constr(strict=True, max_length=100, min_length=3) = Field(..., description="The identifier of the action to be performed on the resource")
    __properties = ["entityCode", "scope", "activity"]

    @validator('entity_code')
    def entity_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?=.*[a-zA-Z])[\w][\w +-]{2,100}$", value):
            raise ValueError(r"must validate the regular expression /^(?=.*[a-zA-Z])[\w][\w +-]{2,100}$/")
        return value

    @validator('scope')
    def scope_validate_regular_expression(cls, value):
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
    def from_json(cls, json_str: str) -> RequestedActionKey:
        """Create an instance of RequestedActionKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RequestedActionKey:
        """Create an instance of RequestedActionKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RequestedActionKey.parse_obj(obj)

        _obj = RequestedActionKey.parse_obj({
            "entity_code": obj.get("entityCode"),
            "scope": obj.get("scope"),
            "activity": obj.get("activity")
        })
        return _obj
