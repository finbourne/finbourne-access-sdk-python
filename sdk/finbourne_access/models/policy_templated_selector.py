# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.3829
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


class PolicyTemplatedSelector(object):
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
        'application': 'str',
        'tag': 'str',
        'selector': 'SelectorDefinition'
    }

    attribute_map = {
        'application': 'application',
        'tag': 'tag',
        'selector': 'selector'
    }

    required_map = {
        'application': 'required',
        'tag': 'required',
        'selector': 'required'
    }

    def __init__(self, application=None, tag=None, selector=None, local_vars_configuration=None):  # noqa: E501
        """PolicyTemplatedSelector - a model defined in OpenAPI"
        
        :param application:  The application that this selector definition applies to (required)
        :type application: str
        :param tag:  The type of policy that this selector definition applies to (required)
        :type tag: str
        :param selector:  (required)
        :type selector: finbourne_access.SelectorDefinition

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._application = None
        self._tag = None
        self._selector = None
        self.discriminator = None

        self.application = application
        self.tag = tag
        self.selector = selector

    @property
    def application(self):
        """Gets the application of this PolicyTemplatedSelector.  # noqa: E501

        The application that this selector definition applies to  # noqa: E501

        :return: The application of this PolicyTemplatedSelector.  # noqa: E501
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """Sets the application of this PolicyTemplatedSelector.

        The application that this selector definition applies to  # noqa: E501

        :param application: The application of this PolicyTemplatedSelector.  # noqa: E501
        :type application: str
        """
        if self.local_vars_configuration.client_side_validation and application is None:  # noqa: E501
            raise ValueError("Invalid value for `application`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                application is not None and len(application) < 1):
            raise ValueError("Invalid value for `application`, length must be greater than or equal to `1`")  # noqa: E501

        self._application = application

    @property
    def tag(self):
        """Gets the tag of this PolicyTemplatedSelector.  # noqa: E501

        The type of policy that this selector definition applies to  # noqa: E501

        :return: The tag of this PolicyTemplatedSelector.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this PolicyTemplatedSelector.

        The type of policy that this selector definition applies to  # noqa: E501

        :param tag: The tag of this PolicyTemplatedSelector.  # noqa: E501
        :type tag: str
        """
        if self.local_vars_configuration.client_side_validation and tag is None:  # noqa: E501
            raise ValueError("Invalid value for `tag`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                tag is not None and len(tag) < 1):
            raise ValueError("Invalid value for `tag`, length must be greater than or equal to `1`")  # noqa: E501

        self._tag = tag

    @property
    def selector(self):
        """Gets the selector of this PolicyTemplatedSelector.  # noqa: E501


        :return: The selector of this PolicyTemplatedSelector.  # noqa: E501
        :rtype: finbourne_access.SelectorDefinition
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this PolicyTemplatedSelector.


        :param selector: The selector of this PolicyTemplatedSelector.  # noqa: E501
        :type selector: finbourne_access.SelectorDefinition
        """
        if self.local_vars_configuration.client_side_validation and selector is None:  # noqa: E501
            raise ValueError("Invalid value for `selector`, must not be `None`")  # noqa: E501

        self._selector = selector

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
        if not isinstance(other, PolicyTemplatedSelector):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyTemplatedSelector):
            return True

        return self.to_dict() != other.to_dict()
