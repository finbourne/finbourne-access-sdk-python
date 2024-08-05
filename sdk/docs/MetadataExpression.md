# MetadataExpression


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_key** | **str** |  | 
**operator** | [**Operator**](Operator.md) |  | 
**text_value** | **str** |  | [optional] 

## Example

```python
from finbourne_access.models.metadata_expression import MetadataExpression

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataExpression from a JSON string
metadata_expression_instance = MetadataExpression.from_json(json)
# print the JSON string representation of the object
print MetadataExpression.to_json()

# convert the object into a dict
metadata_expression_dict = metadata_expression_instance.to_dict()
# create an instance of MetadataExpression from a dict
metadata_expression_form_dict = metadata_expression.from_dict(metadata_expression_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


