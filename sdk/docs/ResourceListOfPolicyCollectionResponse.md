# ResourceListOfPolicyCollectionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[PolicyCollectionResponse]**](PolicyCollectionResponse.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from finbourne_access.models.resource_list_of_policy_collection_response import ResourceListOfPolicyCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfPolicyCollectionResponse from a JSON string
resource_list_of_policy_collection_response_instance = ResourceListOfPolicyCollectionResponse.from_json(json)
# print the JSON string representation of the object
print ResourceListOfPolicyCollectionResponse.to_json()

# convert the object into a dict
resource_list_of_policy_collection_response_dict = resource_list_of_policy_collection_response_instance.to_dict()
# create an instance of ResourceListOfPolicyCollectionResponse from a dict
resource_list_of_policy_collection_response_form_dict = resource_list_of_policy_collection_response.from_dict(resource_list_of_policy_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


