# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.3901
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


class TemplateMetadata(object):
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
        'template_selection': 'list[TemplateSelection]',
        'build_as_at': 'datetime'
    }

    attribute_map = {
        'template_selection': 'templateSelection',
        'build_as_at': 'buildAsAt'
    }

    required_map = {
        'template_selection': 'optional',
        'build_as_at': 'optional'
    }

    def __init__(self, template_selection=None, build_as_at=None, local_vars_configuration=None):  # noqa: E501
        """TemplateMetadata - a model defined in OpenAPI"
        
        :param template_selection:  List of policy templates used for a generation request
        :type template_selection: list[finbourne_access.TemplateSelection]
        :param build_as_at:  Policy template build AsAt time used for a generation request
        :type build_as_at: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._template_selection = None
        self._build_as_at = None
        self.discriminator = None

        self.template_selection = template_selection
        if build_as_at is not None:
            self.build_as_at = build_as_at

    @property
    def template_selection(self):
        """Gets the template_selection of this TemplateMetadata.  # noqa: E501

        List of policy templates used for a generation request  # noqa: E501

        :return: The template_selection of this TemplateMetadata.  # noqa: E501
        :rtype: list[finbourne_access.TemplateSelection]
        """
        return self._template_selection

    @template_selection.setter
    def template_selection(self, template_selection):
        """Sets the template_selection of this TemplateMetadata.

        List of policy templates used for a generation request  # noqa: E501

        :param template_selection: The template_selection of this TemplateMetadata.  # noqa: E501
        :type template_selection: list[finbourne_access.TemplateSelection]
        """

        self._template_selection = template_selection

    @property
    def build_as_at(self):
        """Gets the build_as_at of this TemplateMetadata.  # noqa: E501

        Policy template build AsAt time used for a generation request  # noqa: E501

        :return: The build_as_at of this TemplateMetadata.  # noqa: E501
        :rtype: datetime
        """
        return self._build_as_at

    @build_as_at.setter
    def build_as_at(self, build_as_at):
        """Sets the build_as_at of this TemplateMetadata.

        Policy template build AsAt time used for a generation request  # noqa: E501

        :param build_as_at: The build_as_at of this TemplateMetadata.  # noqa: E501
        :type build_as_at: datetime
        """

        self._build_as_at = build_as_at

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
        if not isinstance(other, TemplateMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateMetadata):
            return True

        return self.to_dict() != other.to_dict()
