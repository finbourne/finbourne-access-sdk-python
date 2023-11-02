# HowSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**parameters** | [**List[KeyValuePairOfStringToString]**](KeyValuePairOfStringToString.md) |  | [optional] 

## Example

```python
from finbourne_access.models.how_spec import HowSpec

# TODO update the JSON string below
json = "{}"
# create an instance of HowSpec from a JSON string
how_spec_instance = HowSpec.from_json(json)
# print the JSON string representation of the object
print HowSpec.to_json()

# convert the object into a dict
how_spec_dict = how_spec_instance.to_dict()
# create an instance of HowSpec from a dict
how_spec_form_dict = how_spec.from_dict(how_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


