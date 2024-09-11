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





class Grant(str, Enum):
    """
    Grant
    """

    """
    allowed enum values
    """
    ALLOW = 'Allow'
    DENY = 'Deny'

    @classmethod
    def from_json(cls, json_str: str) -> Grant:
        """Create an instance of Grant from a JSON string"""
        return Grant(json.loads(json_str))
