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


from typing import Any, Dict, List
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist 

class NonTransitiveSupervisorRoleResource(BaseModel):
    """
    NonTransitiveSupervisorRoleResource
    """
    roles: conlist(Dict[str, StrictStr], min_items=1) = Field(...)
    __properties = ["roles"]

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
    def from_json(cls, json_str: str) -> NonTransitiveSupervisorRoleResource:
        """Create an instance of NonTransitiveSupervisorRoleResource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NonTransitiveSupervisorRoleResource:
        """Create an instance of NonTransitiveSupervisorRoleResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NonTransitiveSupervisorRoleResource.parse_obj(obj)

        _obj = NonTransitiveSupervisorRoleResource.parse_obj({
            "roles": obj.get("roles")
        })
        return _obj
