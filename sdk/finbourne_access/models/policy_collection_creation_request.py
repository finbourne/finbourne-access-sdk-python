# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.3482
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


class PolicyCollectionCreationRequest(object):
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
        'policies': 'list[PolicyId]',
        'metadata': 'dict(str, list[EntitlementMetadata])',
        'policy_collections': 'list[PolicyCollectionId]',
        'description': 'str'
    }

    attribute_map = {
        'code': 'code',
        'policies': 'policies',
        'metadata': 'metadata',
        'policy_collections': 'policyCollections',
        'description': 'description'
    }

    required_map = {
        'code': 'required',
        'policies': 'optional',
        'metadata': 'optional',
        'policy_collections': 'optional',
        'description': 'optional'
    }

    def __init__(self, code=None, policies=None, metadata=None, policy_collections=None, description=None, local_vars_configuration=None):  # noqa: E501
        """PolicyCollectionCreationRequest - a model defined in OpenAPI"
        
        :param code:  The identifier for the PolicyCollection being created (required)
        :type code: str
        :param policies:  The identifiers of the Policies in this collection
        :type policies: list[finbourne_access.PolicyId]
        :param metadata:  Any relevant metadata associated with this resource for controlling access to this resource
        :type metadata: dict(str, list[EntitlementMetadata])
        :param policy_collections:  The identifiers of the PolicyCollections in this collection
        :type policy_collections: list[finbourne_access.PolicyCollectionId]
        :param description:  A description of this policy collection
        :type description: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._policies = None
        self._metadata = None
        self._policy_collections = None
        self._description = None
        self.discriminator = None

        self.code = code
        self.policies = policies
        self.metadata = metadata
        self.policy_collections = policy_collections
        self.description = description

    @property
    def code(self):
        """Gets the code of this PolicyCollectionCreationRequest.  # noqa: E501

        The identifier for the PolicyCollection being created  # noqa: E501

        :return: The code of this PolicyCollectionCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PolicyCollectionCreationRequest.

        The identifier for the PolicyCollection being created  # noqa: E501

        :param code: The code of this PolicyCollectionCreationRequest.  # noqa: E501
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
    def policies(self):
        """Gets the policies of this PolicyCollectionCreationRequest.  # noqa: E501

        The identifiers of the Policies in this collection  # noqa: E501

        :return: The policies of this PolicyCollectionCreationRequest.  # noqa: E501
        :rtype: list[finbourne_access.PolicyId]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this PolicyCollectionCreationRequest.

        The identifiers of the Policies in this collection  # noqa: E501

        :param policies: The policies of this PolicyCollectionCreationRequest.  # noqa: E501
        :type policies: list[finbourne_access.PolicyId]
        """

        self._policies = policies

    @property
    def metadata(self):
        """Gets the metadata of this PolicyCollectionCreationRequest.  # noqa: E501

        Any relevant metadata associated with this resource for controlling access to this resource  # noqa: E501

        :return: The metadata of this PolicyCollectionCreationRequest.  # noqa: E501
        :rtype: dict(str, list[EntitlementMetadata])
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PolicyCollectionCreationRequest.

        Any relevant metadata associated with this resource for controlling access to this resource  # noqa: E501

        :param metadata: The metadata of this PolicyCollectionCreationRequest.  # noqa: E501
        :type metadata: dict(str, list[EntitlementMetadata])
        """

        self._metadata = metadata

    @property
    def policy_collections(self):
        """Gets the policy_collections of this PolicyCollectionCreationRequest.  # noqa: E501

        The identifiers of the PolicyCollections in this collection  # noqa: E501

        :return: The policy_collections of this PolicyCollectionCreationRequest.  # noqa: E501
        :rtype: list[finbourne_access.PolicyCollectionId]
        """
        return self._policy_collections

    @policy_collections.setter
    def policy_collections(self, policy_collections):
        """Sets the policy_collections of this PolicyCollectionCreationRequest.

        The identifiers of the PolicyCollections in this collection  # noqa: E501

        :param policy_collections: The policy_collections of this PolicyCollectionCreationRequest.  # noqa: E501
        :type policy_collections: list[finbourne_access.PolicyCollectionId]
        """

        self._policy_collections = policy_collections

    @property
    def description(self):
        """Gets the description of this PolicyCollectionCreationRequest.  # noqa: E501

        A description of this policy collection  # noqa: E501

        :return: The description of this PolicyCollectionCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyCollectionCreationRequest.

        A description of this policy collection  # noqa: E501

        :param description: The description of this PolicyCollectionCreationRequest.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1024):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

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
        if not isinstance(other, PolicyCollectionCreationRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyCollectionCreationRequest):
            return True

        return self.to_dict() != other.to_dict()
