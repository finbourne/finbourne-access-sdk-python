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
from pydantic import BaseModel, Field, StrictStr, conlist
from finbourne_access.models.selector_definition import SelectorDefinition
from finbourne_access.models.template_metadata import TemplateMetadata

class GeneratedPolicyComponents(BaseModel):
    """
    Response object for policy generated from template  # noqa: E501
    """
    applications: Optional[conlist(StrictStr)] = Field(None, description="Applications to which the policy applies")
    template_metadata: Optional[TemplateMetadata] = Field(None, alias="templateMetadata")
    selectors: Optional[conlist(SelectorDefinition)] = Field(None, description="Selectors that this policy will be applied to")
    __properties = ["applications", "templateMetadata", "selectors"]

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
    def from_json(cls, json_str: str) -> GeneratedPolicyComponents:
        """Create an instance of GeneratedPolicyComponents from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of template_metadata
        if self.template_metadata:
            _dict['templateMetadata'] = self.template_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in selectors (list)
        _items = []
        if self.selectors:
            for _item in self.selectors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['selectors'] = _items
        # set to None if applications (nullable) is None
        # and __fields_set__ contains the field
        if self.applications is None and "applications" in self.__fields_set__:
            _dict['applications'] = None

        # set to None if selectors (nullable) is None
        # and __fields_set__ contains the field
        if self.selectors is None and "selectors" in self.__fields_set__:
            _dict['selectors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GeneratedPolicyComponents:
        """Create an instance of GeneratedPolicyComponents from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GeneratedPolicyComponents.parse_obj(obj)

        _obj = GeneratedPolicyComponents.parse_obj({
            "applications": obj.get("applications"),
            "template_metadata": TemplateMetadata.from_dict(obj.get("templateMetadata")) if obj.get("templateMetadata") is not None else None,
            "selectors": [SelectorDefinition.from_dict(_item) for _item in obj.get("selectors")] if obj.get("selectors") is not None else None
        })
        return _obj
