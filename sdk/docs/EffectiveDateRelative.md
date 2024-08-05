# EffectiveDateRelative


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**PointInTimeSpecification**](PointInTimeSpecification.md) |  | [optional] 
**adjustment** | **int** |  | [optional] 
**unit** | [**DateUnit**](DateUnit.md) |  | [optional] 
**relative_to_date_time** | [**RelativeToDateTime**](RelativeToDateTime.md) |  | [optional] 

## Example

```python
from finbourne_access.models.effective_date_relative import EffectiveDateRelative

# TODO update the JSON string below
json = "{}"
# create an instance of EffectiveDateRelative from a JSON string
effective_date_relative_instance = EffectiveDateRelative.from_json(json)
# print the JSON string representation of the object
print EffectiveDateRelative.to_json()

# convert the object into a dict
effective_date_relative_dict = effective_date_relative_instance.to_dict()
# create an instance of EffectiveDateRelative from a dict
effective_date_relative_form_dict = effective_date_relative.from_dict(effective_date_relative_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


