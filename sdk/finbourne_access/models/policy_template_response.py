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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist 
from finbourne_access.models.policy_templated_selector import PolicyTemplatedSelector

class PolicyTemplateResponse(BaseModel):
    """
    Response object for a policy template  # noqa: E501
    """
    display_name:  Optional[StrictStr] = Field(None,alias="displayName", description="Display name of the policy template being created") 
    scope:  Optional[StrictStr] = Field(None,alias="scope", description="The Scope of the policy template being created") 
    code:  Optional[StrictStr] = Field(None,alias="code", description="The Code of the policy template being created") 
    description:  Optional[StrictStr] = Field(None,alias="description", description="Description of the policy template being created") 
    applications: Optional[conlist(StrictStr)] = Field(None, description="List of applications that this policy template covers")
    tags: Optional[conlist(StrictStr)] = Field(None, description="List of policy types that this policy template covers")
    templated_selectors: Optional[conlist(PolicyTemplatedSelector)] = Field(None, alias="templatedSelectors", description="The selector definitions of policies included in this policy template")
    __properties = ["displayName", "scope", "code", "description", "applications", "tags", "templatedSelectors"]

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
    def from_json(cls, json_str: str) -> PolicyTemplateResponse:
        """Create an instance of PolicyTemplateResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in templated_selectors (list)
        _items = []
        if self.templated_selectors:
            for _item in self.templated_selectors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['templatedSelectors'] = _items
        # set to None if display_name (nullable) is None
        # and __fields_set__ contains the field
        if self.display_name is None and "display_name" in self.__fields_set__:
            _dict['displayName'] = None

        # set to None if scope (nullable) is None
        # and __fields_set__ contains the field
        if self.scope is None and "scope" in self.__fields_set__:
            _dict['scope'] = None

        # set to None if code (nullable) is None
        # and __fields_set__ contains the field
        if self.code is None and "code" in self.__fields_set__:
            _dict['code'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if applications (nullable) is None
        # and __fields_set__ contains the field
        if self.applications is None and "applications" in self.__fields_set__:
            _dict['applications'] = None

        # set to None if tags (nullable) is None
        # and __fields_set__ contains the field
        if self.tags is None and "tags" in self.__fields_set__:
            _dict['tags'] = None

        # set to None if templated_selectors (nullable) is None
        # and __fields_set__ contains the field
        if self.templated_selectors is None and "templated_selectors" in self.__fields_set__:
            _dict['templatedSelectors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PolicyTemplateResponse:
        """Create an instance of PolicyTemplateResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PolicyTemplateResponse.parse_obj(obj)

        _obj = PolicyTemplateResponse.parse_obj({
            "display_name": obj.get("displayName"),
            "scope": obj.get("scope"),
            "code": obj.get("code"),
            "description": obj.get("description"),
            "applications": obj.get("applications"),
            "tags": obj.get("tags"),
            "templated_selectors": [PolicyTemplatedSelector.from_dict(_item) for _item in obj.get("templatedSelectors")] if obj.get("templatedSelectors") is not None else None
        })
        return _obj
