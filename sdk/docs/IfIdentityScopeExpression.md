# IfIdentityScopeExpression

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_name** | **str** |  | 
## Example

```python
from finbourne_access.models.if_identity_scope_expression import IfIdentityScopeExpression
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope_name: StrictStr = "example_scope_name"
if_identity_scope_expression_instance = IfIdentityScopeExpression(scope_name=scope_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

