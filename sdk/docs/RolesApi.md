# finbourne_access.RolesApi

All URIs are relative to *https://fbn-prd.lusid.com/access*

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

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    RolesApi
)

async def main():

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

    # Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)
        scope = 'scope_example' # str | The scope of the Role
        code = 'code_example' # str | The code of the Role

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # add_policy_collection_to_role_request = AddPolicyCollectionToRoleRequest.from_json("")
        # add_policy_collection_to_role_request = AddPolicyCollectionToRoleRequest.from_dict({})
        add_policy_collection_to_role_request = AddPolicyCollectionToRoleRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.add_policy_collection_to_role(scope, code, add_policy_collection_to_role_request, opts=opts)

            # AddPolicyCollectionToRole: Add policy collections to a role
            api_response = await api_instance.add_policy_collection_to_role(scope, code, add_policy_collection_to_role_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RolesApi->add_policy_collection_to_role: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| The scope of the Role | 
 **code** | **str**| The code of the Role | 
 **add_policy_collection_to_role_request** | [**AddPolicyCollectionToRoleRequest**](AddPolicyCollectionToRoleRequest.md)| The policy collections to add | 

### Return type

[**RoleResponse**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AddPolicyCollectionToRole |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_role**
> RoleResponse create_role(role_creation_request)

CreateRole: Create Role

Creates a Role

### Example

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    RolesApi
)

async def main():

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

    # Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # role_creation_request = RoleCreationRequest.from_json("")
        # role_creation_request = RoleCreationRequest.from_dict({})
        role_creation_request = RoleCreationRequest()

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.create_role(role_creation_request, opts=opts)

            # CreateRole: Create Role
            api_response = await api_instance.create_role(role_creation_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RolesApi->create_role: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_creation_request** | [**RoleCreationRequest**](RoleCreationRequest.md)| The definition of the Role | 

### Return type

[**RoleResponse**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created Role |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_role**
> delete_role(code, scope=scope)

DeleteRole: Delete Role

Deletes an identified Role

### Example

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    RolesApi
)

async def main():

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

    # Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)
        code = 'code_example' # str | The code of the Role
        scope = 'scope_example' # str | >Optional. Will use default scope if not supplied. The scope of the Role (optional)

        try:
            # uncomment the below to set overrides at the request level
            # await api_instance.delete_role(code, scope=scope, opts=opts)

            # DeleteRole: Delete Role
            await api_instance.delete_role(code, scope=scope)        except ApiException as e:
            print("Exception when calling RolesApi->delete_role: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Role | 
 **scope** | **str**| &gt;Optional. Will use default scope if not supplied. The scope of the Role | [optional] 

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

# **get_role**
> RoleResponse get_role(code, scope=scope)

GetRole: Get Role

Gets an identified Role

### Example

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    RolesApi
)

async def main():

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

    # Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)
        code = 'code_example' # str | The code of the Role
        scope = 'scope_example' # str | Optional. Will use default scope if not supplied. The scope of the Role (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.get_role(code, scope=scope, opts=opts)

            # GetRole: Get Role
            api_response = await api_instance.get_role(code, scope=scope)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RolesApi->get_role: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Role | 
 **scope** | **str**| Optional. Will use default scope if not supplied. The scope of the Role | [optional] 

### Return type

[**RoleResponse**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested Role |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_roles**
> List[RoleResponse] list_roles(scope=scope)

ListRoles: List Roles

Gets all Roles in a scope

### Example

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    RolesApi
)

async def main():

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

    # Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)
        scope = 'scope_example' # str | Optional. Will use all scopes if not supplied. The requested scope (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.list_roles(scope=scope, opts=opts)

            # ListRoles: List Roles
            api_response = await api_instance.list_roles(scope=scope)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RolesApi->list_roles: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Optional. Will use all scopes if not supplied. The requested scope | [optional] 

### Return type

[**List[RoleResponse]**](RoleResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Roles |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **remove_policy_collection_from_role**
> RoleResponse remove_policy_collection_from_role(scope, code, policycollectionscope, policycollectioncode)

RemovePolicyCollectionFromRole: Remove policy collection from role

Removes a policy collection from a role

### Example

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    RolesApi
)

async def main():

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

    # Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)
        scope = 'scope_example' # str | The scope of the Role
        code = 'code_example' # str | The code of the Role
        policycollectionscope = 'policycollectionscope_example' # str | The scope of policy collection to remove from the Role
        policycollectioncode = 'policycollectioncode_example' # str | The code of the policy collection to remove from the Role

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.remove_policy_collection_from_role(scope, code, policycollectionscope, policycollectioncode, opts=opts)

            # RemovePolicyCollectionFromRole: Remove policy collection from role
            api_response = await api_instance.remove_policy_collection_from_role(scope, code, policycollectionscope, policycollectioncode)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RolesApi->remove_policy_collection_from_role: %s\n" % e)

asyncio.run(main())
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

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | RemovePolicyCollectionFromRole |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_role**
> RoleResponse update_role(code, role_update_request, scope=scope, before_scope=before_scope, before_code=before_code, after_scope=after_scope, after_code=after_code)

UpdateRole: Update Role

Updates a Role

### Example

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    RolesApi
)

async def main():

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

    # Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
    # By default this will read config from environment variables
    # Then from a secrets.json file found in the current working directory

    # uncomment the below to use configuration overrides
    # opts = ConfigurationOptions();
    # opts.total_timeout_ms = 30_000

    # uncomment the below to use an api client factory with overrides
    # api_client_factory = ApiClientFactory(opts=opts)

    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(RolesApi)
        code = 'code_example' # str | The code of the Role

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # role_update_request = RoleUpdateRequest.from_json("")
        # role_update_request = RoleUpdateRequest.from_dict({})
        role_update_request = RoleUpdateRequest()
        scope = 'scope_example' # str | >Optional. Will use default scope if not supplied. The scope of the Role (optional)
        before_scope = 'before_scope_example' # str | Optional. The scope of the Role. Will use default scope if not supplied. (optional)
        before_code = 'before_code_example' # str | Optional. The code of the Role (optional)
        after_scope = 'after_scope_example' # str | Optional. The scope of the Role. Will use default scope if not supplied. (optional)
        after_code = 'after_code_example' # str | Optional. The code of the Role (optional)

        try:
            # uncomment the below to set overrides at the request level
            # api_response = await api_instance.update_role(code, role_update_request, scope=scope, before_scope=before_scope, before_code=before_code, after_scope=after_scope, after_code=after_code, opts=opts)

            # UpdateRole: Update Role
            api_response = await api_instance.update_role(code, role_update_request, scope=scope, before_scope=before_scope, before_code=before_code, after_scope=after_scope, after_code=after_code)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling RolesApi->update_role: %s\n" % e)

asyncio.run(main())
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

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Role |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

