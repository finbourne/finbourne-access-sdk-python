# ResourceDetails

Details about the resource being requested that may be pertinent to the entitlement evaluation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Dict[str, str]** | The identifier of the resource being evaluated | 
**metadata** | **Dict[str, List[EntitlementMetadata]]** | Any metadata associated with the resource being requested | [optional] 

## Example

```python
from finbourne_access.models.resource_details import ResourceDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceDetails from a JSON string
resource_details_instance = ResourceDetails.from_json(json)
# print the JSON string representation of the object
print ResourceDetails.to_json()

# convert the object into a dict
resource_details_dict = resource_details_instance.to_dict()
# create an instance of ResourceDetails from a dict
resource_details_form_dict = resource_details.from_dict(resource_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


