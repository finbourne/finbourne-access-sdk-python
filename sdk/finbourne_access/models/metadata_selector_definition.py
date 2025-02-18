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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, conlist, constr 
from finbourne_access.models.action_id import ActionId
from finbourne_access.models.metadata_expression import MetadataExpression

class MetadataSelectorDefinition(BaseModel):
    """
    MetadataSelectorDefinition
    """
    expressions: conlist(MetadataExpression, min_items=1) = Field(...)
    actions: conlist(ActionId, min_items=1) = Field(...)
    name:  Optional[StrictStr] = Field(None,alias="name") 
    description:  Optional[StrictStr] = Field(None,alias="description") 
    __properties = ["expressions", "actions", "name", "description"]

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
    def from_json(cls, json_str: str) -> MetadataSelectorDefinition:
        """Create an instance of MetadataSelectorDefinition from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in expressions (list)
        _items = []
        if self.expressions:
            for _item in self.expressions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['expressions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in actions (list)
        _items = []
        if self.actions:
            for _item in self.actions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['actions'] = _items
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MetadataSelectorDefinition:
        """Create an instance of MetadataSelectorDefinition from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MetadataSelectorDefinition.parse_obj(obj)

        _obj = MetadataSelectorDefinition.parse_obj({
            "expressions": [MetadataExpression.from_dict(_item) for _item in obj.get("expressions")] if obj.get("expressions") is not None else None,
            "actions": [ActionId.from_dict(_item) for _item in obj.get("actions")] if obj.get("actions") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description")
        })
        return _obj
