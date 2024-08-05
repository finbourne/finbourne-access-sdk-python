# PolicySelectorDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_restriction** | **Dict[str, str]** |  | [optional] 
**restriction_selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) |  | [optional] 
**actions** | [**List[ActionId]**](ActionId.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from finbourne_access.models.policy_selector_definition import PolicySelectorDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of PolicySelectorDefinition from a JSON string
policy_selector_definition_instance = PolicySelectorDefinition.from_json(json)
# print the JSON string representation of the object
print PolicySelectorDefinition.to_json()

# convert the object into a dict
policy_selector_definition_dict = policy_selector_definition_instance.to_dict()
# create an instance of PolicySelectorDefinition from a dict
policy_selector_definition_form_dict = policy_selector_definition.from_dict(policy_selector_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


