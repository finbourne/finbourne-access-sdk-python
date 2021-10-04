# finbourne_access.LicencesApi

All URIs are relative to *https://fbn-ci.lusid.com/access*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_licence**](LicencesApi.md#create_licence) | **POST** /api/licences | [EXPERIMENTAL] CreateLicence: Create a Licence
[**create_licence_assignment**](LicencesApi.md#create_licence_assignment) | **PUT** /api/licences/{code}/assignments/{tenant} | [EXPERIMENTAL] CreateLicenceAssignment: Assign Licence
[**delete_licence**](LicencesApi.md#delete_licence) | **DELETE** /api/licences/{code} | [EXPERIMENTAL] DeleteLicence: Delete Licence
[**delete_licence_assignment**](LicencesApi.md#delete_licence_assignment) | **DELETE** /api/licences/{code}/assignments/{tenant} | [EXPERIMENTAL] DeleteLicenceAssignment: Unassign Licence
[**get_licence**](LicencesApi.md#get_licence) | **GET** /api/licences/{code} | [EXPERIMENTAL] GetLicence: Get Licence
[**list_assignments**](LicencesApi.md#list_assignments) | **GET** /api/licences/{code}/assignments | [EXPERIMENTAL] ListAssignments: List Assignments
[**list_licences**](LicencesApi.md#list_licences) | **GET** /api/licences | [EXPERIMENTAL] ListLicences: List Licences
[**update_licence**](LicencesApi.md#update_licence) | **PUT** /api/licences/{code} | [EXPERIMENTAL] UpdateLicence: Update Licence


# **create_licence**
> PolicyResponse create_licence(licence_creation_request)

[EXPERIMENTAL] CreateLicence: Create a Licence

Creates an unassigned Licence policy

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
    api_instance = finbourne_access.LicencesApi(api_client)
    licence_creation_request = {"code":"dataset-licence-1","description":"Access to licensed dataset","applications":["LUSID"],"selectors":[{"code":"dataset-licence-1","actionIds":[{"scope":"default","activity":"Read","entity":"Portfolio"}]}],"when":{"activate":"2016-08-31T18:00:00.0000000+00:00","deactivate":"2020-08-31T18:00:00.0000000+00:00"}} # LicenceCreationRequest | The Licence definition

    try:
        # [EXPERIMENTAL] CreateLicence: Create a Licence
        api_response = api_instance.create_licence(licence_creation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicencesApi->create_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **licence_creation_request** | [**LicenceCreationRequest**](LicenceCreationRequest.md)| The Licence definition | 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a new Licence |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_licence_assignment**
> PolicyResponse create_licence_assignment(code, tenant)

[EXPERIMENTAL] CreateLicenceAssignment: Assign Licence

Create a licence assignment to another, authorised, tenant

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
    api_instance = finbourne_access.LicencesApi(api_client)
    code = 'code_example' # str | Code of the Licence
tenant = 'tenant_example' # str | Name of the tenant to be shared with

    try:
        # [EXPERIMENTAL] CreateLicenceAssignment: Assign Licence
        api_response = api_instance.create_licence_assignment(code, tenant)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicencesApi->create_licence_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the Licence | 
 **tenant** | **str**| Name of the tenant to be shared with | 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Assign a Licence to a tenant |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_licence**
> delete_licence(code, scope=scope)

[EXPERIMENTAL] DeleteLicence: Delete Licence

Deletes an identified Licence

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
    api_instance = finbourne_access.LicencesApi(api_client)
    code = 'code_example' # str | The code of the Licence
scope = 'scope_example' # str | Optional. Will use the client name if not provided. The scope of the Licence (optional)

    try:
        # [EXPERIMENTAL] DeleteLicence: Delete Licence
        api_instance.delete_licence(code, scope=scope)
    except ApiException as e:
        print("Exception when calling LicencesApi->delete_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Licence | 
 **scope** | **str**| Optional. Will use the client name if not provided. The scope of the Licence | [optional] 

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

# **delete_licence_assignment**
> delete_licence_assignment(code, tenant)

[EXPERIMENTAL] DeleteLicenceAssignment: Unassign Licence

Remove a Licence assignment from a tenant

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
    api_instance = finbourne_access.LicencesApi(api_client)
    code = 'code_example' # str | Code of the Licence
tenant = 'tenant_example' # str | Name of the tenant to be shared with

    try:
        # [EXPERIMENTAL] DeleteLicenceAssignment: Unassign Licence
        api_instance.delete_licence_assignment(code, tenant)
    except ApiException as e:
        print("Exception when calling LicencesApi->delete_licence_assignment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the Licence | 
 **tenant** | **str**| Name of the tenant to be shared with | 

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

# **get_licence**
> PolicyResponse get_licence(code, as_at=as_at, scope=scope)

[EXPERIMENTAL] GetLicence: Get Licence

Gets an identified Licence

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
    api_instance = finbourne_access.LicencesApi(api_client)
    code = 'code_example' # str | The code of the Licence
as_at = '2013-10-20T19:20:30+01:00' # datetime | Optional. The AsAt date time of the data (optional)
scope = 'scope_example' # str | Optional. Will use the default client name if not provided. The scope of the Licence (optional)

    try:
        # [EXPERIMENTAL] GetLicence: Get Licence
        api_response = api_instance.get_licence(code, as_at=as_at, scope=scope)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicencesApi->get_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Licence | 
 **as_at** | **datetime**| Optional. The AsAt date time of the data | [optional] 
 **scope** | **str**| Optional. Will use the default client name if not provided. The scope of the Licence | [optional] 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a specific Licence |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assignments**
> list[str] list_assignments(code)

[EXPERIMENTAL] ListAssignments: List Assignments

List tenants the specified Licence is assigned to

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
    api_instance = finbourne_access.LicencesApi(api_client)
    code = 'code_example' # str | Code of the Licence

    try:
        # [EXPERIMENTAL] ListAssignments: List Assignments
        api_response = api_instance.list_assignments(code)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicencesApi->list_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Code of the Licence | 

### Return type

**list[str]**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get the list of tenants assigned to a licence |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_licences**
> list[PolicyResponse] list_licences(assigned_to=assigned_to)

[EXPERIMENTAL] ListLicences: List Licences

Gets all Licences in a scope

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
    api_instance = finbourne_access.LicencesApi(api_client)
    assigned_to = 'assigned_to_example' # str | Optional. If specified, applies a filter for only Licences that are assigned to the specified tenant (optional)

    try:
        # [EXPERIMENTAL] ListLicences: List Licences
        api_response = api_instance.list_licences(assigned_to=assigned_to)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicencesApi->list_licences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assigned_to** | **str**| Optional. If specified, applies a filter for only Licences that are assigned to the specified tenant | [optional] 

### Return type

[**list[PolicyResponse]**](PolicyResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All of the licences in a scope |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_licence**
> PolicyResponse update_licence(code, licence_update_request)

[EXPERIMENTAL] UpdateLicence: Update Licence

Update an existing Licence policy

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
    api_instance = finbourne_access.LicencesApi(api_client)
    code = 'code_example' # str | The code of the Licence
licence_update_request = {"description":"Access to licensed dataset","applications":["LUSID"],"selectors":[{"code":"dataset-licence-1","actionIds":[{"scope":"default","activity":"Read","entity":"Portfolio"}]}],"when":{"activate":"2016-08-31T18:00:00.0000000+00:00","deactivate":"2020-08-31T18:00:00.0000000+00:00"}} # LicenceUpdateRequest | The Licence definition

    try:
        # [EXPERIMENTAL] UpdateLicence: Update Licence
        api_response = api_instance.update_licence(code, licence_update_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling LicencesApi->update_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code of the Licence | 
 **licence_update_request** | [**LicenceUpdateRequest**](LicenceUpdateRequest.md)| The Licence definition | 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update a specific Licence |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

