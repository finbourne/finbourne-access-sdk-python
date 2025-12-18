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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

header_name: StrictStr = "example_header_name"
operator: TextOperator
value: Optional[StrictStr] = "example_value"
if_request_header_expression_instance = IfRequestHeaderExpression(header_name=header_name, operator=operator, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

