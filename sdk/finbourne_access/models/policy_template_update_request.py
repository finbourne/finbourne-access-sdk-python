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
from pydantic.v1 import BaseModel, Field, conlist, constr, Field
from finbourne_access.models.policy_templated_selector import PolicyTemplatedSelector

class PolicyTemplateUpdateRequest(BaseModel):
    """
    Update policy template request  # noqa: E501
    """
    display_name: constr(strict=True) = Field(...,alias="displayName", description="The display name of the policy template being created") 
    description: constr(strict=True) = Field(...,alias="description", description="Description of the policy template being craeted") 
    templated_selectors: conlist(PolicyTemplatedSelector) = Field(..., alias="templatedSelectors", description="The selector definitions of policies included in this policy template")
    __properties = ["displayName", "description", "templatedSelectors"]

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
    def from_json(cls, json_str: str) -> PolicyTemplateUpdateRequest:
        """Create an instance of PolicyTemplateUpdateRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PolicyTemplateUpdateRequest:
        """Create an instance of PolicyTemplateUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PolicyTemplateUpdateRequest.parse_obj(obj)

        _obj = PolicyTemplateUpdateRequest.parse_obj({
            "display_name": obj.get("displayName"),
            "description": obj.get("description"),
            "templated_selectors": [PolicyTemplatedSelector.from_dict(_item) for _item in obj.get("templatedSelectors")] if obj.get("templatedSelectors") is not None else None
        })
        return _obj
