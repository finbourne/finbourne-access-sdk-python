# finbourne_access.PoliciesApi

All URIs are relative to *https://fbn-prd.lusid.com/access*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_to_policy_collection**](PoliciesApi.md#add_to_policy_collection) | **POST** /api/policycollections/{code}/add | AddToPolicyCollection: Add To PolicyCollection
[**create_policy**](PoliciesApi.md#create_policy) | **POST** /api/policies | CreatePolicy: Create Policy
[**create_policy_collection**](PoliciesApi.md#create_policy_collection) | **POST** /api/policycollections | CreatePolicyCollection: Create PolicyCollection
[**delete_policy**](PoliciesApi.md#delete_policy) | **DELETE** /api/policies/{code} | DeletePolicy: Delete Policy
[**delete_policy_collection**](PoliciesApi.md#delete_policy_collection) | **DELETE** /api/policycollections/{code} | DeletePolicyCollection: Delete PolicyCollection
[**evaluate**](PoliciesApi.md#evaluate) | **POST** /api/me | Evaluate: Run one or more evaluations
[**get_own_policies**](PoliciesApi.md#get_own_policies) | **GET** /api/me | GetOwnPolicies: Get policies of requesting user
[**get_policy**](PoliciesApi.md#get_policy) | **GET** /api/policies/{code} | GetPolicy: Get Policy
[**get_policy_collection**](PoliciesApi.md#get_policy_collection) | **GET** /api/policycollections/{code} | GetPolicyCollection: Get PolicyCollection
[**list_policies**](PoliciesApi.md#list_policies) | **GET** /api/policies | ListPolicies: List Policies
[**list_policy_collections**](PoliciesApi.md#list_policy_collections) | **GET** /api/policycollections | ListPolicyCollections: List PolicyCollections
[**page_policies**](PoliciesApi.md#page_policies) | **GET** /api/policies/page | PagePolicies: Page Policies
[**page_policy_collections**](PoliciesApi.md#page_policy_collections) | **GET** /api/policycollections/page | PagePolicyCollections: Page PolicyCollections
[**remove_from_policy_collection**](PoliciesApi.md#remove_from_policy_collection) | **POST** /api/policycollections/{code}/remove | RemoveFromPolicyCollection: Remove From PolicyCollection
[**update_policy**](PoliciesApi.md#update_policy) | **PUT** /api/policies/{code} | UpdatePolicy: Update Policy
[**update_policy_collection**](PoliciesApi.md#update_policy_collection) | **PUT** /api/policycollections/{code} | UpdatePolicyCollection: Update PolicyCollection


# **add_to_policy_collection**
> PolicyCollectionResponse add_to_policy_collection(code, add_to_policy_collection_request, scope=scope)

AddToPolicyCollection: Add To PolicyCollection

Add Policies and/or PolicyCollections to a PolicyCollection

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    code = 'code_example' # str | The code of the PolicyCollection

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # add_to_policy_collection_request = AddToPolicyCollectionRequest.from_json("")
    # add_to_policy_collection_request = AddToPolicyCollectionRequest.from_dict({})
    add_to_policy_collection_request = AddToPolicyCollectionRequest()
    scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The scope of the PolicyCollection (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.add_to_policy_collection(code, add_to_policy_collection_request, scope=scope, opts=opts)

        # AddToPolicyCollection: Add To PolicyCollection
        api_response = api_instance.add_to_policy_collection(code, add_to_policy_collection_request, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->add_to_policy_collection: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the PolicyCollection | 
 **add_to_policy_collection_request** | [**AddToPolicyCollectionRequest**](AddToPolicyCollectionRequest.md)| Ids of the PolicyCollections and/or Policies to add to the PolicyCollection | 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the PolicyCollection | [optional] 

### Return type

[**PolicyCollectionResponse**](PolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated PolicyCollection |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_policy**
> PolicyResponse create_policy(policy_creation_request)

CreatePolicy: Create Policy

Creates a Policy

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # policy_creation_request = PolicyCreationRequest.from_json("")
    # policy_creation_request = PolicyCreationRequest.from_dict({})
    policy_creation_request = PolicyCreationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_policy(policy_creation_request, opts=opts)

        # CreatePolicy: Create Policy
        api_response = api_instance.create_policy(policy_creation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->create_policy: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_creation_request** | [**PolicyCreationRequest**](PolicyCreationRequest.md)| The definition of the Policy | 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created policy |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **create_policy_collection**
> PolicyCollectionResponse create_policy_collection(policy_collection_creation_request)

CreatePolicyCollection: Create PolicyCollection

Creates a PolicyCollection

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # policy_collection_creation_request = PolicyCollectionCreationRequest.from_json("")
    # policy_collection_creation_request = PolicyCollectionCreationRequest.from_dict({})
    policy_collection_creation_request = PolicyCollectionCreationRequest()

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.create_policy_collection(policy_collection_creation_request, opts=opts)

        # CreatePolicyCollection: Create PolicyCollection
        api_response = api_instance.create_policy_collection(policy_collection_creation_request)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->create_policy_collection: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_collection_creation_request** | [**PolicyCollectionCreationRequest**](PolicyCollectionCreationRequest.md)| The definition of the PolicyCollection | 

### Return type

[**PolicyCollectionResponse**](PolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created PolicyCollection |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_policy**
> delete_policy(code, scope=scope)

DeletePolicy: Delete Policy

Deletes an identified Policy

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    code = 'code_example' # str | The code of the Policy
    scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The scope of the Policy (optional)

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.delete_policy(code, scope=scope, opts=opts)

        # DeletePolicy: Delete Policy
        api_instance.delete_policy(code, scope=scope)
    except ApiException as e:
        print("Exception when calling PoliciesApi->delete_policy: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Policy | 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the Policy | [optional] 

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

# **delete_policy_collection**
> delete_policy_collection(code, scope=scope)

DeletePolicyCollection: Delete PolicyCollection

Deletes an identified PolicyCollection

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    code = 'code_example' # str | The code of the PolicyCollection
    scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The scope of the PolicyCollection (optional)

    try:
        # uncomment the below to set overrides at the request level
        #  api_instance.delete_policy_collection(code, scope=scope, opts=opts)

        # DeletePolicyCollection: Delete PolicyCollection
        api_instance.delete_policy_collection(code, scope=scope)
    except ApiException as e:
        print("Exception when calling PoliciesApi->delete_policy_collection: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the PolicyCollection | 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the PolicyCollection | [optional] 

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

# **evaluate**
> Dict[str, EvaluationResponse] evaluate(request_body, applications=applications)

Evaluate: Run one or more evaluations

Given a dictionary of evaluation requests (keyed by any arbitrary correlation identifier), each will be evaluated according to the current user's policies (deduced from the provided OAuth token).

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    request_body = {"data-access-page-evaluation":{"request":{"action":{"entityCode":"WebSitePage","scope":"FINBOURNE","activity":"SeeAdminControls"},"toEffectiveDate":"2018-12-08T13:30:00.0000000+00:00","toAsAt":"2018-12-31T11:00:00.0000000+00:00"},"resource":{"id":{"scope":"FINBOURNE","code":"DataAccessPage"},"metadata":{"RequiredLicence":[{"provider":"WebsiteAccess","value":"FINBOURNE"}]}}}} # Dict[str, EvaluationRequest] | A dictionary of evaluations, keyed using any arbitrary correlation id (it will be returned with the response for that evaluation).
    applications = ['applications_example'] # List[str] | Optional. The application type of the roles and policies to use when evaluating. (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.evaluate(request_body, applications=applications, opts=opts)

        # Evaluate: Run one or more evaluations
        api_response = api_instance.evaluate(request_body, applications=applications)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->evaluate: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, EvaluationRequest]**](EvaluationRequest.md)| A dictionary of evaluations, keyed using any arbitrary correlation id (it will be returned with the response for that evaluation). | 
 **applications** | [**List[str]**](str.md)| Optional. The application type of the roles and policies to use when evaluating. | [optional] 

### Return type

[**Dict[str, EvaluationResponse]**](EvaluationResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Run an evaluation against the current user&#39;s entitlements |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_own_policies**
> List[AttachedPolicyDefinitionResponse] get_own_policies(applications=applications)

GetOwnPolicies: Get policies of requesting user

Gets all Policies for the current user

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    applications = ['applications_example'] # List[str] | Optional. Filter on the applications that the policies apply to (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_own_policies(applications=applications, opts=opts)

        # GetOwnPolicies: Get policies of requesting user
        api_response = api_instance.get_own_policies(applications=applications)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->get_own_policies: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applications** | [**List[str]**](str.md)| Optional. Filter on the applications that the policies apply to | [optional] 

### Return type

[**List[AttachedPolicyDefinitionResponse]**](AttachedPolicyDefinitionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get policies and licences of current user |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_policy**
> PolicyResponse get_policy(code, scope=scope)

GetPolicy: Get Policy

Gets an identified Policy

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    code = 'code_example' # str | The code of the Policy
    scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The scope of the Policy (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_policy(code, scope=scope, opts=opts)

        # GetPolicy: Get Policy
        api_response = api_instance.get_policy(code, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->get_policy: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Policy | 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the Policy | [optional] 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a specific Policy |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_policy_collection**
> PolicyCollectionResponse get_policy_collection(code, scope=scope)

GetPolicyCollection: Get PolicyCollection

Gets an identified PolicyCollection

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    code = 'code_example' # str | The code of the PolicyCollection
    scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The scope of the PolicyCollection (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.get_policy_collection(code, scope=scope, opts=opts)

        # GetPolicyCollection: Get PolicyCollection
        api_response = api_instance.get_policy_collection(code, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->get_policy_collection: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the PolicyCollection | 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the PolicyCollection | [optional] 

### Return type

[**PolicyCollectionResponse**](PolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested PolicyCollection |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_policies**
> List[PolicyResponse] list_policies(scope=scope)

ListPolicies: List Policies

Gets all Policies in a scope. For pagination support, use PagePolicies.

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The requested scope (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_policies(scope=scope, opts=opts)

        # ListPolicies: List Policies
        api_response = api_instance.list_policies(scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->list_policies: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Optional. Will use the default scope if not provided. The requested scope | [optional] 

### Return type

[**List[PolicyResponse]**](PolicyResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Policies |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_policy_collections**
> List[PolicyCollectionResponse] list_policy_collections(scope=scope)

ListPolicyCollections: List PolicyCollections

Gets all PolicyCollections in a scope. For pagination support, use PagePolicyCollections

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The requested scope (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_policy_collections(scope=scope, opts=opts)

        # ListPolicyCollections: List PolicyCollections
        api_response = api_instance.list_policy_collections(scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->list_policy_collections: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Optional. Will use the default scope if not provided. The requested scope | [optional] 

### Return type

[**List[PolicyCollectionResponse]**](PolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested list of PolicyCollections |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **page_policies**
> ResourceListOfPolicyResponse page_policies(sort_by=sort_by, limit=limit, filter=filter, page=page)

PagePolicies: Page Policies

Gets all Policies with pagination support.

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    sort_by = 'sort_by_example' # str | Optional. Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName (optional)
    limit = 56 # int | Optional. 2000 if not provided. When paginating, limit the number of returned results to this many (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
    page = 'page_example' # str | Optional. Paging token returned from a previous result (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.page_policies(sort_by=sort_by, limit=limit, filter=filter, page=page, opts=opts)

        # PagePolicies: Page Policies
        api_response = api_instance.page_policies(sort_by=sort_by, limit=limit, filter=filter, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->page_policies: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Optional. Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. 2000 if not provided. When paginating, limit the number of returned results to this many | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **page** | **str**| Optional. Paging token returned from a previous result | [optional] 

### Return type

[**ResourceListOfPolicyResponse**](ResourceListOfPolicyResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested list of Policies |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **page_policy_collections**
> ResourceListOfPolicyCollectionResponse page_policy_collections(sort_by=sort_by, limit=limit, filter=filter, page=page)

PagePolicyCollections: Page PolicyCollections

Gets all PolicyCollections with pagination support.

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    sort_by = 'sort_by_example' # str | Optional. Order the results by these fields. Use the '-' sign to denote descending order e.g. -MyFieldName (optional)
    limit = 56 # int | Optional. 2000 if not provided. When paginating, limit the number of returned results to this many (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
    page = 'page_example' # str | Optional. Paging token returned from a previous result (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.page_policy_collections(sort_by=sort_by, limit=limit, filter=filter, page=page, opts=opts)

        # PagePolicyCollections: Page PolicyCollections
        api_response = api_instance.page_policy_collections(sort_by=sort_by, limit=limit, filter=filter, page=page)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->page_policy_collections: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_by** | **str**| Optional. Order the results by these fields. Use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. 2000 if not provided. When paginating, limit the number of returned results to this many | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **page** | **str**| Optional. Paging token returned from a previous result | [optional] 

### Return type

[**ResourceListOfPolicyCollectionResponse**](ResourceListOfPolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested list of PolicyCollections |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **remove_from_policy_collection**
> PolicyCollectionResponse remove_from_policy_collection(code, remove_from_policy_collection_request, scope=scope)

RemoveFromPolicyCollection: Remove From PolicyCollection

Remove Policies and/or PolicyCollections from a PolicyCollection

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    code = 'code_example' # str | The code of the PolicyCollection

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # remove_from_policy_collection_request = RemoveFromPolicyCollectionRequest.from_json("")
    # remove_from_policy_collection_request = RemoveFromPolicyCollectionRequest.from_dict({})
    remove_from_policy_collection_request = RemoveFromPolicyCollectionRequest()
    scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The scope of the PolicyCollection (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.remove_from_policy_collection(code, remove_from_policy_collection_request, scope=scope, opts=opts)

        # RemoveFromPolicyCollection: Remove From PolicyCollection
        api_response = api_instance.remove_from_policy_collection(code, remove_from_policy_collection_request, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->remove_from_policy_collection: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the PolicyCollection | 
 **remove_from_policy_collection_request** | [**RemoveFromPolicyCollectionRequest**](RemoveFromPolicyCollectionRequest.md)| Ids of the PolicyCollections and/or Policies to remove from the PolicyCollection | 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the PolicyCollection | [optional] 

### Return type

[**PolicyCollectionResponse**](PolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated PolicyCollection |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_policy**
> PolicyResponse update_policy(code, policy_update_request, scope=scope)

UpdatePolicy: Update Policy

Updates a Policy

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    code = 'code_example' # str | The code of the Policy

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # policy_update_request = PolicyUpdateRequest.from_json("")
    # policy_update_request = PolicyUpdateRequest.from_dict({})
    policy_update_request = PolicyUpdateRequest()
    scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The scope of the Policy (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_policy(code, policy_update_request, scope=scope, opts=opts)

        # UpdatePolicy: Update Policy
        api_response = api_instance.update_policy(code, policy_update_request, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->update_policy: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Policy | 
 **policy_update_request** | [**PolicyUpdateRequest**](PolicyUpdateRequest.md)| The updated definition of the Policy | 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the Policy | [optional] 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated policy |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_policy_collection**
> PolicyCollectionResponse update_policy_collection(code, policy_collection_update_request, scope=scope)

UpdatePolicyCollection: Update PolicyCollection

Updates a PolicyCollection

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    PoliciesApi
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
    api_instance = api_client_factory.build(PoliciesApi)
    code = 'code_example' # str | The code of the PolicyCollection

    # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
    # Change the lines below to switch approach
    # policy_collection_update_request = PolicyCollectionUpdateRequest.from_json("")
    # policy_collection_update_request = PolicyCollectionUpdateRequest.from_dict({})
    policy_collection_update_request = PolicyCollectionUpdateRequest()
    scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The scope of the PolicyCollection (optional)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.update_policy_collection(code, policy_collection_update_request, scope=scope, opts=opts)

        # UpdatePolicyCollection: Update PolicyCollection
        api_response = api_instance.update_policy_collection(code, policy_collection_update_request, scope=scope)
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling PoliciesApi->update_policy_collection: %s\n" % e)

main()
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the PolicyCollection | 
 **policy_collection_update_request** | [**PolicyCollectionUpdateRequest**](PolicyCollectionUpdateRequest.md)| The updated definition of the PolicyCollection | 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the PolicyCollection | [optional] 

### Return type

[**PolicyCollectionResponse**](PolicyCollectionResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated PolicyCollection |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

