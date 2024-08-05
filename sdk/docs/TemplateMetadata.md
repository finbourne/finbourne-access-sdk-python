# TemplateMetadata

Extra policy template metadata information, used during a generation request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_selection** | [**List[TemplateSelection]**](TemplateSelection.md) | List of policy templates used for a generation request | [optional] 
**build_as_at** | **datetime** | Policy template build AsAt time used for a generation request | [optional] 

## Example

```python
from finbourne_access.models.template_metadata import TemplateMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateMetadata from a JSON string
template_metadata_instance = TemplateMetadata.from_json(json)
# print the JSON string representation of the object
print TemplateMetadata.to_json()

# convert the object into a dict
template_metadata_dict = template_metadata_instance.to_dict()
# create an instance of TemplateMetadata from a dict
template_metadata_form_dict = template_metadata.from_dict(template_metadata_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


