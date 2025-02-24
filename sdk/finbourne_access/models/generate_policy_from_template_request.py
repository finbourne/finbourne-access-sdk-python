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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, conlist 
from finbourne_access.models.selector_definition import SelectorDefinition
from finbourne_access.models.template_selection import TemplateSelection

class GeneratePolicyFromTemplateRequest(BaseModel):
    """
    Generate policy from template  # noqa: E501
    """
    template_selection: conlist(TemplateSelection) = Field(..., alias="templateSelection", description="List of template selection, identifying policy templates to use for generation")
    selectors: Optional[conlist(SelectorDefinition)] = Field(None, description="List of additional selectors to be included in the policy")
    __properties = ["templateSelection", "selectors"]

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
    def from_json(cls, json_str: str) -> GeneratePolicyFromTemplateRequest:
        """Create an instance of GeneratePolicyFromTemplateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in template_selection (list)
        _items = []
        if self.template_selection:
            for _item in self.template_selection:
                if _item:
                    _items.append(_item.to_dict())
            _dict['templateSelection'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in selectors (list)
        _items = []
        if self.selectors:
            for _item in self.selectors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['selectors'] = _items
        # set to None if selectors (nullable) is None
        # and __fields_set__ contains the field
        if self.selectors is None and "selectors" in self.__fields_set__:
            _dict['selectors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GeneratePolicyFromTemplateRequest:
        """Create an instance of GeneratePolicyFromTemplateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GeneratePolicyFromTemplateRequest.parse_obj(obj)

        _obj = GeneratePolicyFromTemplateRequest.parse_obj({
            "template_selection": [TemplateSelection.from_dict(_item) for _item in obj.get("templateSelection")] if obj.get("templateSelection") is not None else None,
            "selectors": [SelectorDefinition.from_dict(_item) for _item in obj.get("selectors")] if obj.get("selectors") is not None else None
        })
        return _obj
