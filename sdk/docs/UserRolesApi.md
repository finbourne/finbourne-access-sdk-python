# finbourne_access.UserRolesApi

All URIs are relative to *https://fbn-ci.lusid.com/access*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_policy_collection_to_user_role**](UserRolesApi.md#add_policy_collection_to_user_role) | **POST** /api/userroles/{userid}/policycollections | [EXPERIMENTAL] AddPolicyCollectionToUserRole: Add a policy collection to a user-role
[**add_policy_to_user_role**](UserRolesApi.md#add_policy_to_user_role) | **POST** /api/userroles/{userid}/policies | [EXPERIMENTAL] AddPolicyToUserRole: Add a policy to a user-role
[**create_user_role**](UserRolesApi.md#create_user_role) | **POST** /api/userroles | [EXPERIMENTAL] CreateUserRole: Create a user-role
[**delete_user_role**](UserRolesApi.md#delete_user_role) | **DELETE** /api/userroles/{userid} | [EXPERIMENTAL] DeleteUserRole: Delete a user-role
[**get_user_role**](UserRolesApi.md#get_user_role) | **GET** /api/userroles/{userid} | [EXPERIMENTAL] GetUserRole: Get a user-role
[**list_user_roles**](UserRolesApi.md#list_user_roles) | **GET** /api/userroles | [EXPERIMENTAL] ListUserRoles: List user-roles
[**remove_policy_collection_from_user_role**](UserRolesApi.md#remove_policy_collection_from_user_role) | **DELETE** /api/userroles/{userid}/policycollections/{policyCollectionScope}/{policyCollectionCode} | [EXPERIMENTAL] RemovePolicyCollectionFromUserRole: Remove a policy collection from a user-role
[**remove_policy_from_user_role**](UserRolesApi.md#remove_policy_from_user_role) | **DELETE** /api/userroles/{userid}/policies/{policyScope}/{policyCode} | [EXPERIMENTAL] RemovePolicyFromUserRole: Remove a policy from a user-role
[**update_user_role**](UserRolesApi.md#update_user_role) | **POST** /api/userroles/{userid}/update | [EXPERIMENTAL] UpdateUserRole: Update a user-role


# **add_policy_collection_to_user_role**
> UserRoleResponse add_policy_collection_to_user_role(userid, add_policy_collection_to_role_request)

[EXPERIMENTAL] AddPolicyCollectionToUserRole: Add a policy collection to a user-role

Adds a policy collection to a user-role.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/access
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_access.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_access.UserRolesApi(api_client)
    userid = 'userid_example' # str | Id of the User Role to get
add_policy_collection_to_role_request = {"policyCollections":[{"scope":"ExampleAddPolicyCollectionScope","code":"ExampleAddPolicyCollectionCode"}]} # AddPolicyCollectionToRoleRequest | Dto of the policy collection to be added.

    try:
        # [EXPERIMENTAL] AddPolicyCollectionToUserRole: Add a policy collection to a user-role
        api_response = api_instance.add_policy_collection_to_user_role(userid, add_policy_collection_to_role_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserRolesApi->add_policy_collection_to_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the User Role to get | 
 **add_policy_collection_to_role_request** | [**AddPolicyCollectionToRoleRequest**](AddPolicyCollectionToRoleRequest.md)| Dto of the policy collection to be added. | 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role with added policy collection. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_policy_to_user_role**
> UserRoleResponse add_policy_to_user_role(userid, add_policy_to_role_request)

[EXPERIMENTAL] AddPolicyToUserRole: Add a policy to a user-role

Adds a policy to a user-role.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/access
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_access.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_access.UserRolesApi(api_client)
    userid = 'userid_example' # str | Id of the User Role to get
add_policy_to_role_request = {"policies":[{"scope":"ExampleAddPolicyScope","code":"ExampleAddPolicyCode"}]} # AddPolicyToRoleRequest | Dto of the policy to be added.

    try:
        # [EXPERIMENTAL] AddPolicyToUserRole: Add a policy to a user-role
        api_response = api_instance.add_policy_to_user_role(userid, add_policy_to_role_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserRolesApi->add_policy_to_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the User Role to get | 
 **add_policy_to_role_request** | [**AddPolicyToRoleRequest**](AddPolicyToRoleRequest.md)| Dto of the policy to be added. | 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role with added policy collection. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_role**
> UserRoleResponse create_user_role(user_role_creation_request)

[EXPERIMENTAL] CreateUserRole: Create a user-role

Creates a new user-role.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/access
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_access.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_access.UserRolesApi(api_client)
    user_role_creation_request = {"userId":"ExampleUserId","resource":{"policies":[{"scope":"ExamplePolicyId","code":"ExampleScope"}],"policyCollections":[{"scope":"ExamplePolicyCollectionId","code":"ExampleScope"}]}} # UserRoleCreationRequest | Definition of the user-role to create.

    try:
        # [EXPERIMENTAL] CreateUserRole: Create a user-role
        api_response = api_instance.create_user_role(user_role_creation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserRolesApi->create_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_role_creation_request** | [**UserRoleCreationRequest**](UserRoleCreationRequest.md)| Definition of the user-role to create. | 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role that has been created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_role**
> delete_user_role(userid)

[EXPERIMENTAL] DeleteUserRole: Delete a user-role

Deletes an identified user-role.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/access
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_access.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_access.UserRolesApi(api_client)
    userid = 'userid_example' # str | Id of the user-role to delete.

    try:
        # [EXPERIMENTAL] DeleteUserRole: Delete a user-role
        api_instance.delete_user_role(userid)
    except ApiException as e:
        print("Exception when calling UserRolesApi->delete_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the user-role to delete. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_role**
> UserRoleResponse get_user_role(userid)

[EXPERIMENTAL] GetUserRole: Get a user-role

Get an identified user-role.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/access
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_access.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_access.UserRolesApi(api_client)
    userid = 'userid_example' # str | Id of the user-role to get.

    try:
        # [EXPERIMENTAL] GetUserRole: Get a user-role
        api_response = api_instance.get_user_role(userid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserRolesApi->get_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the user-role to get. | 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested user role. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_roles**
> ResourceListOfUserRoleResponse list_user_roles(filter=filter, sort_by=sort_by, limit=limit, page=page)

[EXPERIMENTAL] ListUserRoles: List user-roles

Lists all user-roles and pages.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/access
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_access.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_access.UserRolesApi(api_client)
    filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
sort_by = 'sort_by_example' # str | Optional. Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName (optional)
limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
page = 'page_example' # str | Optional. Encoded page string returned from a previous search result that will retrieve              the next page of data. (optional)

    try:
        # [EXPERIMENTAL] ListUserRoles: List user-roles
        api_response = api_instance.list_user_roles(filter=filter, sort_by=sort_by, limit=limit, page=page)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserRolesApi->list_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **sort_by** | **str**| Optional. Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **page** | **str**| Optional. Encoded page string returned from a previous search result that will retrieve              the next page of data. | [optional] 

### Return type

[**ResourceListOfUserRoleResponse**](ResourceListOfUserRoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_policy_collection_from_user_role**
> remove_policy_collection_from_user_role(userid, policy_collection_scope, policy_collection_code)

[EXPERIMENTAL] RemovePolicyCollectionFromUserRole: Remove a policy collection from a user-role

Removes a policy collection from a user-role.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/access
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_access.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_access.UserRolesApi(api_client)
    userid = 'userid_example' # str | Id of the User Role to get
policy_collection_scope = 'policy_collection_scope_example' # str | The scope of policy collection to remove from the User Role
policy_collection_code = 'policy_collection_code_example' # str | The code of the policy collection to remove from the User Role

    try:
        # [EXPERIMENTAL] RemovePolicyCollectionFromUserRole: Remove a policy collection from a user-role
        api_instance.remove_policy_collection_from_user_role(userid, policy_collection_scope, policy_collection_code)
    except ApiException as e:
        print("Exception when calling UserRolesApi->remove_policy_collection_from_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the User Role to get | 
 **policy_collection_scope** | **str**| The scope of policy collection to remove from the User Role | 
 **policy_collection_code** | **str**| The code of the policy collection to remove from the User Role | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_policy_from_user_role**
> remove_policy_from_user_role(userid, policy_scope, policy_code)

[EXPERIMENTAL] RemovePolicyFromUserRole: Remove a policy from a user-role

Removes a policy from a user-role.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/access
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_access.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_access.UserRolesApi(api_client)
    userid = 'userid_example' # str | Id of the User Role to get
policy_scope = 'policy_scope_example' # str | The scope of the policy to remove from the User Role
policy_code = 'policy_code_example' # str | The code of the policy to remove from the User Role

    try:
        # [EXPERIMENTAL] RemovePolicyFromUserRole: Remove a policy from a user-role
        api_instance.remove_policy_from_user_role(userid, policy_scope, policy_code)
    except ApiException as e:
        print("Exception when calling UserRolesApi->remove_policy_from_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the User Role to get | 
 **policy_scope** | **str**| The scope of the policy to remove from the User Role | 
 **policy_code** | **str**| The code of the policy to remove from the User Role | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_role**
> UserRoleResponse update_user_role(userid, user_role_update_request)

[EXPERIMENTAL] UpdateUserRole: Update a user-role

Updates an identified user-role.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/access
# See configuration.py for a list of all supported configuration parameters.
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = finbourne_access.Configuration(
    host = "https://fbn-ci.lusid.com/access"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with finbourne_access.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = finbourne_access.UserRolesApi(api_client)
    userid = 'userid_example' # str | Id of the user-role to be updated.
user_role_update_request = {"resource":{"policies":[{"scope":"ExamplePolicyId","code":"ExampleScope"}],"policyCollections":[{"scope":"ExamplePolicyCollectionId","code":"ExampleScope"}]}} # UserRoleUpdateRequest | Definition of the update to apply to the user-role.

    try:
        # [EXPERIMENTAL] UpdateUserRole: Update a user-role
        api_response = api_instance.update_user_role(userid, user_role_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserRolesApi->update_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the user-role to be updated. | 
 **user_role_update_request** | [**UserRoleUpdateRequest**](UserRoleUpdateRequest.md)| Definition of the update to apply to the user-role. | 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role that has been updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

