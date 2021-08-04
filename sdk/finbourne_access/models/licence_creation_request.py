# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1300
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class LicenceCreationRequest(object):
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
        'description': 'str',
        'applications': 'list[str]',
        'selectors': 'list[LicenceSelectorDefinition]',
        'when': 'WhenSpec',
        '_for': 'list[ForSpec]',
        'how': 'HowSpec',
        '_if': 'list[IfExpression]'
    }

    attribute_map = {
        'code': 'code',
        'description': 'description',
        'applications': 'applications',
        'selectors': 'selectors',
        'when': 'when',
        '_for': 'for',
        'how': 'how',
        '_if': 'if'
    }

    required_map = {
        'code': 'required',
        'description': 'required',
        'applications': 'required',
        'selectors': 'required',
        'when': 'required',
        '_for': 'optional',
        'how': 'optional',
        '_if': 'optional'
    }

    def __init__(self, code=None, description=None, applications=None, selectors=None, when=None, _for=None, how=None, _if=None):  # noqa: E501
        """
        LicenceCreationRequest - a model defined in OpenAPI

        :param code:  (required)
        :type code: str
        :param description:  (required)
        :type description: str
        :param applications:  (required)
        :type applications: list[str]
        :param selectors:  (required)
        :type selectors: list[finbourne_access.LicenceSelectorDefinition]
        :param when:  (required)
        :type when: finbourne_access.WhenSpec
        :param _for: 
        :type _for: list[finbourne_access.ForSpec]
        :param how: 
        :type how: finbourne_access.HowSpec
        :param _if: 
        :type _if: list[finbourne_access.IfExpression]

        """  # noqa: E501

        self._code = None
        self._description = None
        self._applications = None
        self._selectors = None
        self._when = None
        self.__for = None
        self._how = None
        self.__if = None
        self.discriminator = None

        self.code = code
        self.description = description
        self.applications = applications
        self.selectors = selectors
        self.when = when
        self._for = _for
        if how is not None:
            self.how = how
        self._if = _if

    @property
    def code(self):
        """Gets the code of this LicenceCreationRequest.  # noqa: E501


        :return: The code of this LicenceCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this LicenceCreationRequest.


        :param code: The code of this LicenceCreationRequest.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501
        if code is not None and len(code) > 100:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `100`")  # noqa: E501
        if code is not None and len(code) < 3:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `3`")  # noqa: E501
        if (code is not None and not re.search(r'^[a-zA-Z][a-zA-Z0-9-_ +]{2,100}$', code)):  # noqa: E501
            raise ValueError(r"Invalid value for `code`, must be a follow pattern or equal to `/^[a-zA-Z][a-zA-Z0-9-_ +]{2,100}$/`")  # noqa: E501

        self._code = code

    @property
    def description(self):
        """Gets the description of this LicenceCreationRequest.  # noqa: E501


        :return: The description of this LicenceCreationRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LicenceCreationRequest.


        :param description: The description of this LicenceCreationRequest.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if description is not None and len(description) > 1024:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1024`")  # noqa: E501
        if description is not None and len(description) < 0:
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    @property
    def applications(self):
        """Gets the applications of this LicenceCreationRequest.  # noqa: E501


        :return: The applications of this LicenceCreationRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._applications

    @applications.setter
    def applications(self, applications):
        """Sets the applications of this LicenceCreationRequest.


        :param applications: The applications of this LicenceCreationRequest.  # noqa: E501
        :type: list[str]
        """
        if applications is None:
            raise ValueError("Invalid value for `applications`, must not be `None`")  # noqa: E501

        self._applications = applications

    @property
    def selectors(self):
        """Gets the selectors of this LicenceCreationRequest.  # noqa: E501


        :return: The selectors of this LicenceCreationRequest.  # noqa: E501
        :rtype: list[LicenceSelectorDefinition]
        """
        return self._selectors

    @selectors.setter
    def selectors(self, selectors):
        """Sets the selectors of this LicenceCreationRequest.


        :param selectors: The selectors of this LicenceCreationRequest.  # noqa: E501
        :type: list[LicenceSelectorDefinition]
        """
        if selectors is None:
            raise ValueError("Invalid value for `selectors`, must not be `None`")  # noqa: E501

        self._selectors = selectors

    @property
    def when(self):
        """Gets the when of this LicenceCreationRequest.  # noqa: E501


        :return: The when of this LicenceCreationRequest.  # noqa: E501
        :rtype: WhenSpec
        """
        return self._when

    @when.setter
    def when(self, when):
        """Sets the when of this LicenceCreationRequest.


        :param when: The when of this LicenceCreationRequest.  # noqa: E501
        :type: WhenSpec
        """
        if when is None:
            raise ValueError("Invalid value for `when`, must not be `None`")  # noqa: E501

        self._when = when

    @property
    def _for(self):
        """Gets the _for of this LicenceCreationRequest.  # noqa: E501


        :return: The _for of this LicenceCreationRequest.  # noqa: E501
        :rtype: list[ForSpec]
        """
        return self.__for

    @_for.setter
    def _for(self, _for):
        """Sets the _for of this LicenceCreationRequest.


        :param _for: The _for of this LicenceCreationRequest.  # noqa: E501
        :type: list[ForSpec]
        """

        self.__for = _for

    @property
    def how(self):
        """Gets the how of this LicenceCreationRequest.  # noqa: E501


        :return: The how of this LicenceCreationRequest.  # noqa: E501
        :rtype: HowSpec
        """
        return self._how

    @how.setter
    def how(self, how):
        """Sets the how of this LicenceCreationRequest.


        :param how: The how of this LicenceCreationRequest.  # noqa: E501
        :type: HowSpec
        """

        self._how = how

    @property
    def _if(self):
        """Gets the _if of this LicenceCreationRequest.  # noqa: E501


        :return: The _if of this LicenceCreationRequest.  # noqa: E501
        :rtype: list[IfExpression]
        """
        return self.__if

    @_if.setter
    def _if(self, _if):
        """Sets the _if of this LicenceCreationRequest.


        :param _if: The _if of this LicenceCreationRequest.  # noqa: E501
        :type: list[IfExpression]
        """

        self.__if = _if

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
        if not isinstance(other, LicenceCreationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
