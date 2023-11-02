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
from finbourne_access.models.for_spec import ForSpec
from finbourne_access.models.grant import Grant
from finbourne_access.models.how_spec import HowSpec
from finbourne_access.models.if_expression import IfExpression
from finbourne_access.models.link import Link
from finbourne_access.models.policy_id import PolicyId
from finbourne_access.models.selector_definition import SelectorDefinition
from finbourne_access.models.when_spec import WhenSpec

class PolicyResponse(BaseModel):
    """
    Response object from the policy API  # noqa: E501
    """
    id: Optional[PolicyId] = None
    description: Optional[StrictStr] = Field(None, description="Description of what the policy is entitling")
    applications: Optional[conlist(StrictStr)] = Field(None, description="Applications to which the policy applies")
    grant: Optional[Grant] = None
    selectors: Optional[conlist(SelectorDefinition)] = Field(None, description="Selectors that this policy will be applied to")
    var_for: Optional[conlist(ForSpec)] = Field(None, alias="for", description="\"For Specification\" for when the policy is to be applied")
    var_if: Optional[conlist(IfExpression)] = Field(None, alias="if", description="\"If Specification\" for when the policy is to be applied")
    when: Optional[WhenSpec] = None
    how: Optional[HowSpec] = None
    links: Optional[conlist(Link)] = None
    __properties = ["id", "description", "applications", "grant", "selectors", "for", "if", "when", "how", "links"]

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
    def from_json(cls, json_str: str) -> PolicyResponse:
        """Create an instance of PolicyResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in selectors (list)
        _items = []
        if self.selectors:
            for _item in self.selectors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['selectors'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in var_for (list)
        _items = []
        if self.var_for:
            for _item in self.var_for:
                if _item:
                    _items.append(_item.to_dict())
            _dict['for'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in var_if (list)
        _items = []
        if self.var_if:
            for _item in self.var_if:
                if _item:
                    _items.append(_item.to_dict())
            _dict['if'] = _items
        # override the default output from pydantic by calling `to_dict()` of when
        if self.when:
            _dict['when'] = self.when.to_dict()
        # override the default output from pydantic by calling `to_dict()` of how
        if self.how:
            _dict['how'] = self.how.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if applications (nullable) is None
        # and __fields_set__ contains the field
        if self.applications is None and "applications" in self.__fields_set__:
            _dict['applications'] = None

        # set to None if selectors (nullable) is None
        # and __fields_set__ contains the field
        if self.selectors is None and "selectors" in self.__fields_set__:
            _dict['selectors'] = None

        # set to None if var_for (nullable) is None
        # and __fields_set__ contains the field
        if self.var_for is None and "var_for" in self.__fields_set__:
            _dict['for'] = None

        # set to None if var_if (nullable) is None
        # and __fields_set__ contains the field
        if self.var_if is None and "var_if" in self.__fields_set__:
            _dict['if'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PolicyResponse:
        """Create an instance of PolicyResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PolicyResponse.parse_obj(obj)

        _obj = PolicyResponse.parse_obj({
            "id": PolicyId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "description": obj.get("description"),
            "applications": obj.get("applications"),
            "grant": obj.get("grant"),
            "selectors": [SelectorDefinition.from_dict(_item) for _item in obj.get("selectors")] if obj.get("selectors") is not None else None,
            "var_for": [ForSpec.from_dict(_item) for _item in obj.get("for")] if obj.get("for") is not None else None,
            "var_if": [IfExpression.from_dict(_item) for _item in obj.get("if")] if obj.get("if") is not None else None,
            "when": WhenSpec.from_dict(obj.get("when")) if obj.get("when") is not None else None,
            "how": HowSpec.from_dict(obj.get("how")) if obj.get("how") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
