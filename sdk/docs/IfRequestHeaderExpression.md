# IfRequestHeaderExpression


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header_name** | **str** |  | 
**operator** | [**TextOperator**](TextOperator.md) |  | 
**value** | **str** |  | [optional] 

## Example

```python
from finbourne_access.models.if_request_header_expression import IfRequestHeaderExpression

# TODO update the JSON string below
json = "{}"
# create an instance of IfRequestHeaderExpression from a JSON string
if_request_header_expression_instance = IfRequestHeaderExpression.from_json(json)
# print the JSON string representation of the object
print IfRequestHeaderExpression.to_json()

# convert the object into a dict
if_request_header_expression_dict = if_request_header_expression_instance.to_dict()
# create an instance of IfRequestHeaderExpression from a dict
if_request_header_expression_form_dict = if_request_header_expression.from_dict(if_request_header_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


