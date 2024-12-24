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


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr
from finbourne_access.models.evaluation_result import EvaluationResult

class EvaluationResponse(BaseModel):
    """
    The result of an evaluation request  # noqa: E501
    """
    result: EvaluationResult = Field(...)
    detailed_message: Optional[StrictStr] = Field(None, alias="detailedMessage", description="In the case of the evaluation being denied a message may be returned")
    __properties = ["result", "detailedMessage"]

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
    def from_json(cls, json_str: str) -> EvaluationResponse:
        """Create an instance of EvaluationResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if detailed_message (nullable) is None
        # and __fields_set__ contains the field
        if self.detailed_message is None and "detailed_message" in self.__fields_set__:
            _dict['detailedMessage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EvaluationResponse:
        """Create an instance of EvaluationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EvaluationResponse.parse_obj(obj)

        _obj = EvaluationResponse.parse_obj({
            "result": obj.get("result"),
            "detailed_message": obj.get("detailedMessage")
        })
        return _obj
