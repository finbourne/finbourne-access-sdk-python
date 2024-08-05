# PolicyTemplateCreationRequest

Request to create a policy template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The Code of the policy template being created | 
**display_name** | **str** | The display name of the policy template being created | 
**description** | **str** | Description of the policy template being craeted | 
**templated_selectors** | [**List[PolicyTemplatedSelector]**](PolicyTemplatedSelector.md) | The selector definitions of policies included in this policy template | 

## Example

```python
from finbourne_access.models.policy_template_creation_request import PolicyTemplateCreationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplateCreationRequest from a JSON string
policy_template_creation_request_instance = PolicyTemplateCreationRequest.from_json(json)
# print the JSON string representation of the object
print PolicyTemplateCreationRequest.to_json()

# convert the object into a dict
policy_template_creation_request_dict = policy_template_creation_request_instance.to_dict()
# create an instance of PolicyTemplateCreationRequest from a dict
policy_template_creation_request_form_dict = policy_template_creation_request.from_dict(policy_template_creation_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


