# finbourne_access.PolicyTemplatesApi

All URIs are relative to *https://fbn-prd.lusid.com/access*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy_template**](PolicyTemplatesApi.md#create_policy_template) | **POST** /api/policytemplates | [EXPERIMENTAL] CreatePolicyTemplate: Create a Policy Template
[**delete_policy_template**](PolicyTemplatesApi.md#delete_policy_template) | **DELETE** /api/policytemplates/{code} | [EXPERIMENTAL] DeletePolicyTemplate: Deleting a policy template
[**generate_policy_from_template**](PolicyTemplatesApi.md#generate_policy_from_template) | **POST** /api/policytemplates/$generatepolicy | [EXPERIMENTAL] GeneratePolicyFromTemplate: Generate policy from template
[**get_policy_template**](PolicyTemplatesApi.md#get_policy_template) | **GET** /api/policytemplates/{code} | [EXPERIMENTAL] GetPolicyTemplate: Retrieving one Policy Template
[**list_policy_templates**](PolicyTemplatesApi.md#list_policy_templates) | **GET** /api/policytemplates | [EXPERIMENTAL] ListPolicyTemplates: List Policy Templates
[**update_policy_template**](PolicyTemplatesApi.md#update_policy_template) | **PUT** /api/policytemplates/{code} | [EXPERIMENTAL] UpdatePolicyTemplate: Update a Policy Template


# **create_policy_template**
> PolicyTemplateResponse create_policy_template(policy_template_creation_request)

[EXPERIMENTAL] CreatePolicyTemplate: Create a Policy Template

Creates a Policy Template

### Example

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    PolicyTemplatesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PolicyTemplatesApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # policy_template_creation_request = PolicyTemplateCreationRequest()
        # policy_template_creation_request = PolicyTemplateCreationRequest.from_json("")
        policy_template_creation_request = PolicyTemplateCreationRequest.from_dict({"code":"official-portfolios-read-only","displayName":"updated-policy-template","description":"Example policy template for a policy that grants access to some resource","templatedSelectors":[{"application":"LUSID","tag":"Data","selector":{"idSelectorDefinition":{"identifier":{"scope":"official"},"actions":[{"scope":"default","activity":"Read","entity":"Portfolio"},{"scope":"default","activity":"Aggregate","entity":"Portfolio"}],"name":"access-official-scope","description":"Allow readonly access to the 'official' scope"}}}]}) # PolicyTemplateCreationRequest | The definition of the policy template

        try:
            # [EXPERIMENTAL] CreatePolicyTemplate: Create a Policy Template
            api_response = await api_instance.create_policy_template(policy_template_creation_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PolicyTemplatesApi->create_policy_template: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_template_creation_request** | [**PolicyTemplateCreationRequest**](PolicyTemplateCreationRequest.md)| The definition of the policy template | 

### Return type

[**PolicyTemplateResponse**](PolicyTemplateResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created Policy Template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **delete_policy_template**
> delete_policy_template(code, scope=scope)

[EXPERIMENTAL] DeletePolicyTemplate: Deleting a policy template

Deletes an identified Policy Template

### Example

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    PolicyTemplatesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PolicyTemplatesApi)
        code = 'code_example' # str | The code of the Policy Template
        scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The scope of the Policy Template (optional)

        try:
            # [EXPERIMENTAL] DeletePolicyTemplate: Deleting a policy template
            await api_instance.delete_policy_template(code, scope=scope)        except ApiException as e:
            print("Exception when calling PolicyTemplatesApi->delete_policy_template: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Policy Template | 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the Policy Template | [optional] 

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

# **generate_policy_from_template**
> GeneratedPolicyComponents generate_policy_from_template(generate_policy_from_template_request, as_at=as_at)

[EXPERIMENTAL] GeneratePolicyFromTemplate: Generate policy from template

Generates policies from templates

### Example

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    PolicyTemplatesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PolicyTemplatesApi)

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # generate_policy_from_template_request = GeneratePolicyFromTemplateRequest()
        # generate_policy_from_template_request = GeneratePolicyFromTemplateRequest.from_json("")
        generate_policy_from_template_request = GeneratePolicyFromTemplateRequest.from_dict({"templateSelection":[{"scope":"default","code":"example-policy-template","selectorTags":["Data","Api"]}]}) # GeneratePolicyFromTemplateRequest | Definition of the generate request
        as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date time of the data (optional)

        try:
            # [EXPERIMENTAL] GeneratePolicyFromTemplate: Generate policy from template
            api_response = await api_instance.generate_policy_from_template(generate_policy_from_template_request, as_at=as_at)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PolicyTemplatesApi->generate_policy_from_template: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_policy_from_template_request** | [**GeneratePolicyFromTemplateRequest**](GeneratePolicyFromTemplateRequest.md)| Definition of the generate request | 
 **as_at** | **datetime**| Optional. The AsAt date time of the data | [optional] 

### Return type

[**GeneratedPolicyComponents**](GeneratedPolicyComponents.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **get_policy_template**
> PolicyTemplateResponse get_policy_template(code, as_at=as_at, scope=scope)

[EXPERIMENTAL] GetPolicyTemplate: Retrieving one Policy Template

Gets an identified Policy Template

### Example

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    PolicyTemplatesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PolicyTemplatesApi)
        code = 'code_example' # str | The code of the Policy Template
        as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date time of the data. If not specified defaults to current time (optional)
        scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The scope of the Policy Template (optional)

        try:
            # [EXPERIMENTAL] GetPolicyTemplate: Retrieving one Policy Template
            api_response = await api_instance.get_policy_template(code, as_at=as_at, scope=scope)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PolicyTemplatesApi->get_policy_template: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Policy Template | 
 **as_at** | **datetime**| Optional. The AsAt date time of the data. If not specified defaults to current time | [optional] 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the Policy Template | [optional] 

### Return type

[**PolicyTemplateResponse**](PolicyTemplateResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a specific Policy Template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **list_policy_templates**
> ResourceListOfPolicyTemplateResponse list_policy_templates(as_at=as_at, sort_by=sort_by, limit=limit, filter=filter, page=page)

[EXPERIMENTAL] ListPolicyTemplates: List Policy Templates

Gets all Policy Templates with pagination support.

### Example

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    PolicyTemplatesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PolicyTemplatesApi)
        as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date time of the data (optional)
        sort_by = 'sort_by_example' # str | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
        limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
        filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
        page = 'page_example' # str | Optional. Paging token returned from a previous result (optional)

        try:
            # [EXPERIMENTAL] ListPolicyTemplates: List Policy Templates
            api_response = await api_instance.list_policy_templates(as_at=as_at, sort_by=sort_by, limit=limit, filter=filter, page=page)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PolicyTemplatesApi->list_policy_templates: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **as_at** | **datetime**| Optional. The AsAt date time of the data | [optional] 
 **sort_by** | **str**| Optional. Order the results by these fields. Use use the &#39;-&#39; sign to denote descending order e.g. -MyFieldName | [optional] 
 **limit** | **int**| Optional. When paginating, limit the number of returned results to this many. | [optional] 
 **filter** | **str**| Optional. Expression to filter the result set | [optional] 
 **page** | **str**| Optional. Paging token returned from a previous result | [optional] 

### Return type

[**ResourceListOfPolicyTemplateResponse**](ResourceListOfPolicyTemplateResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Policy Templates |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

# **update_policy_template**
> PolicyTemplateResponse update_policy_template(code, policy_template_update_request=policy_template_update_request)

[EXPERIMENTAL] UpdatePolicyTemplate: Update a Policy Template

Updates an identified Policy Template

### Example

```python
import asyncio
from finbourne_access.exceptions import ApiException
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    ApiClientFactory,
    PolicyTemplatesApi
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
    api_client_factory = ApiClientFactory()

    # Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
    async with api_client_factory:
        # Create an instance of the API class
        api_instance = api_client_factory.build(PolicyTemplatesApi)
        code = 'code_example' # str | Code of the policy template to update

        # Objects can be created either via the class constructor, or using the 'from_dict' or 'from_json' methods
        # Change the lines below to switch approach
        # policy_template_update_request = PolicyTemplateUpdateRequest()
        # policy_template_update_request = PolicyTemplateUpdateRequest.from_json("")
        policy_template_update_request = PolicyTemplateUpdateRequest.from_dict(finbourne_access.PolicyTemplateUpdateRequest()) # PolicyTemplateUpdateRequest | Definition of the updated policy template (optional)

        try:
            # [EXPERIMENTAL] UpdatePolicyTemplate: Update a Policy Template
            api_response = await api_instance.update_policy_template(code, policy_template_update_request=policy_template_update_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling PolicyTemplatesApi->update_policy_template: %s\n" % e)

asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the policy template to update | 
 **policy_template_update_request** | [**PolicyTemplateUpdateRequest**](PolicyTemplateUpdateRequest.md)| Definition of the updated policy template | [optional] 

### Return type

[**PolicyTemplateResponse**](PolicyTemplateResponse.md)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Policy Template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

