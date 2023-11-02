# PolicyResponse

Response object from the policy API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**PolicyId**](PolicyId.md) |  | [optional] 
**description** | **str** | Description of what the policy is entitling | [optional] 
**applications** | **List[str]** | Applications to which the policy applies | [optional] 
**grant** | [**Grant**](Grant.md) |  | [optional] 
**selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) | Selectors that this policy will be applied to | [optional] 
**var_for** | [**List[ForSpec]**](ForSpec.md) | \&quot;For Specification\&quot; for when the policy is to be applied | [optional] 
**var_if** | [**List[IfExpression]**](IfExpression.md) | \&quot;If Specification\&quot; for when the policy is to be applied | [optional] 
**when** | [**WhenSpec**](WhenSpec.md) |  | [optional] 
**how** | [**HowSpec**](HowSpec.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_access.models.policy_response import PolicyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyResponse from a JSON string
policy_response_instance = PolicyResponse.from_json(json)
# print the JSON string representation of the object
print PolicyResponse.to_json()

# convert the object into a dict
policy_response_dict = policy_response_instance.to_dict()
# create an instance of PolicyResponse from a dict
policy_response_form_dict = policy_response.from_dict(policy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


