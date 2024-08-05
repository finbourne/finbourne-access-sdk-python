# WhenSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate** | **datetime** |  | 
**deactivate** | **datetime** |  | [optional] 

## Example

```python
from finbourne_access.models.when_spec import WhenSpec

# TODO update the JSON string below
json = "{}"
# create an instance of WhenSpec from a JSON string
when_spec_instance = WhenSpec.from_json(json)
# print the JSON string representation of the object
print WhenSpec.to_json()

# convert the object into a dict
when_spec_dict = when_spec_instance.to_dict()
# create an instance of WhenSpec from a dict
when_spec_form_dict = when_spec.from_dict(when_spec_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


