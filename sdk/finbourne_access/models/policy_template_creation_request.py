# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.3752
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


class PolicyTemplateCreationRequest(object):
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
        'display_name': 'str',
        'description': 'str',
        'templated_selectors': 'list[PolicyTemplatedSelector]'
    }

    attribute_map = {
        'code': 'code',
        'display_name': 'displayName',
        'description': 'description',
        'templated_selectors': 'templatedSelectors'
    }

    required_map = {
        'code': 'required',
        'display_name': 'required',
        'description': 'required',
        'templated_selectors': 'required'
    }

    def __init__(self, code=None, display_name=None, description=None, templated_selectors=None, local_vars_configuration=None):  # noqa: E501
        """PolicyTemplateCreationRequest - a model defined in OpenAPI"
        
        :param code:  The Code of the policy template being created (required)
        :type code: str
        :param display_name:  The display name of the policy template being created (required)
        :type display_name: str
        :param description:  Description of the policy template being craeted (required)
        :type description: str
        :param templated_selectors:  The selector definitions of policies included in this policy template (required)
        :type templated_selectors: list[finbourne_access.PolicyTemplatedSelector]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._display_name = None
        self._description = None
        self._templated_selectors = None
        self.discriminator = None

        self.code = code
        self.display_name = display_name
        self.description = description
        self.templated_selectors = templated_selectors

    @property
    def code(self):
        """Gets the code of this PolicyTemplateCreationRequest.  # noqa: E501

        The Code of the policy template being created  # noqa: E501

        :return: The code of this PolicyTemplateCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PolicyTemplateCreationRequest.

        The Code of the policy template being created  # noqa: E501

        :param code: The code of this PolicyTemplateCreationRequest.  # noqa: E501
        :type code: str
        """
        if self.local_vars_configuration.client_side_validation and code is None:  # noqa: E501
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) > 100):
            raise ValueError("Invalid value for `code`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and len(code) < 3):
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `3`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                code is not None and not re.search(r'^(?=.*[a-zA-Z])[\w][\w +-]{2,100}$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^(?=.*[a-zA-Z])[\w][\w +-]{2,100}$/`")  # noqa: E501

        self._code = code

    @property
    def display_name(self):
        """Gets the display_name of this PolicyTemplateCreationRequest.  # noqa: E501

        The display name of the policy template being created  # noqa: E501

        :return: The display_name of this PolicyTemplateCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PolicyTemplateCreationRequest.

        The display name of the policy template being created  # noqa: E501

        :param display_name: The display_name of this PolicyTemplateCreationRequest.  # noqa: E501
        :type display_name: str
        """
        if self.local_vars_configuration.client_side_validation and display_name is None:  # noqa: E501
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) > 512):
            raise ValueError("Invalid value for `display_name`, length must be less than or equal to `512`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                display_name is not None and len(display_name) < 1):
            raise ValueError("Invalid value for `display_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this PolicyTemplateCreationRequest.  # noqa: E501

        Description of the policy template being craeted  # noqa: E501

        :return: The description of this PolicyTemplateCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyTemplateCreationRequest.

        Description of the policy template being craeted  # noqa: E501

        :param description: The description of this PolicyTemplateCreationRequest.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def templated_selectors(self):
        """Gets the templated_selectors of this PolicyTemplateCreationRequest.  # noqa: E501

        The selector definitions of policies included in this policy template  # noqa: E501

        :return: The templated_selectors of this PolicyTemplateCreationRequest.  # noqa: E501
        :rtype: list[finbourne_access.PolicyTemplatedSelector]
        """
        return self._templated_selectors

    @templated_selectors.setter
    def templated_selectors(self, templated_selectors):
        """Sets the templated_selectors of this PolicyTemplateCreationRequest.

        The selector definitions of policies included in this policy template  # noqa: E501

        :param templated_selectors: The templated_selectors of this PolicyTemplateCreationRequest.  # noqa: E501
        :type templated_selectors: list[finbourne_access.PolicyTemplatedSelector]
        """
        if self.local_vars_configuration.client_side_validation and templated_selectors is None:  # noqa: E501
            raise ValueError("Invalid value for `templated_selectors`, must not be `None`")  # noqa: E501

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
        if not isinstance(other, PolicyTemplateCreationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyTemplateCreationRequest):
            return True

        return self.to_dict() != other.to_dict()
