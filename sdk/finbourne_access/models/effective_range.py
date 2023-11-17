# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.3462
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


class EffectiveRange(object):
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
        '_from': 'datetime',
        'to': 'datetime'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to'
    }

    required_map = {
        '_from': 'optional',
        'to': 'optional'
    }

    def __init__(self, _from=None, to=None, local_vars_configuration=None):  # noqa: E501
        """EffectiveRange - a model defined in OpenAPI"
        
        :param _from: 
        :type _from: datetime
        :param to: 
        :type to: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self.__from = None
        self._to = None
        self.discriminator = None

        if _from is not None:
            self._from = _from
        self.to = to

    @property
    def _from(self):
        """Gets the _from of this EffectiveRange.  # noqa: E501


        :return: The _from of this EffectiveRange.  # noqa: E501
        :rtype: datetime
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this EffectiveRange.


        :param _from: The _from of this EffectiveRange.  # noqa: E501
        :type _from: datetime
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this EffectiveRange.  # noqa: E501


        :return: The to of this EffectiveRange.  # noqa: E501
        :rtype: datetime
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this EffectiveRange.


        :param to: The to of this EffectiveRange.  # noqa: E501
        :type to: datetime
        """

        self._to = to

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
        if not isinstance(other, EffectiveRange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EffectiveRange):
            return True

        return self.to_dict() != other.to_dict()
