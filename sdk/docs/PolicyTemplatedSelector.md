# PolicyTemplatedSelector

Templated selector for a policy template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | The application that this selector definition applies to | 
**tag** | **str** | The type of policy that this selector definition applies to | 
**selector** | [**SelectorDefinition**](SelectorDefinition.md) |  | 

## Example

```python
from finbourne_access.models.policy_templated_selector import PolicyTemplatedSelector

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTemplatedSelector from a JSON string
policy_templated_selector_instance = PolicyTemplatedSelector.from_json(json)
# print the JSON string representation of the object
print PolicyTemplatedSelector.to_json()

# convert the object into a dict
policy_templated_selector_dict = policy_templated_selector_instance.to_dict()
# create an instance of PolicyTemplatedSelector from a dict
policy_templated_selector_form_dict = policy_templated_selector.from_dict(policy_templated_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


