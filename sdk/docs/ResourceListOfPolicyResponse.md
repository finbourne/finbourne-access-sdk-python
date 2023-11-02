# ResourceListOfPolicyResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[PolicyResponse]**](PolicyResponse.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from finbourne_access.models.resource_list_of_policy_response import ResourceListOfPolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfPolicyResponse from a JSON string
resource_list_of_policy_response_instance = ResourceListOfPolicyResponse.from_json(json)
# print the JSON string representation of the object
print ResourceListOfPolicyResponse.to_json()

# convert the object into a dict
resource_list_of_policy_response_dict = resource_list_of_policy_response_instance.to_dict()
# create an instance of ResourceListOfPolicyResponse from a dict
resource_list_of_policy_response_form_dict = resource_list_of_policy_response.from_dict(resource_list_of_policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


