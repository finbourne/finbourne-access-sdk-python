# IfViaApiExpression

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_feature_codes** | **List[str]** |  | 
## Example

```python
from finbourne_access.models.if_via_api_expression import IfViaApiExpression
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

api_feature_codes: List[StrictStr] = # Replace with your value
if_via_api_expression_instance = IfViaApiExpression(api_feature_codes=api_feature_codes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

