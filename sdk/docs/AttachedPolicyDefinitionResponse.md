# AttachedPolicyDefinitionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_role** | [**RoleId**](RoleId.md) |  | [optional] 
**role_hierarchy_index** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**applications** | **List[str]** |  | [optional] 
**policy_type** | [**PolicyType**](PolicyType.md) |  | [optional] 
**id** | [**PolicyId**](PolicyId.md) |  | [optional] 
**grant** | [**Grant**](Grant.md) |  | [optional] 
**selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) |  | [optional] 
**var_for** | [**List[ForSpec]**](ForSpec.md) |  | [optional] 
**var_if** | [**List[IfExpression]**](IfExpression.md) |  | [optional] 
**when** | [**WhenSpec**](WhenSpec.md) |  | [optional] 
**how** | [**HowSpec**](HowSpec.md) |  | [optional] 

## Example

```python
from finbourne_access.models.attached_policy_definition_response import AttachedPolicyDefinitionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AttachedPolicyDefinitionResponse from a JSON string
attached_policy_definition_response_instance = AttachedPolicyDefinitionResponse.from_json(json)
# print the JSON string representation of the object
print AttachedPolicyDefinitionResponse.to_json()

# convert the object into a dict
attached_policy_definition_response_dict = attached_policy_definition_response_instance.to_dict()
# create an instance of AttachedPolicyDefinitionResponse from a dict
attached_policy_definition_response_form_dict = attached_policy_definition_response.from_dict(attached_policy_definition_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


