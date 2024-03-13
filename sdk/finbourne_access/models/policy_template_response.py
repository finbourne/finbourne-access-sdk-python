# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.3737
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


class PolicyTemplateResponse(object):
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
        'display_name': 'str',
        'scope': 'str',
        'code': 'str',
        'description': 'str',
        'applications': 'list[str]',
        'tags': 'list[str]',
        'templated_selectors': 'list[PolicyTemplatedSelector]'
    }

    attribute_map = {
        'display_name': 'displayName',
        'scope': 'scope',
        'code': 'code',
        'description': 'description',
        'applications': 'applications',
        'tags': 'tags',
        'templated_selectors': 'templatedSelectors'
    }

    required_map = {
        'display_name': 'optional',
        'scope': 'optional',
        'code': 'optional',
        'description': 'optional',
        'applications': 'optional',
        'tags': 'optional',
        'templated_selectors': 'optional'
    }

    def __init__(self, display_name=None, scope=None, code=None, description=None, applications=None, tags=None, templated_selectors=None, local_vars_configuration=None):  # noqa: E501
        """PolicyTemplateResponse - a model defined in OpenAPI"
        
        :param display_name:  Display name of the policy template being created
        :type display_name: str
        :param scope:  The Scope of the policy template being created
        :type scope: str
        :param code:  The Code of the policy template being created
        :type code: str
        :param description:  Description of the policy template being created
        :type description: str
        :param applications:  List of applications that this policy template covers
        :type applications: list[str]
        :param tags:  List of policy types that this policy template covers
        :type tags: list[str]
        :param templated_selectors:  The selector definitions of policies included in this policy template
        :type templated_selectors: list[finbourne_access.PolicyTemplatedSelector]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._display_name = None
        self._scope = None
        self._code = None
        self._description = None
        self._applications = None
        self._tags = None
        self._templated_selectors = None
        self.discriminator = None

        self.display_name = display_name
        self.scope = scope
        self.code = code
        self.description = description
        self.applications = applications
        self.tags = tags
        self.templated_selectors = templated_selectors

    @property
    def display_name(self):
        """Gets the display_name of this PolicyTemplateResponse.  # noqa: E501

        Display name of the policy template being created  # noqa: E501

        :return: The display_name of this PolicyTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PolicyTemplateResponse.

        Display name of the policy template being created  # noqa: E501

        :param display_name: The display_name of this PolicyTemplateResponse.  # noqa: E501
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def scope(self):
        """Gets the scope of this PolicyTemplateResponse.  # noqa: E501

        The Scope of the policy template being created  # noqa: E501

        :return: The scope of this PolicyTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this PolicyTemplateResponse.

        The Scope of the policy template being created  # noqa: E501

        :param scope: The scope of this PolicyTemplateResponse.  # noqa: E501
        :type scope: str
        """

        self._scope = scope

    @property
    def code(self):
        """Gets the code of this PolicyTemplateResponse.  # noqa: E501

        The Code of the policy template being created  # noqa: E501

        :return: The code of this PolicyTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PolicyTemplateResponse.

        The Code of the policy template being created  # noqa: E501

        :param code: The code of this PolicyTemplateResponse.  # noqa: E501
        :type code: str
        """

        self._code = code

    @property
    def description(self):
        """Gets the description of this PolicyTemplateResponse.  # noqa: E501

        Description of the policy template being created  # noqa: E501

        :return: The description of this PolicyTemplateResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyTemplateResponse.

        Description of the policy template being created  # noqa: E501

        :param description: The description of this PolicyTemplateResponse.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def applications(self):
        """Gets the applications of this PolicyTemplateResponse.  # noqa: E501

        List of applications that this policy template covers  # noqa: E501

        :return: The applications of this PolicyTemplateResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this PolicyTemplateResponse.

        List of applications that this policy template covers  # noqa: E501

        :param applications: The applications of this PolicyTemplateResponse.  # noqa: E501
        :type applications: list[str]
        """

        self._applications = applications

    @property
    def tags(self):
        """Gets the tags of this PolicyTemplateResponse.  # noqa: E501

        List of policy types that this policy template covers  # noqa: E501

        :return: The tags of this PolicyTemplateResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this PolicyTemplateResponse.

        List of policy types that this policy template covers  # noqa: E501

        :param tags: The tags of this PolicyTemplateResponse.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def templated_selectors(self):
        """Gets the templated_selectors of this PolicyTemplateResponse.  # noqa: E501

        The selector definitions of policies included in this policy template  # noqa: E501

        :return: The templated_selectors of this PolicyTemplateResponse.  # noqa: E501
        :rtype: list[finbourne_access.PolicyTemplatedSelector]
        """
        return self._templated_selectors

    @templated_selectors.setter
    def templated_selectors(self, templated_selectors):
        """Sets the templated_selectors of this PolicyTemplateResponse.

        The selector definitions of policies included in this policy template  # noqa: E501

        :param templated_selectors: The templated_selectors of this PolicyTemplateResponse.  # noqa: E501
        :type templated_selectors: list[finbourne_access.PolicyTemplatedSelector]
        """

        self._templated_selectors = templated_selectors

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
        if not isinstance(other, PolicyTemplateResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyTemplateResponse):
            return True

        return self.to_dict() != other.to_dict()
