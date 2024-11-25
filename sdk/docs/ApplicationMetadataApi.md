# finbourne_access.ApplicationMetadataApi

All URIs are relative to *https://fbn-prd.lusid.com/access*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_access_controlled_resources**](ApplicationMetadataApi.md#list_access_controlled_resources) | **GET** /api/metadata/access/resources | ListAccessControlledResources: Get resources available for access control


# **list_access_controlled_resources**
> ResourceListOfAccessControlledResource list_access_controlled_resources()

ListAccessControlledResources: Get resources available for access control

Get the comprehensive set of resources that are available for access control

### Example

```python
from finbourne_access.exceptions import ApiException
from finbourne_access.extensions.configuration_options import ConfigurationOptions
from finbourne_access.models import *
from pprint import pprint
from finbourne_access import (
    SyncApiClientFactory,
    ApplicationMetadataApi
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
    api_instance = api_client_factory.build(ApplicationMetadataApi)

    try:
        # uncomment the below to set overrides at the request level
        # api_response =  api_instance.list_access_controlled_resources(opts=opts)

        # ListAccessControlledResources: Get resources available for access control
        api_response = api_instance.list_access_controlled_resources()
        pprint(api_response)

    except ApiException as e:
        print("Exception when calling ApplicationMetadataApi->list_access_controlled_resources: %s\n" % e)

main()
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceListOfAccessControlledResource**](ResourceListOfAccessControlledResource.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**0** | Error response |  -  |

[Back to top](#) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to Model list](../README.md#documentation-for-models) &#8226; [Back to README](../README.md)

