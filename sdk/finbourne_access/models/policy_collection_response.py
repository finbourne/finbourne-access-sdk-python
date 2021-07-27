# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1282
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class PolicyCollectionResponse(object):
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
        'id': 'PolicyCollectionId',
        'policies': 'list[PolicyId]',
        'policy_collections': 'list[PolicyCollectionId]',
        'description': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'policies': 'policies',
        'policy_collections': 'policyCollections',
        'description': 'description',
        'links': 'links'
    }

    required_map = {
        'id': 'optional',
        'policies': 'optional',
        'policy_collections': 'optional',
        'description': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, policies=None, policy_collections=None, description=None, links=None):  # noqa: E501
        """
        PolicyCollectionResponse - a model defined in OpenAPI

        :param id: 
        :type id: finbourne_access.PolicyCollectionId
        :param policies:  The identifiers of the Policies in this collection
        :type policies: list[finbourne_access.PolicyId]
        :param policy_collections:  The identifiers of the PolicyCollections in this collection
        :type policy_collections: list[finbourne_access.PolicyCollectionId]
        :param description:  A description of this policy collection
        :type description: str
        :param links: 
        :type links: list[finbourne_access.Link]

        """  # noqa: E501

        self._id = None
        self._policies = None
        self._policy_collections = None
        self._description = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.policies = policies
        self.policy_collections = policy_collections
        self.description = description
        self.links = links

    @property
    def id(self):
        """Gets the id of this PolicyCollectionResponse.  # noqa: E501


        :return: The id of this PolicyCollectionResponse.  # noqa: E501
        :rtype: PolicyCollectionId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PolicyCollectionResponse.


        :param id: The id of this PolicyCollectionResponse.  # noqa: E501
        :type: PolicyCollectionId
        """

        self._id = id

    @property
    def policies(self):
        """Gets the policies of this PolicyCollectionResponse.  # noqa: E501

        The identifiers of the Policies in this collection  # noqa: E501

        :return: The policies of this PolicyCollectionResponse.  # noqa: E501
        :rtype: list[PolicyId]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this PolicyCollectionResponse.

        The identifiers of the Policies in this collection  # noqa: E501

        :param policies: The policies of this PolicyCollectionResponse.  # noqa: E501
        :type: list[PolicyId]
        """

        self._policies = policies

    @property
    def policy_collections(self):
        """Gets the policy_collections of this PolicyCollectionResponse.  # noqa: E501

        The identifiers of the PolicyCollections in this collection  # noqa: E501

        :return: The policy_collections of this PolicyCollectionResponse.  # noqa: E501
        :rtype: list[PolicyCollectionId]
        """
        return self._policy_collections

    @policy_collections.setter
    def policy_collections(self, policy_collections):
        """Sets the policy_collections of this PolicyCollectionResponse.

        The identifiers of the PolicyCollections in this collection  # noqa: E501

        :param policy_collections: The policy_collections of this PolicyCollectionResponse.  # noqa: E501
        :type: list[PolicyCollectionId]
        """

        self._policy_collections = policy_collections

    @property
    def description(self):
        """Gets the description of this PolicyCollectionResponse.  # noqa: E501

        A description of this policy collection  # noqa: E501

        :return: The description of this PolicyCollectionResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyCollectionResponse.

        A description of this policy collection  # noqa: E501

        :param description: The description of this PolicyCollectionResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def links(self):
        """Gets the links of this PolicyCollectionResponse.  # noqa: E501


        :return: The links of this PolicyCollectionResponse.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PolicyCollectionResponse.


        :param links: The links of this PolicyCollectionResponse.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if not isinstance(other, PolicyCollectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
