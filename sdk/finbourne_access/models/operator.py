# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class Operator(str, Enum):
    """
    Operator
    """

    """
    allowed enum values
    """
    UNDEFINED = 'Undefined'
    EQUALS = 'Equals'
    NOTEQUALS = 'NotEquals'
    GREATERTHAN = 'GreaterThan'
    GREATERTHANOREQUALTO = 'GreaterThanOrEqualTo'
    LESSTHAN = 'LessThan'
    LESSTHANOREQUALTO = 'LessThanOrEqualTo'
    IN = 'In'

    @classmethod
    def from_json(cls, json_str: str) -> Operator:
        """Create an instance of Operator from a JSON string"""
        return Operator(json.loads(json_str))
