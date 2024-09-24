# finbourne_access.RolesApi

All URIs are relative to *https://fbn-ci.lusid.com/access*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_policy_collection_to_role**](RolesApi.md#add_policy_collection_to_role) | **POST** /api/roles/{scope}/{code}/policycollections | AddPolicyCollectionToRole: Add policy collections to a role
[**create_role**](RolesApi.md#create_role) | **POST** /api/roles | CreateRole: Create Role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /api/roles/{code} | DeleteRole: Delete Role
[**get_role**](RolesApi.md#get_role) | **GET** /api/roles/{code} | GetRole: Get Role
[**list_roles**](RolesApi.md#list_roles) | **GET** /api/roles | ListRoles: List Roles
[**remove_policy_collection_from_role**](RolesApi.md#remove_policy_collection_from_role) | **DELETE** /api/roles/{scope}/{code}/policycollections/{policycollectionscope}/{policycollectioncode} | RemovePolicyCollectionFromRole: Remove policy collection from role
[**update_role**](RolesApi.md#update_role) | **PUT** /api/roles/{code} | UpdateRole: Update Role


# **add_policy_collection_to_role**
> RoleResponse add_policy_collection_to_role(scope, code, add_policy_collection_to_role_request)

AddPolicyCollectionToRole: Add policy collections to a role

Assigns policy collections to a role

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
    api_instance = finbourne_access.RolesApi(api_client)
    scope = 'scope_example' # str | The scope of the Role
code = 'code_example' # str | The code of the Role
add_policy_collection_to_role_request = {"policyCollections":[{"scope":"ScopeValue","code":"SomePolCollectionCode"},{"scope":"ScopeValue2","code":"AnotherPolicyCollection"}]} # AddPolicyCollectionToRoleRequest | The policy collections to add

    try:
        # AddPolicyCollectionToRole: Add policy collections to a role
        api_response = api_instance.add_policy_collection_to_role(scope, code, add_policy_collection_to_role_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->add_policy_collection_to_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Role | 
 **code** | **str**| The code of the Role | 
 **add_policy_collection_to_role_request** | [**AddPolicyCollectionToRoleRequest**](AddPolicyCollectionToRoleRequest.md)| The policy collections to add | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AddPolicyCollectionToRole |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> RoleResponse create_role(role_creation_request)

CreateRole: Create Role

Creates a Role

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
    api_instance = finbourne_access.RolesApi(api_client)
    role_creation_request = {"code":"example-organisation-role-id","description":"This is an example role to demonstrate their creation","resource":{"policyIdRoleResource":{"policies":[{"scope":"default","code":"official-portfolios-read-only"},{"scope":"default","code":"desk-portfolios"}],"policyCollections":[{"scope":"default","code":"CompanyEmployeeAccess"}]}},"when":{"activate":"2016-08-31T18:00:00.0000000+00:00","deactivate":"2020-08-31T18:00:00.0000000+00:00"}} # RoleCreationRequest | The definition of the Role

    try:
        # CreateRole: Create Role
        api_response = api_instance.create_role(role_creation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_creation_request** | [**RoleCreationRequest**](RoleCreationRequest.md)| The definition of the Role | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created Role |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(code, scope=scope)

DeleteRole: Delete Role

Deletes an identified Role

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
    api_instance = finbourne_access.RolesApi(api_client)
    code = 'code_example' # str | The code of the Role
scope = 'scope_example' # str | >Optional. Will use default scope if not supplied. The scope of the Role (optional)

    try:
        # DeleteRole: Delete Role
        api_instance.delete_role(code, scope=scope)
    except ApiException as e:
        print("Exception when calling RolesApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Role | 
 **scope** | **str**| &gt;Optional. Will use default scope if not supplied. The scope of the Role | [optional] 

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
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleResponse get_role(code, scope=scope)

GetRole: Get Role

Gets an identified Role

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
    api_instance = finbourne_access.RolesApi(api_client)
    code = 'code_example' # str | The code of the Role
scope = 'scope_example' # str | Optional. Will use default scope if not supplied. The scope of the Role (optional)

    try:
        # GetRole: Get Role
        api_response = api_instance.get_role(code, scope=scope)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Role | 
 **scope** | **str**| Optional. Will use default scope if not supplied. The scope of the Role | [optional] 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested Role |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> list[RoleResponse] list_roles(scope=scope)

ListRoles: List Roles

Gets all Roles in a scope

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
    api_instance = finbourne_access.RolesApi(api_client)
    scope = 'scope_example' # str | Optional. Will use all scopes if not supplied. The requested scope (optional)

    try:
        # ListRoles: List Roles
        api_response = api_instance.list_roles(scope=scope)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->list_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Optional. Will use all scopes if not supplied. The requested scope | [optional] 

### Return type

[**list[RoleResponse]**](RoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Roles |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_policy_collection_from_role**
> RoleResponse remove_policy_collection_from_role(scope, code, policycollectionscope, policycollectioncode)

RemovePolicyCollectionFromRole: Remove policy collection from role

Removes a policy collection from a role

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
    api_instance = finbourne_access.RolesApi(api_client)
    scope = 'scope_example' # str | The scope of the Role
code = 'code_example' # str | The code of the Role
policycollectionscope = 'policycollectionscope_example' # str | The scope of policy collection to remove from the Role
policycollectioncode = 'policycollectioncode_example' # str | The code of the policy collection to remove from the Role

    try:
        # RemovePolicyCollectionFromRole: Remove policy collection from role
        api_response = api_instance.remove_policy_collection_from_role(scope, code, policycollectionscope, policycollectioncode)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->remove_policy_collection_from_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Role | 
 **code** | **str**| The code of the Role | 
 **policycollectionscope** | **str**| The scope of policy collection to remove from the Role | 
 **policycollectioncode** | **str**| The code of the policy collection to remove from the Role | 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RemovePolicyCollectionFromRole |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> RoleResponse update_role(code, role_update_request, scope=scope, before_scope=before_scope, before_code=before_code, after_scope=after_scope, after_code=after_code)

UpdateRole: Update Role

Updates a Role

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
    api_instance = finbourne_access.RolesApi(api_client)
    code = 'code_example' # str | The code of the Role
role_update_request = {"description":"This is an example role to demonstrate their update","resource":{"policyIdRoleResource":{"policies":[{"scope":"default","code":"official-portfolios-read-only"},{"scope":"default","code":"desk-portfolios"}],"policyCollections":[{"scope":"default","code":"CompanyEmployeeAccess"}]}},"when":{"activate":"2016-08-31T18:00:00.0000000+00:00","deactivate":"2020-08-31T18:00:00.0000000+00:00"}} # RoleUpdateRequest | The updated definition of the Role
scope = 'scope_example' # str | >Optional. Will use default scope if not supplied. The scope of the Role (optional)
before_scope = 'before_scope_example' # str | Optional. The scope of the Role. Will use default scope if not supplied. (optional)
before_code = 'before_code_example' # str | Optional. The code of the Role (optional)
after_scope = 'after_scope_example' # str | Optional. The scope of the Role. Will use default scope if not supplied. (optional)
after_code = 'after_code_example' # str | Optional. The code of the Role (optional)

    try:
        # UpdateRole: Update Role
        api_response = api_instance.update_role(code, role_update_request, scope=scope, before_scope=before_scope, before_code=before_code, after_scope=after_scope, after_code=after_code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Role | 
 **role_update_request** | [**RoleUpdateRequest**](RoleUpdateRequest.md)| The updated definition of the Role | 
 **scope** | **str**| &gt;Optional. Will use default scope if not supplied. The scope of the Role | [optional] 
 **before_scope** | **str**| Optional. The scope of the Role. Will use default scope if not supplied. | [optional] 
 **before_code** | **str**| Optional. The code of the Role | [optional] 
 **after_scope** | **str**| Optional. The scope of the Role. Will use default scope if not supplied. | [optional] 
 **after_code** | **str**| Optional. The code of the Role | [optional] 

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Role |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

