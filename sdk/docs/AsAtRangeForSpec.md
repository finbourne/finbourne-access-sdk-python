# AsAtRangeForSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | [**AsAtPredicateContract**](AsAtPredicateContract.md) |  | 
**to** | [**AsAtPredicateContract**](AsAtPredicateContract.md) |  | 
## Example

```python
from finbourne_access.models.as_at_range_for_spec import AsAtRangeForSpec
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

var_from: AsAtPredicateContract = # Replace with your value
to: AsAtPredicateContract = # Replace with your value
as_at_range_for_spec_instance = AsAtRangeForSpec(var_from=var_from, to=to)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

