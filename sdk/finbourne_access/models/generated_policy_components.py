# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.3772
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


class GeneratedPolicyComponents(object):
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
        'applications': 'list[str]',
        'template_metadata': 'TemplateMetadata',
        'selectors': 'list[SelectorDefinition]'
    }

    attribute_map = {
        'applications': 'applications',
        'template_metadata': 'templateMetadata',
        'selectors': 'selectors'
    }

    required_map = {
        'applications': 'optional',
        'template_metadata': 'optional',
        'selectors': 'optional'
    }

    def __init__(self, applications=None, template_metadata=None, selectors=None, local_vars_configuration=None):  # noqa: E501
        """GeneratedPolicyComponents - a model defined in OpenAPI"
        
        :param applications:  Applications to which the policy applies
        :type applications: list[str]
        :param template_metadata: 
        :type template_metadata: finbourne_access.TemplateMetadata
        :param selectors:  Selectors that this policy will be applied to
        :type selectors: list[finbourne_access.SelectorDefinition]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._applications = None
        self._template_metadata = None
        self._selectors = None
        self.discriminator = None

        self.applications = applications
        if template_metadata is not None:
            self.template_metadata = template_metadata
        self.selectors = selectors

    @property
    def applications(self):
        """Gets the applications of this GeneratedPolicyComponents.  # noqa: E501

        Applications to which the policy applies  # noqa: E501

        :return: The applications of this GeneratedPolicyComponents.  # noqa: E501
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this GeneratedPolicyComponents.

        Applications to which the policy applies  # noqa: E501

        :param applications: The applications of this GeneratedPolicyComponents.  # noqa: E501
        :type applications: list[str]
        """

        self._applications = applications

    @property
    def template_metadata(self):
        """Gets the template_metadata of this GeneratedPolicyComponents.  # noqa: E501


        :return: The template_metadata of this GeneratedPolicyComponents.  # noqa: E501
        :rtype: finbourne_access.TemplateMetadata
        """
        return self._template_metadata

    @template_metadata.setter
    def template_metadata(self, template_metadata):
        """Sets the template_metadata of this GeneratedPolicyComponents.


        :param template_metadata: The template_metadata of this GeneratedPolicyComponents.  # noqa: E501
        :type template_metadata: finbourne_access.TemplateMetadata
        """

        self._template_metadata = template_metadata

    @property
    def selectors(self):
        """Gets the selectors of this GeneratedPolicyComponents.  # noqa: E501

        Selectors that this policy will be applied to  # noqa: E501

        :return: The selectors of this GeneratedPolicyComponents.  # noqa: E501
        :rtype: list[finbourne_access.SelectorDefinition]
        """
        return self._selectors

    @selectors.setter
    def selectors(self, selectors):
        """Sets the selectors of this GeneratedPolicyComponents.

        Selectors that this policy will be applied to  # noqa: E501

        :param selectors: The selectors of this GeneratedPolicyComponents.  # noqa: E501
        :type selectors: list[finbourne_access.SelectorDefinition]
        """

        self._selectors = selectors

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
        if not isinstance(other, GeneratedPolicyComponents):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeneratedPolicyComponents):
            return True

        return self.to_dict() != other.to_dict()
