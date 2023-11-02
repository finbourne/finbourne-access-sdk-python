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
from finbourne_access.models.link import Link
from finbourne_access.models.policy_collection_id import PolicyCollectionId
from finbourne_access.models.policy_id import PolicyId

class PolicyCollectionResponse(BaseModel):
    """
    A PolicyCollection encapsulating one or more Policies and PolicyCollections  # noqa: E501
    """
    id: Optional[PolicyCollectionId] = None
    policies: Optional[conlist(PolicyId)] = Field(None, description="The identifiers of the Policies in this collection")
    policy_collections: Optional[conlist(PolicyCollectionId)] = Field(None, alias="policyCollections", description="The identifiers of the PolicyCollections in this collection")
    description: Optional[StrictStr] = Field(None, description="A description of this policy collection")
    links: Optional[conlist(Link)] = None
    __properties = ["id", "policies", "policyCollections", "description", "links"]

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
    def from_json(cls, json_str: str) -> PolicyCollectionResponse:
        """Create an instance of PolicyCollectionResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in policies (list)
        _items = []
        if self.policies:
            for _item in self.policies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['policies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in policy_collections (list)
        _items = []
        if self.policy_collections:
            for _item in self.policy_collections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['policyCollections'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if policies (nullable) is None
        # and __fields_set__ contains the field
        if self.policies is None and "policies" in self.__fields_set__:
            _dict['policies'] = None

        # set to None if policy_collections (nullable) is None
        # and __fields_set__ contains the field
        if self.policy_collections is None and "policy_collections" in self.__fields_set__:
            _dict['policyCollections'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PolicyCollectionResponse:
        """Create an instance of PolicyCollectionResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PolicyCollectionResponse.parse_obj(obj)

        _obj = PolicyCollectionResponse.parse_obj({
            "id": PolicyCollectionId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "policies": [PolicyId.from_dict(_item) for _item in obj.get("policies")] if obj.get("policies") is not None else None,
            "policy_collections": [PolicyCollectionId.from_dict(_item) for _item in obj.get("policyCollections")] if obj.get("policyCollections") is not None else None,
            "description": obj.get("description"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
