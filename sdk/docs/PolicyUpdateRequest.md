# PolicyUpdateRequest

Update policy request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of what the policy will be used for | [optional] 
**applications** | **List[str]** | Applications this policy is used with | [optional] 
**grant** | [**Grant**](Grant.md) |  | 
**selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) | Selectors that identify what resources this policy qualifies for | 
**var_for** | [**List[ForSpec]**](ForSpec.md) | \&quot;For Specification\&quot; for when the policy is to be applied | [optional] 
**var_if** | [**List[IfExpression]**](IfExpression.md) | \&quot;If Specification\&quot; for when the policy is to be applied | [optional] 
**when** | [**WhenSpec**](WhenSpec.md) |  | 
**how** | [**HowSpec**](HowSpec.md) |  | [optional] 

## Example

```python
from finbourne_access.models.policy_update_request import PolicyUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyUpdateRequest from a JSON string
policy_update_request_instance = PolicyUpdateRequest.from_json(json)
# print the JSON string representation of the object
print PolicyUpdateRequest.to_json()

# convert the object into a dict
policy_update_request_dict = policy_update_request_instance.to_dict()
# create an instance of PolicyUpdateRequest from a dict
policy_update_request_form_dict = policy_update_request.from_dict(policy_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


