# KeyValuePairOfStringToString


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from finbourne_access.models.key_value_pair_of_string_to_string import KeyValuePairOfStringToString

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValuePairOfStringToString from a JSON string
key_value_pair_of_string_to_string_instance = KeyValuePairOfStringToString.from_json(json)
# print the JSON string representation of the object
print KeyValuePairOfStringToString.to_json()

# convert the object into a dict
key_value_pair_of_string_to_string_dict = key_value_pair_of_string_to_string_instance.to_dict()
# create an instance of KeyValuePairOfStringToString from a dict
key_value_pair_of_string_to_string_form_dict = key_value_pair_of_string_to_string.from_dict(key_value_pair_of_string_to_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


