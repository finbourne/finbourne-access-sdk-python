# KeyValuePairOfStringToString

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
## Example

```python
from finbourne_access.models.key_value_pair_of_string_to_string import KeyValuePairOfStringToString
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictStr

key: Optional[StrictStr] = "example_key"
value: Optional[StrictStr] = "example_value"
key_value_pair_of_string_to_string_instance = KeyValuePairOfStringToString(key=key, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

