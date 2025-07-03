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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

header_name: StrictStr = "example_header_name"
operator: TextOperator = # Replace with your value
value: Optional[StrictStr] = "example_value"
if_request_header_expression_instance = IfRequestHeaderExpression(header_name=header_name, operator=operator, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

