# PolicyId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | [optional] 
**code** | **str** |  | 
## Example

```python
from finbourne_access.models.policy_id import PolicyId
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

scope: Optional[StrictStr] = "example_scope"
code: StrictStr = "example_code"
policy_id_instance = PolicyId(scope=scope, code=code)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

