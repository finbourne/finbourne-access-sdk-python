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

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from finbourne_access.models.policy_template_creation_request import PolicyTemplateCreationRequest
from finbourne_access.models.policy_template_response import PolicyTemplateResponse
from pprint import pprint

import os
from finbourne_access import (
    ApiClientFactory,
    PolicyTemplatesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/access"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_access.PolicyTemplatesApi)
    policy_template_creation_request = {"code":"official-portfolios-read-only","displayName":"updated-policy-template","description":"Example policy template for a policy that grants access to some resource","templatedSelectors":[{"application":"LUSID","tag":"Data","selector":{"idSelectorDefinition":{"identifier":{"scope":"official"},"actions":[{"scope":"default","activity":"Read","entity":"Portfolio"},{"scope":"default","activity":"Aggregate","entity":"Portfolio"}],"name":"access-official-scope","description":"Allow readonly access to the 'official' scope"}}}]} # PolicyTemplateCreationRequest | The definition of the policy template

    try:
        # [EXPERIMENTAL] CreatePolicyTemplate: Create a Policy Template
        api_response = await api_instance.create_policy_template(policy_template_creation_request)
        print("The response of PolicyTemplatesApi->create_policy_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplatesApi->create_policy_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_template_creation_request** | [**PolicyTemplateCreationRequest**](PolicyTemplateCreationRequest.md)| The definition of the policy template | 

### Return type

[**PolicyTemplateResponse**](PolicyTemplateResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created Policy Template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy_template**
> delete_policy_template(code, scope=scope)

[EXPERIMENTAL] DeletePolicyTemplate: Deleting a policy template

Deletes an identified Policy Template

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from pprint import pprint

import os
from finbourne_access import (
    ApiClientFactory,
    PolicyTemplatesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/access"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_access.PolicyTemplatesApi)
    code = 'code_example' # str | The code of the Policy Template
    scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The scope of the Policy Template (optional)

    try:
        # [EXPERIMENTAL] DeletePolicyTemplate: Deleting a policy template
        await api_instance.delete_policy_template(code, scope=scope)
    except Exception as e:
        print("Exception when calling PolicyTemplatesApi->delete_policy_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Policy Template | 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the Policy Template | [optional] 

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

# **generate_policy_from_template**
> GeneratedPolicyComponents generate_policy_from_template(generate_policy_from_template_request, as_at=as_at)

[EXPERIMENTAL] GeneratePolicyFromTemplate: Generate policy from template

Generates policies from templates

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from finbourne_access.models.generate_policy_from_template_request import GeneratePolicyFromTemplateRequest
from finbourne_access.models.generated_policy_components import GeneratedPolicyComponents
from pprint import pprint

import os
from finbourne_access import (
    ApiClientFactory,
    PolicyTemplatesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/access"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_access.PolicyTemplatesApi)
    generate_policy_from_template_request = {"templateSelection":[{"scope":"default","code":"example-policy-template","selectorTags":["Data","Api"]}]} # GeneratePolicyFromTemplateRequest | Definition of the generate request
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date time of the data (optional)

    try:
        # [EXPERIMENTAL] GeneratePolicyFromTemplate: Generate policy from template
        api_response = await api_instance.generate_policy_from_template(generate_policy_from_template_request, as_at=as_at)
        print("The response of PolicyTemplatesApi->generate_policy_from_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplatesApi->generate_policy_from_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_policy_from_template_request** | [**GeneratePolicyFromTemplateRequest**](GeneratePolicyFromTemplateRequest.md)| Definition of the generate request | 
 **as_at** | **datetime**| Optional. The AsAt date time of the data | [optional] 

### Return type

[**GeneratedPolicyComponents**](GeneratedPolicyComponents.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy_template**
> PolicyTemplateResponse get_policy_template(code, as_at=as_at, scope=scope)

[EXPERIMENTAL] GetPolicyTemplate: Retrieving one Policy Template

Gets an identified Policy Template

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from finbourne_access.models.policy_template_response import PolicyTemplateResponse
from pprint import pprint

import os
from finbourne_access import (
    ApiClientFactory,
    PolicyTemplatesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/access"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_access.PolicyTemplatesApi)
    code = 'code_example' # str | The code of the Policy Template
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date time of the data. If not specified defaults to current time (optional)
    scope = 'scope_example' # str | Optional. Will use the default scope if not provided. The scope of the Policy Template (optional)

    try:
        # [EXPERIMENTAL] GetPolicyTemplate: Retrieving one Policy Template
        api_response = await api_instance.get_policy_template(code, as_at=as_at, scope=scope)
        print("The response of PolicyTemplatesApi->get_policy_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplatesApi->get_policy_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Policy Template | 
 **as_at** | **datetime**| Optional. The AsAt date time of the data. If not specified defaults to current time | [optional] 
 **scope** | **str**| Optional. Will use the default scope if not provided. The scope of the Policy Template | [optional] 

### Return type

[**PolicyTemplateResponse**](PolicyTemplateResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a specific Policy Template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policy_templates**
> ResourceListOfPolicyTemplateResponse list_policy_templates(as_at=as_at, sort_by=sort_by, limit=limit, filter=filter, page=page)

[EXPERIMENTAL] ListPolicyTemplates: List Policy Templates

Gets all Policy Templates with pagination support.

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from finbourne_access.models.resource_list_of_policy_template_response import ResourceListOfPolicyTemplateResponse
from pprint import pprint

import os
from finbourne_access import (
    ApiClientFactory,
    PolicyTemplatesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/access"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_access.PolicyTemplatesApi)
    as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date time of the data (optional)
    sort_by = 'sort_by_example' # str | Optional. Order the results by these fields. Use use the '-' sign to denote descending order e.g. -MyFieldName (optional)
    limit = 56 # int | Optional. When paginating, limit the number of returned results to this many. (optional)
    filter = 'filter_example' # str | Optional. Expression to filter the result set (optional)
    page = 'page_example' # str | Optional. Paging token returned from a previous result (optional)

    try:
        # [EXPERIMENTAL] ListPolicyTemplates: List Policy Templates
        api_response = await api_instance.list_policy_templates(as_at=as_at, sort_by=sort_by, limit=limit, filter=filter, page=page)
        print("The response of PolicyTemplatesApi->list_policy_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplatesApi->list_policy_templates: %s\n" % e)
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

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Policy Templates |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy_template**
> PolicyTemplateResponse update_policy_template(code, policy_template_update_request=policy_template_update_request)

[EXPERIMENTAL] UpdatePolicyTemplate: Update a Policy Template

Updates an identified Policy Template

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import finbourne_access
from finbourne_access.rest import ApiException
from finbourne_access.models.policy_template_response import PolicyTemplateResponse
from finbourne_access.models.policy_template_update_request import PolicyTemplateUpdateRequest
from pprint import pprint

import os
from finbourne_access import (
    ApiClientFactory,
    PolicyTemplatesApi,
    EnvironmentVariablesConfigurationLoader,
    SecretsFileConfigurationLoader,
    ArgsConfigurationLoader
)

# Use the finbourne_access ApiClientFactory to build Api instances with a configured api client
# By default this will read config from environment variables
# Then from a secrets.json file found in the current working directory
api_client_factory = ApiClientFactory()

# The ApiClientFactory can be passed an iterable of configuration loaders to read configuration from

api_url = "https://fbn-prd.lusid.com/access"
# Path to a secrets.json file containing authentication credentials
# See https://support.lusid.com/knowledgebase/article/KA-01667/en-us
# for a detailed guide to setting up the SDK make authenticated calls to LUSID APIs
secrets_path = os.getenv("FBN_SECRETS_PATH")
app_name="LusidJupyterNotebook"

config_loaders = [
	EnvironmentVariablesConfigurationLoader(),
	SecretsFileConfigurationLoader(api_secrets_file=secrets_path),
	ArgsConfigurationLoader(api_url=api_url, app_name=app_name)
]
api_client_factory = ApiClientFactory(config_loaders=config_loaders)


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.



# Enter a context with an instance of the ApiClientFactory to ensure the connection pool is closed after use
async with api_client_factory:
    # Create an instance of the API class
    api_instance = api_client_factory.build(finbourne_access.PolicyTemplatesApi)
    code = 'code_example' # str | Code of the policy template to update
    policy_template_update_request = finbourne_access.PolicyTemplateUpdateRequest() # PolicyTemplateUpdateRequest | Definition of the updated policy template (optional)

    try:
        # [EXPERIMENTAL] UpdatePolicyTemplate: Update a Policy Template
        api_response = await api_instance.update_policy_template(code, policy_template_update_request=policy_template_update_request)
        print("The response of PolicyTemplatesApi->update_policy_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PolicyTemplatesApi->update_policy_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the policy template to update | 
 **policy_template_update_request** | [**PolicyTemplateUpdateRequest**](PolicyTemplateUpdateRequest.md)| Definition of the updated policy template | [optional] 

### Return type

[**PolicyTemplateResponse**](PolicyTemplateResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated Policy Template |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

