# ForSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_range_for_spec** | [**AsAtRangeForSpec**](AsAtRangeForSpec.md) |  | [optional] 
**as_at_relative** | [**AsAtRelative**](AsAtRelative.md) |  | [optional] 
**effective_date_has_quality** | [**EffectiveDateHasQuality**](EffectiveDateHasQuality.md) |  | [optional] 
**effective_date_relative** | [**EffectiveDateRelative**](EffectiveDateRelative.md) |  | [optional] 
**effective_range** | [**EffectiveRange**](EffectiveRange.md) |  | [optional] 

## Example

```python
from finbourne_access.models.for_spec import ForSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ForSpec from a JSON string
for_spec_instance = ForSpec.from_json(json)
# print the JSON string representation of the object
print ForSpec.to_json()

# convert the object into a dict
for_spec_dict = for_spec_instance.to_dict()
# create an instance of ForSpec from a dict
for_spec_form_dict = for_spec.from_dict(for_spec_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


