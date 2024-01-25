# ResourceListOfPolicyTemplateResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[PolicyTemplateResponse]**](PolicyTemplateResponse.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from finbourne_access.models.resource_list_of_policy_template_response import ResourceListOfPolicyTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfPolicyTemplateResponse from a JSON string
resource_list_of_policy_template_response_instance = ResourceListOfPolicyTemplateResponse.from_json(json)
# print the JSON string representation of the object
print ResourceListOfPolicyTemplateResponse.to_json()

# convert the object into a dict
resource_list_of_policy_template_response_dict = resource_list_of_policy_template_response_instance.to_dict()
# create an instance of ResourceListOfPolicyTemplateResponse from a dict
resource_list_of_policy_template_response_form_dict = resource_list_of_policy_template_response.from_dict(resource_list_of_policy_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


