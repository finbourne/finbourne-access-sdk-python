# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.3029
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


class RequestDetails(object):
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
        'action': 'RequestedActionKey',
        'from_effective_date': 'datetime',
        'to_effective_date': 'datetime',
        'from_as_at': 'datetime',
        'to_as_at': 'datetime'
    }

    attribute_map = {
        'action': 'action',
        'from_effective_date': 'fromEffectiveDate',
        'to_effective_date': 'toEffectiveDate',
        'from_as_at': 'fromAsAt',
        'to_as_at': 'toAsAt'
    }

    required_map = {
        'action': 'required',
        'from_effective_date': 'optional',
        'to_effective_date': 'optional',
        'from_as_at': 'optional',
        'to_as_at': 'optional'
    }

    def __init__(self, action=None, from_effective_date=None, to_effective_date=None, from_as_at=None, to_as_at=None, local_vars_configuration=None):  # noqa: E501
        """RequestDetails - a model defined in OpenAPI"
        
        :param action:  (required)
        :type action: finbourne_access.RequestedActionKey
        :param from_effective_date:  The start date for the requested effective date range for the resource (if null, UtcNow)
        :type from_effective_date: datetime
        :param to_effective_date:  The end date for the requested effective date range for the resource (if null, same as from date)
        :type to_effective_date: datetime
        :param from_as_at:  The requested AsAt date for the resource (if null, Latest). If specifying a range of AsAt dates, this is the lower bounds.
        :type from_as_at: datetime
        :param to_as_at:  Upper bound if specifying a request that requires a range of AsAt dates. This is used if specifying the desire to grant access for a user between an AsAt range.
        :type to_as_at: datetime

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._action = None
        self._from_effective_date = None
        self._to_effective_date = None
        self._from_as_at = None
        self._to_as_at = None
        self.discriminator = None

        self.action = action
        self.from_effective_date = from_effective_date
        self.to_effective_date = to_effective_date
        self.from_as_at = from_as_at
        self.to_as_at = to_as_at

    @property
    def action(self):
        """Gets the action of this RequestDetails.  # noqa: E501


        :return: The action of this RequestDetails.  # noqa: E501
        :rtype: finbourne_access.RequestedActionKey
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this RequestDetails.


        :param action: The action of this RequestDetails.  # noqa: E501
        :type action: finbourne_access.RequestedActionKey
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def from_effective_date(self):
        """Gets the from_effective_date of this RequestDetails.  # noqa: E501

        The start date for the requested effective date range for the resource (if null, UtcNow)  # noqa: E501

        :return: The from_effective_date of this RequestDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._from_effective_date

    @from_effective_date.setter
    def from_effective_date(self, from_effective_date):
        """Sets the from_effective_date of this RequestDetails.

        The start date for the requested effective date range for the resource (if null, UtcNow)  # noqa: E501

        :param from_effective_date: The from_effective_date of this RequestDetails.  # noqa: E501
        :type from_effective_date: datetime
        """

        self._from_effective_date = from_effective_date

    @property
    def to_effective_date(self):
        """Gets the to_effective_date of this RequestDetails.  # noqa: E501

        The end date for the requested effective date range for the resource (if null, same as from date)  # noqa: E501

        :return: The to_effective_date of this RequestDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._to_effective_date

    @to_effective_date.setter
    def to_effective_date(self, to_effective_date):
        """Sets the to_effective_date of this RequestDetails.

        The end date for the requested effective date range for the resource (if null, same as from date)  # noqa: E501

        :param to_effective_date: The to_effective_date of this RequestDetails.  # noqa: E501
        :type to_effective_date: datetime
        """

        self._to_effective_date = to_effective_date

    @property
    def from_as_at(self):
        """Gets the from_as_at of this RequestDetails.  # noqa: E501

        The requested AsAt date for the resource (if null, Latest). If specifying a range of AsAt dates, this is the lower bounds.  # noqa: E501

        :return: The from_as_at of this RequestDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._from_as_at

    @from_as_at.setter
    def from_as_at(self, from_as_at):
        """Sets the from_as_at of this RequestDetails.

        The requested AsAt date for the resource (if null, Latest). If specifying a range of AsAt dates, this is the lower bounds.  # noqa: E501

        :param from_as_at: The from_as_at of this RequestDetails.  # noqa: E501
        :type from_as_at: datetime
        """

        self._from_as_at = from_as_at

    @property
    def to_as_at(self):
        """Gets the to_as_at of this RequestDetails.  # noqa: E501

        Upper bound if specifying a request that requires a range of AsAt dates. This is used if specifying the desire to grant access for a user between an AsAt range.  # noqa: E501

        :return: The to_as_at of this RequestDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._to_as_at

    @to_as_at.setter
    def to_as_at(self, to_as_at):
        """Sets the to_as_at of this RequestDetails.

        Upper bound if specifying a request that requires a range of AsAt dates. This is used if specifying the desire to grant access for a user between an AsAt range.  # noqa: E501

        :param to_as_at: The to_as_at of this RequestDetails.  # noqa: E501
        :type to_as_at: datetime
        """

        self._to_as_at = to_as_at

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
        if not isinstance(other, RequestDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RequestDetails):
            return True

        return self.to_dict() != other.to_dict()
