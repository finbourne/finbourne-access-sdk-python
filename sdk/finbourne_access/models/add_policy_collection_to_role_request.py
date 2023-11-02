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
from pydantic import BaseModel, Field, conlist
from finbourne_access.models.policy_collection_id import PolicyCollectionId

class AddPolicyCollectionToRoleRequest(BaseModel):
    """
    Request body used to add Policy Collections to a Role  # noqa: E501
    """
    policy_collections: conlist(PolicyCollectionId) = Field(..., alias="policyCollections", description="Identifiers of policy collections to add to a role")
    __properties = ["policyCollections"]

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
    def from_json(cls, json_str: str) -> AddPolicyCollectionToRoleRequest:
        """Create an instance of AddPolicyCollectionToRoleRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in policy_collections (list)
        _items = []
        if self.policy_collections:
            for _item in self.policy_collections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['policyCollections'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AddPolicyCollectionToRoleRequest:
        """Create an instance of AddPolicyCollectionToRoleRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AddPolicyCollectionToRoleRequest.parse_obj(obj)

        _obj = AddPolicyCollectionToRoleRequest.parse_obj({
            "policy_collections": [PolicyCollectionId.from_dict(_item) for _item in obj.get("policyCollections")] if obj.get("policyCollections") is not None else None
        })
        return _obj
