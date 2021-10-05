# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1430
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from finbourne_access.configuration import Configuration


class WhenSpec(object):
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
        'activate': 'datetime',
        'deactivate': 'datetime'
    }

    attribute_map = {
        'activate': 'activate',
        'deactivate': 'deactivate'
    }

    required_map = {
        'activate': 'required',
        'deactivate': 'optional'
    }

    def __init__(self, activate=None, deactivate=None, local_vars_configuration=None):  # noqa: E501
        """WhenSpec - a model defined in OpenAPI"
        
        :param activate:  (required)
        :type activate: datetime
        :param deactivate: 
        :type deactivate: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._activate = None
        self._deactivate = None
        self.discriminator = None

        self.activate = activate
        self.deactivate = deactivate

    @property
    def activate(self):
        """Gets the activate of this WhenSpec.  # noqa: E501


        :return: The activate of this WhenSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._activate

    @activate.setter
    def activate(self, activate):
        """Sets the activate of this WhenSpec.


        :param activate: The activate of this WhenSpec.  # noqa: E501
        :type activate: datetime
        """
        if self.local_vars_configuration.client_side_validation and activate is None:  # noqa: E501
            raise ValueError("Invalid value for `activate`, must not be `None`")  # noqa: E501

        self._activate = activate

    @property
    def deactivate(self):
        """Gets the deactivate of this WhenSpec.  # noqa: E501


        :return: The deactivate of this WhenSpec.  # noqa: E501
        :rtype: datetime
        """
        return self._deactivate

    @deactivate.setter
    def deactivate(self, deactivate):
        """Sets the deactivate of this WhenSpec.


        :param deactivate: The deactivate of this WhenSpec.  # noqa: E501
        :type deactivate: datetime
        """

        self._deactivate = deactivate

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WhenSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WhenSpec):
            return True

        return self.to_dict() != other.to_dict()
