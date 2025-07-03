# HowSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**parameters** | [**List[KeyValuePairOfStringToString]**](KeyValuePairOfStringToString.md) |  | [optional] 
## Example

```python
from finbourne_access.models.how_spec import HowSpec
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, StrictStr, conlist

type: Optional[StrictStr] = "example_type"
parameters: Optional[conlist(KeyValuePairOfStringToString)] = None
how_spec_instance = HowSpec(type=type, parameters=parameters)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

