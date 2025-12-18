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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

metadata_key: StrictStr = "example_metadata_key"
operator: Operator
text_value: Optional[StrictStr] = "example_text_value"
metadata_expression_instance = MetadataExpression(metadata_key=metadata_key, operator=operator, text_value=text_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

