# MatchAllSelectorDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[ActionId]**](ActionId.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from finbourne_access.models.match_all_selector_definition import MatchAllSelectorDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAllSelectorDefinition from a JSON string
match_all_selector_definition_instance = MatchAllSelectorDefinition.from_json(json)
# print the JSON string representation of the object
print MatchAllSelectorDefinition.to_json()

# convert the object into a dict
match_all_selector_definition_dict = match_all_selector_definition_instance.to_dict()
# create an instance of MatchAllSelectorDefinition from a dict
match_all_selector_definition_form_dict = match_all_selector_definition.from_dict(match_all_selector_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


