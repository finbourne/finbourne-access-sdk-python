# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1192
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class LicenceSelectorDefinition(object):
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
        'code': 'str',
        'action_ids': 'list[ActionId]',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'code': 'code',
        'action_ids': 'actionIds',
        'name': 'name',
        'description': 'description'
    }

    required_map = {
        'code': 'required',
        'action_ids': 'required',
        'name': 'optional',
        'description': 'optional'
    }

    def __init__(self, code=None, action_ids=None, name=None, description=None):  # noqa: E501
        """
        LicenceSelectorDefinition - a model defined in OpenAPI

        :param code:  The code of the licence (required)
        :type code: str
        :param action_ids:  (required)
        :type action_ids: list[finbourne_access.ActionId]
        :param name:  The name of this selector within the licence (for reporting and diagnostic purposes)
        :type name: str
        :param description:  A description of the point of this selector within this licence
        :type description: str

        """  # noqa: E501

        self._code = None
        self._action_ids = None
        self._name = None
        self._description = None
        self.discriminator = None

        self.code = code
        self.action_ids = action_ids
        self.name = name
        self.description = description

    @property
    def code(self):
        """Gets the code of this LicenceSelectorDefinition.  # noqa: E501

        The code of the licence  # noqa: E501

        :return: The code of this LicenceSelectorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LicenceSelectorDefinition.

        The code of the licence  # noqa: E501

        :param code: The code of this LicenceSelectorDefinition.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def action_ids(self):
        """Gets the action_ids of this LicenceSelectorDefinition.  # noqa: E501


        :return: The action_ids of this LicenceSelectorDefinition.  # noqa: E501
        :rtype: list[ActionId]
        """
        return self._action_ids

    @action_ids.setter
    def action_ids(self, action_ids):
        """Sets the action_ids of this LicenceSelectorDefinition.


        :param action_ids: The action_ids of this LicenceSelectorDefinition.  # noqa: E501
        :type: list[ActionId]
        """
        if action_ids is None:
            raise ValueError("Invalid value for `action_ids`, must not be `None`")  # noqa: E501

        self._action_ids = action_ids

    @property
    def name(self):
        """Gets the name of this LicenceSelectorDefinition.  # noqa: E501

        The name of this selector within the licence (for reporting and diagnostic purposes)  # noqa: E501

        :return: The name of this LicenceSelectorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LicenceSelectorDefinition.

        The name of this selector within the licence (for reporting and diagnostic purposes)  # noqa: E501

        :param name: The name of this LicenceSelectorDefinition.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this LicenceSelectorDefinition.  # noqa: E501

        A description of the point of this selector within this licence  # noqa: E501

        :return: The description of this LicenceSelectorDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LicenceSelectorDefinition.

        A description of the point of this selector within this licence  # noqa: E501

        :param description: The description of this LicenceSelectorDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if not isinstance(other, LicenceSelectorDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
