# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.3618
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


class GeneratePolicyFromTemplateRequest(object):
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
        'template_selection': 'list[TemplateSelection]'
    }

    attribute_map = {
        'template_selection': 'templateSelection'
    }

    required_map = {
        'template_selection': 'required'
    }

    def __init__(self, template_selection=None, local_vars_configuration=None):  # noqa: E501
        """GeneratePolicyFromTemplateRequest - a model defined in OpenAPI"
        
        :param template_selection:  List of template selection, identifying policy templates to use for generation (required)
        :type template_selection: list[finbourne_access.TemplateSelection]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._template_selection = None
        self.discriminator = None

        self.template_selection = template_selection

    @property
    def template_selection(self):
        """Gets the template_selection of this GeneratePolicyFromTemplateRequest.  # noqa: E501

        List of template selection, identifying policy templates to use for generation  # noqa: E501

        :return: The template_selection of this GeneratePolicyFromTemplateRequest.  # noqa: E501
        :rtype: list[finbourne_access.TemplateSelection]
        """
        return self._template_selection

    @template_selection.setter
    def template_selection(self, template_selection):
        """Sets the template_selection of this GeneratePolicyFromTemplateRequest.

        List of template selection, identifying policy templates to use for generation  # noqa: E501

        :param template_selection: The template_selection of this GeneratePolicyFromTemplateRequest.  # noqa: E501
        :type template_selection: list[finbourne_access.TemplateSelection]
        """
        if self.local_vars_configuration.client_side_validation and template_selection is None:  # noqa: E501
            raise ValueError("Invalid value for `template_selection`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                template_selection is not None and len(template_selection) > 10):
            raise ValueError("Invalid value for `template_selection`, number of items must be less than or equal to `10`")  # noqa: E501

        self._template_selection = template_selection

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
        if not isinstance(other, GeneratePolicyFromTemplateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneratePolicyFromTemplateRequest):
            return True

        return self.to_dict() != other.to_dict()
