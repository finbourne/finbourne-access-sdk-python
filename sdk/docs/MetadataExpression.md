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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

metadata_key: StrictStr = "example_metadata_key"
operator: Operator = # Replace with your value
text_value: Optional[StrictStr] = "example_text_value"
metadata_expression_instance = MetadataExpression(metadata_key=metadata_key, operator=operator, text_value=text_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

