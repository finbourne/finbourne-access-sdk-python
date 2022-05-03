# coding: utf-8

"""
    FINBOURNE Access Management API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.0.1942
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from finbourne_access.api_client import ApiClient
from finbourne_access.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)
from finbourne_access.models.lusid_problem_details import LusidProblemDetails
from finbourne_access.models.lusid_validation_problem_details import LusidValidationProblemDetails
from finbourne_access.models.resource_list_of_user_role_response import ResourceListOfUserRoleResponse
from finbourne_access.models.user_role_creation_request import UserRoleCreationRequest
from finbourne_access.models.user_role_response import UserRoleResponse
from finbourne_access.models.user_role_update_request import UserRoleUpdateRequest


class UserRolesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_user_role(self, user_role_creation_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] CreateUserRole: Create a user-role  # noqa: E501

        Creates a new user-role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_user_role(user_role_creation_request, async_req=True)
        >>> result = thread.get()

        :param user_role_creation_request: Dto of the user-role to be created. (required)
        :type user_role_creation_request: UserRoleCreationRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserRoleResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.create_user_role_with_http_info(user_role_creation_request, **kwargs)  # noqa: E501

    def create_user_role_with_http_info(self, user_role_creation_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] CreateUserRole: Create a user-role  # noqa: E501

        Creates a new user-role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_user_role_with_http_info(user_role_creation_request, async_req=True)
        >>> result = thread.get()

        :param user_role_creation_request: Dto of the user-role to be created. (required)
        :type user_role_creation_request: UserRoleCreationRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (UserRoleResponse, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'user_role_creation_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user_role" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'user_role_creation_request' is set
        if self.api_client.client_side_validation and ('user_role_creation_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_role_creation_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_role_creation_request` when calling `create_user_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_role_creation_request' in local_var_params:
            body_params = local_var_params['user_role_creation_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.1942'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "UserRoleResponse",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/userroles', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def delete_user_role(self, userid, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] DeleteUserRole: Delete a user-role  # noqa: E501

        Deletes an identified user-role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_user_role(userid, async_req=True)
        >>> result = thread.get()

        :param userid: Id of the user, who's user-role will be deleted. (required)
        :type userid: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_user_role_with_http_info(userid, **kwargs)  # noqa: E501

    def delete_user_role_with_http_info(self, userid, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] DeleteUserRole: Delete a user-role  # noqa: E501

        Deletes an identified user-role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_user_role_with_http_info(userid, async_req=True)
        >>> result = thread.get()

        :param userid: Id of the user, who's user-role will be deleted. (required)
        :type userid: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = [
            'userid'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_user_role" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'userid' is set
        if self.api_client.client_side_validation and ('userid' not in local_var_params or  # noqa: E501
                                                        local_var_params['userid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `userid` when calling `delete_user_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'userid' in local_var_params:
            path_params['userid'] = local_var_params['userid']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.1942'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            '/api/userroles/{userid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def get_user_role(self, userid, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetUserRole: Gets a user-role  # noqa: E501

        Gets an identified user-role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_role(userid, async_req=True)
        >>> result = thread.get()

        :param userid: Id of the user-role to get (required)
        :type userid: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserRoleResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.get_user_role_with_http_info(userid, **kwargs)  # noqa: E501

    def get_user_role_with_http_info(self, userid, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] GetUserRole: Gets a user-role  # noqa: E501

        Gets an identified user-role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_user_role_with_http_info(userid, async_req=True)
        >>> result = thread.get()

        :param userid: Id of the user-role to get (required)
        :type userid: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (UserRoleResponse, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'userid'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_role" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'userid' is set
        if self.api_client.client_side_validation and ('userid' not in local_var_params or  # noqa: E501
                                                        local_var_params['userid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `userid` when calling `get_user_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'userid' in local_var_params:
            path_params['userid'] = local_var_params['userid']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.1942'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "UserRoleResponse",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/userroles/{userid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def list_user_roles(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListUserRoles: List user-roles  # noqa: E501

        Lists all user-roles and pages.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_user_roles(async_req=True)
        >>> result = thread.get()

        :param limit: Optional. When paginating, limit the number of returned results to this many.
        :type limit: int
        :param page: Optional. Encoded page string returned from a previous search result that will retrieve              the next page of data.
        :type page: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResourceListOfUserRoleResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.list_user_roles_with_http_info(**kwargs)  # noqa: E501

    def list_user_roles_with_http_info(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] ListUserRoles: List user-roles  # noqa: E501

        Lists all user-roles and pages.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_user_roles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param limit: Optional. When paginating, limit the number of returned results to this many.
        :type limit: int
        :param page: Optional. Encoded page string returned from a previous search result that will retrieve              the next page of data.
        :type page: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (ResourceListOfUserRoleResponse, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'limit',
            'page'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_user_roles" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 5000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_user_roles`, must be a value less than or equal to `5000`")  # noqa: E501
        if self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `limit` when calling `list_user_roles`, must be a value greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('page' in local_var_params and  # noqa: E501
                                                        len(local_var_params['page']) > 500):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_user_roles`, length must be less than or equal to `500`")  # noqa: E501
        if self.api_client.client_side_validation and ('page' in local_var_params and  # noqa: E501
                                                        len(local_var_params['page']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_user_roles`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and 'page' in local_var_params and not re.search(r'^[a-zA-Z0-9\+\/]*={0,3}$', local_var_params['page']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page` when calling `list_user_roles`, must conform to the pattern `/^[a-zA-Z0-9\+\/]*={0,3}$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"


        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.1942'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "ResourceListOfUserRoleResponse",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/userroles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))

    def update_user_role(self, userid, user_role_update_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] UpdateUserRole: Update a user-role  # noqa: E501

        Updates an identified user-role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_user_role(userid, user_role_update_request, async_req=True)
        >>> result = thread.get()

        :param userid: Id of the user-role to get (required)
        :type userid: str
        :param user_role_update_request: Dto of the user-role to be updated. (required)
        :type user_role_update_request: UserRoleUpdateRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UserRoleResponse
        """
        kwargs['_return_http_data_only'] = True
        return self.update_user_role_with_http_info(userid, user_role_update_request, **kwargs)  # noqa: E501

    def update_user_role_with_http_info(self, userid, user_role_update_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] UpdateUserRole: Update a user-role  # noqa: E501

        Updates an identified user-role.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_user_role_with_http_info(userid, user_role_update_request, async_req=True)
        >>> result = thread.get()

        :param userid: Id of the user-role to get (required)
        :type userid: str
        :param user_role_update_request: Dto of the user-role to be updated. (required)
        :type user_role_update_request: UserRoleUpdateRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :return: Returns the result object, the HTTP status code, and the headers.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: (UserRoleResponse, int, HTTPHeaderDict)
        """

        local_var_params = locals()

        all_params = [
            'userid',
            'user_role_update_request'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_headers'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_user_role" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'userid' is set
        if self.api_client.client_side_validation and ('userid' not in local_var_params or  # noqa: E501
                                                        local_var_params['userid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `userid` when calling `update_user_role`")  # noqa: E501
        # verify the required parameter 'user_role_update_request' is set
        if self.api_client.client_side_validation and ('user_role_update_request' not in local_var_params or  # noqa: E501
                                                        local_var_params['user_role_update_request'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `user_role_update_request` when calling `update_user_role`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'userid' in local_var_params:
            path_params['userid'] = local_var_params['userid']  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get('_headers', {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_role_update_request' in local_var_params:
            body_params = local_var_params['user_role_update_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        header_params['Accept-Encoding'] = "gzip, deflate, br"

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.0.1942'

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        response_types_map = {
            200: "UserRoleResponse",
            400: "LusidValidationProblemDetails",
        }

        return self.api_client.call_api(
            '/api/userroles/{userid}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get('_request_auth'))