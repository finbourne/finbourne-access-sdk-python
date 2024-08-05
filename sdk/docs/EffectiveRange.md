# EffectiveRange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** |  | [optional] 
**to** | **datetime** |  | [optional] 

## Example

```python
from finbourne_access.models.effective_range import EffectiveRange

# TODO update the JSON string below
json = "{}"
# create an instance of EffectiveRange from a JSON string
effective_range_instance = EffectiveRange.from_json(json)
# print the JSON string representation of the object
print EffectiveRange.to_json()

# convert the object into a dict
effective_range_dict = effective_range_instance.to_dict()
# create an instance of EffectiveRange from a dict
effective_range_form_dict = effective_range.from_dict(effective_range_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


