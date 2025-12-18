# AsAtRangeForSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**AsAtPredicateContract**](AsAtPredicateContract.md) |  | 
**to** | [**AsAtPredicateContract**](AsAtPredicateContract.md) |  | 
## Example

```python
from finbourne_access.models.as_at_range_for_spec import AsAtRangeForSpec
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

var_from: AsAtPredicateContract = # Replace with your value
to: AsAtPredicateContract
as_at_range_for_spec_instance = AsAtRangeForSpec(var_from=var_from, to=to)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

