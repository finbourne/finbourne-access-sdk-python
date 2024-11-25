# finbourne_access.UserRolesApi

All URIs are relative to *https://fbn-prd.lusid.com/access*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_policy_collection_to_user_role**](UserRolesApi.md#add_policy_collection_to_user_role) | **POST** /api/userroles/{userid}/policycollections | AddPolicyCollectionToUserRole: Add a policy collection to a user-role
[**add_policy_to_user_role**](UserRolesApi.md#add_policy_to_user_role) | **POST** /api/userroles/{userid}/policies | AddPolicyToUserRole: Add a policy to a user-role
[**create_user_role**](UserRolesApi.md#create_user_role) | **POST** /api/userroles | CreateUserRole: Create a user-role
[**delete_user_role**](UserRolesApi.md#delete_user_role) | **DELETE** /api/userroles/{userid} | DeleteUserRole: Delete a user-role
[**get_user_role**](UserRolesApi.md#get_user_role) | **GET** /api/userroles/{userid} | GetUserRole: Get a user-role
[**list_user_roles**](UserRolesApi.md#list_user_roles) | **GET** /api/userroles | ListUserRoles: List user-roles
[**remove_policy_collection_from_user_role**](UserRolesApi.md#remove_policy_collection_from_user_role) | **DELETE** /api/userroles/{userid}/policycollections/{policyCollectionScope}/{policyCollectionCode} | RemovePolicyCollectionFromUserRole: Remove a policy collection from a user-role
[**remove_policy_from_user_role**](UserRolesApi.md#remove_policy_from_user_role) | **DELETE** /api/userroles/{userid}/policies/{policyScope}/{policyCode} | RemovePolicyFromUserRole: Remove a policy from a user-role
[**update_user_role**](UserRolesApi.md#update_user_role) | **POST** /api/userroles/{userid}/update | UpdateUserRole: Update a user-role


# **add_policy_collection_to_user_role**
> UserRoleResponse add_policy_collection_to_user_role(userid, add_policy_collection_to_role_request)

AddPolicyCollectionToUserRole: Add a policy collection to a user-role

Adds a policy collection to a user-role.

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    UserRolesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "accessUrl":"https://<your-domain>.lusid.com/access",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_access SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(UserRolesApi)
    userid = 'userid_example' # str | Id of the User Role to get

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # add_policy_collection_to_role_request = AddPolicyCollectionToRoleRequest.from_json("")
    # add_policy_collection_to_role_request = AddPolicyCollectionToRoleRequest.from_dict({})
    add_policy_collection_to_role_request = AddPolicyCollectionToRoleRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_policy_collection_to_user_role(userid, add_policy_collection_to_role_request, opts=opts)

        # AddPolicyCollectionToUserRole: Add a policy collection to a user-role
        api_response = api_instance.add_policy_collection_to_user_role(userid, add_policy_collection_to_role_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling UserRolesApi->add_policy_collection_to_user_role: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the User Role to get | 
 **add_policy_collection_to_role_request** | [**AddPolicyCollectionToRoleRequest**](AddPolicyCollectionToRoleRequest.md)| Dto of the policy collection to be added. | 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role with added policy collection. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **add_policy_to_user_role**
> UserRoleResponse add_policy_to_user_role(userid, add_policy_to_role_request)

AddPolicyToUserRole: Add a policy to a user-role

Adds a policy to a user-role.

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    UserRolesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "accessUrl":"https://<your-domain>.lusid.com/access",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_access SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(UserRolesApi)
    userid = 'userid_example' # str | Id of the User Role to get

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # add_policy_to_role_request = AddPolicyToRoleRequest.from_json("")
    # add_policy_to_role_request = AddPolicyToRoleRequest.from_dict({})
    add_policy_to_role_request = AddPolicyToRoleRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_policy_to_user_role(userid, add_policy_to_role_request, opts=opts)

        # AddPolicyToUserRole: Add a policy to a user-role
        api_response = api_instance.add_policy_to_user_role(userid, add_policy_to_role_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling UserRolesApi->add_policy_to_user_role: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the User Role to get | 
 **add_policy_to_role_request** | [**AddPolicyToRoleRequest**](AddPolicyToRoleRequest.md)| Dto of the policy to be added. | 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role with added policy collection. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_user_role**
> UserRoleResponse create_user_role(user_role_creation_request)

CreateUserRole: Create a user-role

Creates a new user-role.

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    UserRolesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "accessUrl":"https://<your-domain>.lusid.com/access",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_access SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(UserRolesApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # user_role_creation_request = UserRoleCreationRequest.from_json("")
    # user_role_creation_request = UserRoleCreationRequest.from_dict({})
    user_role_creation_request = UserRoleCreationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_user_role(user_role_creation_request, opts=opts)

        # CreateUserRole: Create a user-role
        api_response = api_instance.create_user_role(user_role_creation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling UserRolesApi->create_user_role: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_role_creation_request** | [**UserRoleCreationRequest**](UserRoleCreationRequest.md)| Definition of the user-role to create. | 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role that has been created. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_user_role**
> delete_user_role(userid)

DeleteUserRole: Delete a user-role

Deletes an identified user-role.

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    UserRolesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "accessUrl":"https://<your-domain>.lusid.com/access",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_access SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(UserRolesApi)
    userid = 'userid_example' # str | Id of the user-role to delete.

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.delete_user_role(userid, opts=opts)

        # DeleteUserRole: Delete a user-role
        api_instance.delete_user_role(userid)
    except ApiException as e:
        print("Exception when calling UserRolesApi->delete_user_role: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the user-role to delete. | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_user_role**
> UserRoleResponse get_user_role(userid)

GetUserRole: Get a user-role

Get an identified user-role.

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    UserRolesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "accessUrl":"https://<your-domain>.lusid.com/access",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_access SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(UserRolesApi)
    userid = 'userid_example' # str | Id of the user-role to get.

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_user_role(userid, opts=opts)

        # GetUserRole: Get a user-role
        api_response = api_instance.get_user_role(userid)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling UserRolesApi->get_user_role: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the user-role to get. | 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested user role. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_user_roles**
> ResourceListOfUserRoleResponse list_user_roles(filter=filter, sort_by=sort_by, limit=limit, page=page)

ListUserRoles: List user-roles

Lists all user-roles and pages.

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    UserRolesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "accessUrl":"https://<your-domain>.lusid.com/access",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_access SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(UserRolesApi)
    filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
    sort_by = 'sort_by_example' # str | Optional. Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName (optional)
    limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
    page = 'page_example' # str | Optional. Encoded page string returned from a previous search result that will retrieve              the next page of data. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_user_roles(filter=filter, sort_by=sort_by, limit=limit, page=page, opts=opts)

        # ListUserRoles: List user-roles
        api_response = api_instance.list_user_roles(filter=filter, sort_by=sort_by, limit=limit, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling UserRolesApi->list_user_roles: %s\n" % e)

main()
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **remove_policy_collection_from_user_role**
> remove_policy_collection_from_user_role(userid, policy_collection_scope, policy_collection_code)

RemovePolicyCollectionFromUserRole: Remove a policy collection from a user-role

Removes a policy collection from a user-role.

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    UserRolesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "accessUrl":"https://<your-domain>.lusid.com/access",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_access SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(UserRolesApi)
    userid = 'userid_example' # str | Id of the User Role to get
    policy_collection_scope = 'policy_collection_scope_example' # str | The scope of policy collection to remove from the User Role
    policy_collection_code = 'policy_collection_code_example' # str | The code of the policy collection to remove from the User Role

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.remove_policy_collection_from_user_role(userid, policy_collection_scope, policy_collection_code, opts=opts)

        # RemovePolicyCollectionFromUserRole: Remove a policy collection from a user-role
        api_instance.remove_policy_collection_from_user_role(userid, policy_collection_scope, policy_collection_code)
    except ApiException as e:
        print("Exception when calling UserRolesApi->remove_policy_collection_from_user_role: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the User Role to get | 
 **policy_collection_scope** | **str**| The scope of policy collection to remove from the User Role | 
 **policy_collection_code** | **str**| The code of the policy collection to remove from the User Role | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **remove_policy_from_user_role**
> remove_policy_from_user_role(userid, policy_scope, policy_code)

RemovePolicyFromUserRole: Remove a policy from a user-role

Removes a policy from a user-role.

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    UserRolesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "accessUrl":"https://<your-domain>.lusid.com/access",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_access SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(UserRolesApi)
    userid = 'userid_example' # str | Id of the User Role to get
    policy_scope = 'policy_scope_example' # str | The scope of the policy to remove from the User Role
    policy_code = 'policy_code_example' # str | The code of the policy to remove from the User Role

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.remove_policy_from_user_role(userid, policy_scope, policy_code, opts=opts)

        # RemovePolicyFromUserRole: Remove a policy from a user-role
        api_instance.remove_policy_from_user_role(userid, policy_scope, policy_code)
    except ApiException as e:
        print("Exception when calling UserRolesApi->remove_policy_from_user_role: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the User Role to get | 
 **policy_scope** | **str**| The scope of the policy to remove from the User Role | 
 **policy_code** | **str**| The code of the policy to remove from the User Role | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_user_role**
> UserRoleResponse update_user_role(userid, user_role_update_request)

UpdateUserRole: Update a user-role

Updates an identified user-role.

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    UserRolesApi
)

def main():

    with open("secrets.json", "w") as file:
        file.write('''
    {
        "api":
        {
            "tokenUrl":"<your-token-url>",
            "accessUrl":"https://<your-domain>.lusid.com/access",
            "username":"<your-username>",
            "password":"<your-password>",
            "clientId":"<your-client-id>",
            "clientSecret":"<your-client-secret>"
        }
    }''')

    # Use the finbourne_access SyncApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = SyncApiClientFactory(opts=opts)

    api_client_factory = SyncApiClientFactory()

    # Enter a context with an instance of the SyncApiClientFactory to ensure the connection pool is closed after use
    
    # Create an instance of the API class
    api_instance = api_client_factory.build(UserRolesApi)
    userid = 'userid_example' # str | Id of the user-role to be updated.

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # user_role_update_request = UserRoleUpdateRequest.from_json("")
    # user_role_update_request = UserRoleUpdateRequest.from_dict({})
    user_role_update_request = UserRoleUpdateRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_user_role(userid, user_role_update_request, opts=opts)

        # UpdateUserRole: Update a user-role
        api_response = api_instance.update_user_role(userid, user_role_update_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling UserRolesApi->update_user_role: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| Id of the user-role to be updated. | 
 **user_role_update_request** | [**UserRoleUpdateRequest**](UserRoleUpdateRequest.md)| Definition of the update to apply to the user-role. | 

### Return type

[**UserRoleResponse**](UserRoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User role that has been updated. |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

