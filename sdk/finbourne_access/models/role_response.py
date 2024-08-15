# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.3910
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


class RoleResponse(object):
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
        'id': 'RoleId',
        'role_hierarchy_index': 'int',
        'description': 'str',
        'resource': 'RoleResourceRequest',
        'when': 'WhenSpec',
        'permission': 'str',
        'limit': 'dict(str, str)',
        'links': 'list[Link]'
    }

    attribute_map = {
        'id': 'id',
        'role_hierarchy_index': 'roleHierarchyIndex',
        'description': 'description',
        'resource': 'resource',
        'when': 'when',
        'permission': 'permission',
        'limit': 'limit',
        'links': 'links'
    }

    required_map = {
        'id': 'required',
        'role_hierarchy_index': 'required',
        'description': 'optional',
        'resource': 'required',
        'when': 'required',
        'permission': 'required',
        'limit': 'optional',
        'links': 'optional'
    }

    def __init__(self, id=None, role_hierarchy_index=None, description=None, resource=None, when=None, permission=None, limit=None, links=None, local_vars_configuration=None):  # noqa: E501
        """RoleResponse - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: finbourne_access.RoleId
        :param role_hierarchy_index:  The hierarchical index of the role (required)
        :type role_hierarchy_index: int
        :param description:  The description of the role
        :type description: str
        :param resource:  (required)
        :type resource: finbourne_access.RoleResourceRequest
        :param when:  (required)
        :type when: finbourne_access.WhenSpec
        :param permission:  The action key of the role (required)
        :type permission: str
        :param limit:  The identifiers of the role with the maximum privileges that this role can have
        :type limit: dict(str, str)
        :param links: 
        :type links: list[finbourne_access.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._role_hierarchy_index = None
        self._description = None
        self._resource = None
        self._when = None
        self._permission = None
        self._limit = None
        self._links = None
        self.discriminator = None

        self.id = id
        self.role_hierarchy_index = role_hierarchy_index
        self.description = description
        self.resource = resource
        self.when = when
        self.permission = permission
        self.limit = limit
        self.links = links

    @property
    def id(self):
        """Gets the id of this RoleResponse.  # noqa: E501


        :return: The id of this RoleResponse.  # noqa: E501
        :rtype: finbourne_access.RoleId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleResponse.


        :param id: The id of this RoleResponse.  # noqa: E501
        :type id: finbourne_access.RoleId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def role_hierarchy_index(self):
        """Gets the role_hierarchy_index of this RoleResponse.  # noqa: E501

        The hierarchical index of the role  # noqa: E501

        :return: The role_hierarchy_index of this RoleResponse.  # noqa: E501
        :rtype: int
        """
        return self._role_hierarchy_index

    @role_hierarchy_index.setter
    def role_hierarchy_index(self, role_hierarchy_index):
        """Sets the role_hierarchy_index of this RoleResponse.

        The hierarchical index of the role  # noqa: E501

        :param role_hierarchy_index: The role_hierarchy_index of this RoleResponse.  # noqa: E501
        :type role_hierarchy_index: int
        """
        if self.local_vars_configuration.client_side_validation and role_hierarchy_index is None:  # noqa: E501
            raise ValueError("Invalid value for `role_hierarchy_index`, must not be `None`")  # noqa: E501

        self._role_hierarchy_index = role_hierarchy_index

    @property
    def description(self):
        """Gets the description of this RoleResponse.  # noqa: E501

        The description of the role  # noqa: E501

        :return: The description of this RoleResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleResponse.

        The description of the role  # noqa: E501

        :param description: The description of this RoleResponse.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def resource(self):
        """Gets the resource of this RoleResponse.  # noqa: E501


        :return: The resource of this RoleResponse.  # noqa: E501
        :rtype: finbourne_access.RoleResourceRequest
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this RoleResponse.


        :param resource: The resource of this RoleResponse.  # noqa: E501
        :type resource: finbourne_access.RoleResourceRequest
        """
        if self.local_vars_configuration.client_side_validation and resource is None:  # noqa: E501
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    @property
    def when(self):
        """Gets the when of this RoleResponse.  # noqa: E501


        :return: The when of this RoleResponse.  # noqa: E501
        :rtype: finbourne_access.WhenSpec
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this RoleResponse.


        :param when: The when of this RoleResponse.  # noqa: E501
        :type when: finbourne_access.WhenSpec
        """
        if self.local_vars_configuration.client_side_validation and when is None:  # noqa: E501
            raise ValueError("Invalid value for `when`, must not be `None`")  # noqa: E501

        self._when = when

    @property
    def permission(self):
        """Gets the permission of this RoleResponse.  # noqa: E501

        The action key of the role  # noqa: E501

        :return: The permission of this RoleResponse.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this RoleResponse.

        The action key of the role  # noqa: E501

        :param permission: The permission of this RoleResponse.  # noqa: E501
        :type permission: str
        """
        if self.local_vars_configuration.client_side_validation and permission is None:  # noqa: E501
            raise ValueError("Invalid value for `permission`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                permission is not None and len(permission) < 1):
            raise ValueError("Invalid value for `permission`, length must be greater than or equal to `1`")  # noqa: E501

        self._permission = permission

    @property
    def limit(self):
        """Gets the limit of this RoleResponse.  # noqa: E501

        The identifiers of the role with the maximum privileges that this role can have  # noqa: E501

        :return: The limit of this RoleResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this RoleResponse.

        The identifiers of the role with the maximum privileges that this role can have  # noqa: E501

        :param limit: The limit of this RoleResponse.  # noqa: E501
        :type limit: dict(str, str)
        """

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this RoleResponse.  # noqa: E501


        :return: The links of this RoleResponse.  # noqa: E501
        :rtype: list[finbourne_access.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RoleResponse.


        :param links: The links of this RoleResponse.  # noqa: E501
        :type links: list[finbourne_access.Link]
        """

        self._links = links

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
        if not isinstance(other, RoleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleResponse):
            return True

        return self.to_dict() != other.to_dict()
