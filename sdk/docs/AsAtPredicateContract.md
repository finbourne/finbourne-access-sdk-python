# AsAtPredicateContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**date_time_offset** | **datetime** |  | [optional] 
## Example

```python
from finbourne_access.models.as_at_predicate_contract import AsAtPredicateContract
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr
from datetime import datetime
value: Optional[StrictStr] = "example_value"
date_time_offset: Optional[datetime] = # Replace with your value
as_at_predicate_contract_instance = AsAtPredicateContract(value=value, date_time_offset=date_time_offset)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

