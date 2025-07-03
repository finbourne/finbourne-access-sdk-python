# WhenSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activate** | **datetime** |  | 
**deactivate** | **datetime** |  | [optional] 
## Example

```python
from finbourne_access.models.when_spec import WhenSpec
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field
from datetime import datetime
activate: datetime = # Replace with your value
deactivate: Optional[datetime] = None
when_spec_instance = WhenSpec(activate=activate, deactivate=deactivate)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

