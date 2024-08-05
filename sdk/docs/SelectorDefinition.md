# SelectorDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_selector_definition** | [**MetadataSelectorDefinition**](MetadataSelectorDefinition.md) |  | [optional] 
**id_selector_definition** | [**IdSelectorDefinition**](IdSelectorDefinition.md) |  | [optional] 
**match_all_selector_definition** | [**MatchAllSelectorDefinition**](MatchAllSelectorDefinition.md) |  | [optional] 
**policy_selector_definition** | [**PolicySelectorDefinition**](PolicySelectorDefinition.md) |  | [optional] 

## Example

```python
from finbourne_access.models.selector_definition import SelectorDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of SelectorDefinition from a JSON string
selector_definition_instance = SelectorDefinition.from_json(json)
# print the JSON string representation of the object
print SelectorDefinition.to_json()

# convert the object into a dict
selector_definition_dict = selector_definition_instance.to_dict()
# create an instance of SelectorDefinition from a dict
selector_definition_form_dict = selector_definition.from_dict(selector_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


