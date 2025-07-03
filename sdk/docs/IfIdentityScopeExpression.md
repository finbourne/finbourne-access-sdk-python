# IfIdentityScopeExpression

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope_name** | **str** |  | 
## Example

```python
from finbourne_access.models.if_identity_scope_expression import IfIdentityScopeExpression
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

scope_name: StrictStr = "example_scope_name"
if_identity_scope_expression_instance = IfIdentityScopeExpression(scope_name=scope_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

