# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1202
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class EvaluationRequest(object):
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
        'request': 'RequestDetails',
        'resource': 'ResourceDetails'
    }

    attribute_map = {
        'request': 'request',
        'resource': 'resource'
    }

    required_map = {
        'request': 'required',
        'resource': 'required'
    }

    def __init__(self, request=None, resource=None):  # noqa: E501
        """
        EvaluationRequest - a model defined in OpenAPI

        :param request:  (required)
        :type request: finbourne_access.RequestDetails
        :param resource:  (required)
        :type resource: finbourne_access.ResourceDetails

        """  # noqa: E501

        self._request = None
        self._resource = None
        self.discriminator = None

        self.request = request
        self.resource = resource

    @property
    def request(self):
        """Gets the request of this EvaluationRequest.  # noqa: E501


        :return: The request of this EvaluationRequest.  # noqa: E501
        :rtype: RequestDetails
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this EvaluationRequest.


        :param request: The request of this EvaluationRequest.  # noqa: E501
        :type: RequestDetails
        """
        if request is None:
            raise ValueError("Invalid value for `request`, must not be `None`")  # noqa: E501

        self._request = request

    @property
    def resource(self):
        """Gets the resource of this EvaluationRequest.  # noqa: E501


        :return: The resource of this EvaluationRequest.  # noqa: E501
        :rtype: ResourceDetails
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this EvaluationRequest.


        :param resource: The resource of this EvaluationRequest.  # noqa: E501
        :type: ResourceDetails
        """
        if resource is None:
            raise ValueError("Invalid value for `resource`, must not be `None`")  # noqa: E501

        self._resource = resource

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
        if not isinstance(other, EvaluationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
