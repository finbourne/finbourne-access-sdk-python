# AsAtRelative


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**PointInTimeSpecification**](PointInTimeSpecification.md) |  | [optional] 
**adjustment** | **int** |  | [optional] 
**unit** | [**DateUnit**](DateUnit.md) |  | [optional] 
**relative_to_date_time** | [**RelativeToDateTime**](RelativeToDateTime.md) |  | [optional] 

## Example

```python
from finbourne_access.models.as_at_relative import AsAtRelative

# TODO update the JSON string below
json = "{}"
# create an instance of AsAtRelative from a JSON string
as_at_relative_instance = AsAtRelative.from_json(json)
# print the JSON string representation of the object
print AsAtRelative.to_json()

# convert the object into a dict
as_at_relative_dict = as_at_relative_instance.to_dict()
# create an instance of AsAtRelative from a dict
as_at_relative_form_dict = as_at_relative.from_dict(as_at_relative_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


