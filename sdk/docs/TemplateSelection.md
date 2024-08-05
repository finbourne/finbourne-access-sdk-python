# TemplateSelection

A template selection, identifying a policy template to use for generation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | Scope identifying policy template to use for generation | 
**code** | **str** | Code identifying policy template to use for generation | 
**selector_tags** | **List[str]** | List of selector tags to optionally filter in the template generation   (Eg: Feature, Data, etc) | [optional] 

## Example

```python
from finbourne_access.models.template_selection import TemplateSelection

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateSelection from a JSON string
template_selection_instance = TemplateSelection.from_json(json)
# print the JSON string representation of the object
print TemplateSelection.to_json()

# convert the object into a dict
template_selection_dict = template_selection_instance.to_dict()
# create an instance of TemplateSelection from a dict
template_selection_form_dict = template_selection.from_dict(template_selection_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


