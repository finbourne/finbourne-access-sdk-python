# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2718
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


class RoleResourceRequest(object):
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
        'non_transitive_supervisor_role_resource': 'NonTransitiveSupervisorRoleResource',
        'policy_id_role_resource': 'PolicyIdRoleResource'
    }

    attribute_map = {
        'non_transitive_supervisor_role_resource': 'nonTransitiveSupervisorRoleResource',
        'policy_id_role_resource': 'policyIdRoleResource'
    }

    required_map = {
        'non_transitive_supervisor_role_resource': 'optional',
        'policy_id_role_resource': 'optional'
    }

    def __init__(self, non_transitive_supervisor_role_resource=None, policy_id_role_resource=None, local_vars_configuration=None):  # noqa: E501
        """RoleResourceRequest - a model defined in OpenAPI"
        
        :param non_transitive_supervisor_role_resource: 
        :type non_transitive_supervisor_role_resource: finbourne_access.NonTransitiveSupervisorRoleResource
        :param policy_id_role_resource: 
        :type policy_id_role_resource: finbourne_access.PolicyIdRoleResource

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._non_transitive_supervisor_role_resource = None
        self._policy_id_role_resource = None
        self.discriminator = None

        if non_transitive_supervisor_role_resource is not None:
            self.non_transitive_supervisor_role_resource = non_transitive_supervisor_role_resource
        if policy_id_role_resource is not None:
            self.policy_id_role_resource = policy_id_role_resource

    @property
    def non_transitive_supervisor_role_resource(self):
        """Gets the non_transitive_supervisor_role_resource of this RoleResourceRequest.  # noqa: E501


        :return: The non_transitive_supervisor_role_resource of this RoleResourceRequest.  # noqa: E501
        :rtype: finbourne_access.NonTransitiveSupervisorRoleResource
        """
        return self._non_transitive_supervisor_role_resource

    @non_transitive_supervisor_role_resource.setter
    def non_transitive_supervisor_role_resource(self, non_transitive_supervisor_role_resource):
        """Sets the non_transitive_supervisor_role_resource of this RoleResourceRequest.


        :param non_transitive_supervisor_role_resource: The non_transitive_supervisor_role_resource of this RoleResourceRequest.  # noqa: E501
        :type non_transitive_supervisor_role_resource: finbourne_access.NonTransitiveSupervisorRoleResource
        """

        self._non_transitive_supervisor_role_resource = non_transitive_supervisor_role_resource

    @property
    def policy_id_role_resource(self):
        """Gets the policy_id_role_resource of this RoleResourceRequest.  # noqa: E501


        :return: The policy_id_role_resource of this RoleResourceRequest.  # noqa: E501
        :rtype: finbourne_access.PolicyIdRoleResource
        """
        return self._policy_id_role_resource

    @policy_id_role_resource.setter
    def policy_id_role_resource(self, policy_id_role_resource):
        """Sets the policy_id_role_resource of this RoleResourceRequest.


        :param policy_id_role_resource: The policy_id_role_resource of this RoleResourceRequest.  # noqa: E501
        :type policy_id_role_resource: finbourne_access.PolicyIdRoleResource
        """

        self._policy_id_role_resource = policy_id_role_resource

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
        if not isinstance(other, RoleResourceRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleResourceRequest):
            return True

        return self.to_dict() != other.to_dict()
