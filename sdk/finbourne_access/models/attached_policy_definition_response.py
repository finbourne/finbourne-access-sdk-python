# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1192
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class AttachedPolicyDefinitionResponse(object):
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
        'source_role': 'RoleId',
        'role_hierarchy_index': 'int',
        'description': 'str',
        'applications': 'list[str]',
        'policy_type': 'PolicyType',
        'id': 'PolicyId',
        'grant': 'Grant',
        'selectors': 'list[SelectorDefinition]',
        '_for': 'list[ForSpec]',
        '_if': 'list[IfExpression]',
        'when': 'WhenSpec',
        'how': 'HowSpec'
    }

    attribute_map = {
        'source_role': 'sourceRole',
        'role_hierarchy_index': 'roleHierarchyIndex',
        'description': 'description',
        'applications': 'applications',
        'policy_type': 'policyType',
        'id': 'id',
        'grant': 'grant',
        'selectors': 'selectors',
        '_for': 'for',
        '_if': 'if',
        'when': 'when',
        'how': 'how'
    }

    required_map = {
        'source_role': 'optional',
        'role_hierarchy_index': 'optional',
        'description': 'optional',
        'applications': 'optional',
        'policy_type': 'optional',
        'id': 'optional',
        'grant': 'optional',
        'selectors': 'optional',
        '_for': 'optional',
        '_if': 'optional',
        'when': 'optional',
        'how': 'optional'
    }

    def __init__(self, source_role=None, role_hierarchy_index=None, description=None, applications=None, policy_type=None, id=None, grant=None, selectors=None, _for=None, _if=None, when=None, how=None):  # noqa: E501
        """
        AttachedPolicyDefinitionResponse - a model defined in OpenAPI

        :param source_role: 
        :type source_role: finbourne_access.RoleId
        :param role_hierarchy_index: 
        :type role_hierarchy_index: int
        :param description: 
        :type description: str
        :param applications: 
        :type applications: list[str]
        :param policy_type: 
        :type policy_type: finbourne_access.PolicyType
        :param id: 
        :type id: finbourne_access.PolicyId
        :param grant: 
        :type grant: finbourne_access.Grant
        :param selectors: 
        :type selectors: list[finbourne_access.SelectorDefinition]
        :param _for: 
        :type _for: list[finbourne_access.ForSpec]
        :param _if: 
        :type _if: list[finbourne_access.IfExpression]
        :param when: 
        :type when: finbourne_access.WhenSpec
        :param how: 
        :type how: finbourne_access.HowSpec

        """  # noqa: E501

        self._source_role = None
        self._role_hierarchy_index = None
        self._description = None
        self._applications = None
        self._policy_type = None
        self._id = None
        self._grant = None
        self._selectors = None
        self.__for = None
        self.__if = None
        self._when = None
        self._how = None
        self.discriminator = None

        if source_role is not None:
            self.source_role = source_role
        if role_hierarchy_index is not None:
            self.role_hierarchy_index = role_hierarchy_index
        self.description = description
        self.applications = applications
        if policy_type is not None:
            self.policy_type = policy_type
        if id is not None:
            self.id = id
        if grant is not None:
            self.grant = grant
        self.selectors = selectors
        self._for = _for
        self._if = _if
        if when is not None:
            self.when = when
        if how is not None:
            self.how = how

    @property
    def source_role(self):
        """Gets the source_role of this AttachedPolicyDefinitionResponse.  # noqa: E501


        :return: The source_role of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :rtype: RoleId
        """
        return self._source_role

    @source_role.setter
    def source_role(self, source_role):
        """Sets the source_role of this AttachedPolicyDefinitionResponse.


        :param source_role: The source_role of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :type: RoleId
        """

        self._source_role = source_role

    @property
    def role_hierarchy_index(self):
        """Gets the role_hierarchy_index of this AttachedPolicyDefinitionResponse.  # noqa: E501


        :return: The role_hierarchy_index of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :rtype: int
        """
        return self._role_hierarchy_index

    @role_hierarchy_index.setter
    def role_hierarchy_index(self, role_hierarchy_index):
        """Sets the role_hierarchy_index of this AttachedPolicyDefinitionResponse.


        :param role_hierarchy_index: The role_hierarchy_index of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :type: int
        """

        self._role_hierarchy_index = role_hierarchy_index

    @property
    def description(self):
        """Gets the description of this AttachedPolicyDefinitionResponse.  # noqa: E501


        :return: The description of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AttachedPolicyDefinitionResponse.


        :param description: The description of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def applications(self):
        """Gets the applications of this AttachedPolicyDefinitionResponse.  # noqa: E501


        :return: The applications of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this AttachedPolicyDefinitionResponse.


        :param applications: The applications of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :type: list[str]
        """

        self._applications = applications

    @property
    def policy_type(self):
        """Gets the policy_type of this AttachedPolicyDefinitionResponse.  # noqa: E501


        :return: The policy_type of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :rtype: PolicyType
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """Sets the policy_type of this AttachedPolicyDefinitionResponse.


        :param policy_type: The policy_type of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :type: PolicyType
        """

        self._policy_type = policy_type

    @property
    def id(self):
        """Gets the id of this AttachedPolicyDefinitionResponse.  # noqa: E501


        :return: The id of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :rtype: PolicyId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AttachedPolicyDefinitionResponse.


        :param id: The id of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :type: PolicyId
        """

        self._id = id

    @property
    def grant(self):
        """Gets the grant of this AttachedPolicyDefinitionResponse.  # noqa: E501


        :return: The grant of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :rtype: Grant
        """
        return self._grant

    @grant.setter
    def grant(self, grant):
        """Sets the grant of this AttachedPolicyDefinitionResponse.


        :param grant: The grant of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :type: Grant
        """

        self._grant = grant

    @property
    def selectors(self):
        """Gets the selectors of this AttachedPolicyDefinitionResponse.  # noqa: E501


        :return: The selectors of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :rtype: list[SelectorDefinition]
        """
        return self._selectors

    @selectors.setter
    def selectors(self, selectors):
        """Sets the selectors of this AttachedPolicyDefinitionResponse.


        :param selectors: The selectors of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :type: list[SelectorDefinition]
        """

        self._selectors = selectors

    @property
    def _for(self):
        """Gets the _for of this AttachedPolicyDefinitionResponse.  # noqa: E501


        :return: The _for of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :rtype: list[ForSpec]
        """
        return self.__for

    @_for.setter
    def _for(self, _for):
        """Sets the _for of this AttachedPolicyDefinitionResponse.


        :param _for: The _for of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :type: list[ForSpec]
        """

        self.__for = _for

    @property
    def _if(self):
        """Gets the _if of this AttachedPolicyDefinitionResponse.  # noqa: E501


        :return: The _if of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :rtype: list[IfExpression]
        """
        return self.__if

    @_if.setter
    def _if(self, _if):
        """Sets the _if of this AttachedPolicyDefinitionResponse.


        :param _if: The _if of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :type: list[IfExpression]
        """

        self.__if = _if

    @property
    def when(self):
        """Gets the when of this AttachedPolicyDefinitionResponse.  # noqa: E501


        :return: The when of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :rtype: WhenSpec
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this AttachedPolicyDefinitionResponse.


        :param when: The when of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :type: WhenSpec
        """

        self._when = when

    @property
    def how(self):
        """Gets the how of this AttachedPolicyDefinitionResponse.  # noqa: E501


        :return: The how of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :rtype: HowSpec
        """
        return self._how

    @how.setter
    def how(self, how):
        """Sets the how of this AttachedPolicyDefinitionResponse.


        :param how: The how of this AttachedPolicyDefinitionResponse.  # noqa: E501
        :type: HowSpec
        """

        self._how = how

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
        if not isinstance(other, AttachedPolicyDefinitionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
