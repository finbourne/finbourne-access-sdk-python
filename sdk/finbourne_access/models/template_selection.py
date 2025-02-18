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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist, constr, validator 

class TemplateSelection(BaseModel):
    """
    A template selection, identifying a policy template to use for generation  # noqa: E501
    """
    scope:  StrictStr = Field(...,alias="scope", description="Scope identifying policy template to use for generation") 
    code:  StrictStr = Field(...,alias="code", description="Code identifying policy template to use for generation") 
    selector_tags: Optional[conlist(StrictStr)] = Field(None, alias="selectorTags", description="List of selector tags to optionally filter in the template generation   (Eg: Feature, Data, etc)")
    __properties = ["scope", "code", "selectorTags"]

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
    def from_json(cls, json_str: str) -> TemplateSelection:
        """Create an instance of TemplateSelection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if selector_tags (nullable) is None
        # and __fields_set__ contains the field
        if self.selector_tags is None and "selector_tags" in self.__fields_set__:
            _dict['selectorTags'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TemplateSelection:
        """Create an instance of TemplateSelection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TemplateSelection.parse_obj(obj)

        _obj = TemplateSelection.parse_obj({
            "scope": obj.get("scope"),
            "code": obj.get("code"),
            "selector_tags": obj.get("selectorTags")
        })
        return _obj
