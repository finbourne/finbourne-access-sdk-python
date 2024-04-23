# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.3795
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


class ActionId(object):
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
        'scope': 'str',
        'activity': 'str',
        'entity': 'str'
    }

    attribute_map = {
        'scope': 'scope',
        'activity': 'activity',
        'entity': 'entity'
    }

    required_map = {
        'scope': 'required',
        'activity': 'required',
        'entity': 'required'
    }

    def __init__(self, scope=None, activity=None, entity=None, local_vars_configuration=None):  # noqa: E501
        """ActionId - a model defined in OpenAPI"
        
        :param scope:  (required)
        :type scope: str
        :param activity:  (required)
        :type activity: str
        :param entity:  (required)
        :type entity: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._scope = None
        self._activity = None
        self._entity = None
        self.discriminator = None

        self.scope = scope
        self.activity = activity
        self.entity = entity

    @property
    def scope(self):
        """Gets the scope of this ActionId.  # noqa: E501


        :return: The scope of this ActionId.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this ActionId.


        :param scope: The scope of this ActionId.  # noqa: E501
        :type scope: str
        """
        if self.local_vars_configuration.client_side_validation and scope is None:  # noqa: E501
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) > 100):
            raise ValueError("Invalid value for `scope`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                scope is not None and len(scope) < 3):
            raise ValueError("Invalid value for `scope`, length must be greater than or equal to `3`")  # noqa: E501

        self._scope = scope

    @property
    def activity(self):
        """Gets the activity of this ActionId.  # noqa: E501


        :return: The activity of this ActionId.  # noqa: E501
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this ActionId.


        :param activity: The activity of this ActionId.  # noqa: E501
        :type activity: str
        """
        if self.local_vars_configuration.client_side_validation and activity is None:  # noqa: E501
            raise ValueError("Invalid value for `activity`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                activity is not None and len(activity) > 25):
            raise ValueError("Invalid value for `activity`, length must be less than or equal to `25`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                activity is not None and len(activity) < 3):
            raise ValueError("Invalid value for `activity`, length must be greater than or equal to `3`")  # noqa: E501

        self._activity = activity

    @property
    def entity(self):
        """Gets the entity of this ActionId.  # noqa: E501


        :return: The entity of this ActionId.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this ActionId.


        :param entity: The entity of this ActionId.  # noqa: E501
        :type entity: str
        """
        if self.local_vars_configuration.client_side_validation and entity is None:  # noqa: E501
            raise ValueError("Invalid value for `entity`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                entity is not None and len(entity) > 25):
            raise ValueError("Invalid value for `entity`, length must be less than or equal to `25`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                entity is not None and len(entity) < 3):
            raise ValueError("Invalid value for `entity`, length must be greater than or equal to `3`")  # noqa: E501

        self._entity = entity

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
        if not isinstance(other, ActionId):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ActionId):
            return True

        return self.to_dict() != other.to_dict()
