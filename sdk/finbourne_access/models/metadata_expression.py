# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1196
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class MetadataExpression(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'metadata_key': 'str',
        'operator': 'Operator',
        'text_value': 'str'
    }

    attribute_map = {
        'metadata_key': 'metadataKey',
        'operator': 'operator',
        'text_value': 'textValue'
    }

    required_map = {
        'metadata_key': 'required',
        'operator': 'required',
        'text_value': 'optional'
    }

    def __init__(self, metadata_key=None, operator=None, text_value=None):  # noqa: E501
        """
        MetadataExpression - a model defined in OpenAPI

        :param metadata_key:  (required)
        :type metadata_key: str
        :param operator:  (required)
        :type operator: finbourne_access.Operator
        :param text_value: 
        :type text_value: str

        """  # noqa: E501

        self._metadata_key = None
        self._operator = None
        self._text_value = None
        self.discriminator = None

        self.metadata_key = metadata_key
        self.operator = operator
        self.text_value = text_value

    @property
    def metadata_key(self):
        """Gets the metadata_key of this MetadataExpression.  # noqa: E501


        :return: The metadata_key of this MetadataExpression.  # noqa: E501
        :rtype: str
        """
        return self._metadata_key

    @metadata_key.setter
    def metadata_key(self, metadata_key):
        """Sets the metadata_key of this MetadataExpression.


        :param metadata_key: The metadata_key of this MetadataExpression.  # noqa: E501
        :type: str
        """
        if metadata_key is None:
            raise ValueError("Invalid value for `metadata_key`, must not be `None`")  # noqa: E501
        if metadata_key is not None and len(metadata_key) < 1:
            raise ValueError("Invalid value for `metadata_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._metadata_key = metadata_key

    @property
    def operator(self):
        """Gets the operator of this MetadataExpression.  # noqa: E501


        :return: The operator of this MetadataExpression.  # noqa: E501
        :rtype: Operator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this MetadataExpression.


        :param operator: The operator of this MetadataExpression.  # noqa: E501
        :type: Operator
        """
        if operator is None:
            raise ValueError("Invalid value for `operator`, must not be `None`")  # noqa: E501

        self._operator = operator

    @property
    def text_value(self):
        """Gets the text_value of this MetadataExpression.  # noqa: E501


        :return: The text_value of this MetadataExpression.  # noqa: E501
        :rtype: str
        """
        return self._text_value

    @text_value.setter
    def text_value(self, text_value):
        """Sets the text_value of this MetadataExpression.


        :param text_value: The text_value of this MetadataExpression.  # noqa: E501
        :type: str
        """

        self._text_value = text_value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MetadataExpression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
