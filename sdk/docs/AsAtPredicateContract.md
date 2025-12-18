# AsAtPredicateContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**date_time_offset** | **datetime** |  | [optional] 
## Example

```python
from finbourne_access.models.as_at_predicate_contract import AsAtPredicateContract
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

value: Optional[StrictStr] = "example_value"
date_time_offset: Optional[datetime] = # Replace with your value
as_at_predicate_contract_instance = AsAtPredicateContract(value=value, date_time_offset=date_time_offset)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

