# MetadataSelectorDefinition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expressions** | [**List[MetadataExpression]**](MetadataExpression.md) |  | 
**actions** | [**List[ActionId]**](ActionId.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from finbourne_access.models.metadata_selector_definition import MetadataSelectorDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataSelectorDefinition from a JSON string
metadata_selector_definition_instance = MetadataSelectorDefinition.from_json(json)
# print the JSON string representation of the object
print MetadataSelectorDefinition.to_json()

# convert the object into a dict
metadata_selector_definition_dict = metadata_selector_definition_instance.to_dict()
# create an instance of MetadataSelectorDefinition from a dict
metadata_selector_definition_form_dict = metadata_selector_definition.from_dict(metadata_selector_definition_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


