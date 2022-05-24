# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.2006
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


class UserRoleResponse(object):
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
        'resource': 'RoleResourceRequest',
        'id': 'RoleId',
        'links': 'list[Link]'
    }

    attribute_map = {
        'resource': 'resource',
        'id': 'id',
        'links': 'links'
    }

    required_map = {
        'resource': 'required',
        'id': 'required',
        'links': 'optional'
    }

    def __init__(self, resource=None, id=None, links=None, local_vars_configuration=None):  # noqa: E501
        """UserRoleResponse - a model defined in OpenAPI"
        
        :param resource:  (required)
        :type resource: finbourne_access.RoleResourceRequest
        :param id:  (required)
        :type id: finbourne_access.RoleId
        :param links: 
        :type links: list[finbourne_access.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._resource = None
        self._id = None
        self._links = None
        self.discriminator = None

        self.resource = resource
        self.id = id
        self.links = links

    @property
    def resource(self):
        """Gets the resource of this UserRoleResponse.  # noqa: E501


        :return: The resource of this UserRoleResponse.  # noqa: E501
        :rtype: finbourne_access.RoleResourceRequest
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this UserRoleResponse.


        :param resource: The resource of this UserRoleResponse.  # noqa: E501
        :type resource: finbourne_access.RoleResourceRequest
        """
        if self.local_vars_configuration.client_side_validation and resource is None:  # noqa: E501
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

    @property
    def id(self):
        """Gets the id of this UserRoleResponse.  # noqa: E501


        :return: The id of this UserRoleResponse.  # noqa: E501
        :rtype: finbourne_access.RoleId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserRoleResponse.


        :param id: The id of this UserRoleResponse.  # noqa: E501
        :type id: finbourne_access.RoleId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def links(self):
        """Gets the links of this UserRoleResponse.  # noqa: E501


        :return: The links of this UserRoleResponse.  # noqa: E501
        :rtype: list[finbourne_access.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UserRoleResponse.


        :param links: The links of this UserRoleResponse.  # noqa: E501
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
        if not isinstance(other, UserRoleResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UserRoleResponse):
            return True

        return self.to_dict() != other.to_dict()