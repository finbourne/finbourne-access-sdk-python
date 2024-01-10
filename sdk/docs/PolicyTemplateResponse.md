# PolicyTemplateResponse

Response object for a policy template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display name of the policy template being created | [optional] 
**scope** | **str** | The Scope of the policy template being created | [optional] 
**code** | **str** | The Code of the policy template being created | [optional] 
**description** | **str** | Description of the policy template being created | [optional] 
**applications** | **List[str]** | List of applications that this policy template covers | [optional] 
**tags** | **List[str]** | List of policy types that this policy template covers | [optional] 
**templated_selectors** | [**List[PolicyTemplatedSelector]**](PolicyTemplatedSelector.md) | The selector definitions of policies included in this policy template | [optional] 

## Example

```python
from finbourne_access.models.policy_template_response import PolicyTemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateResponse from a JSON string
policy_template_response_instance = PolicyTemplateResponse.from_json(json)
# print the JSON string representation of the object
print PolicyTemplateResponse.to_json()

# convert the object into a dict
policy_template_response_dict = policy_template_response_instance.to_dict()
# create an instance of PolicyTemplateResponse from a dict
policy_template_response_form_dict = policy_template_response.from_dict(policy_template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


