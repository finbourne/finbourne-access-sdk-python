# EffectiveRange

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** |  | [optional] 
**to** | **datetime** |  | [optional] 
## Example

```python
from finbourne_access.models.effective_range import EffectiveRange
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field
from datetime import datetime
var_from: Optional[datetime] = # Replace with your value
to: Optional[datetime] = None
effective_range_instance = EffectiveRange(var_from=var_from, to=to)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

