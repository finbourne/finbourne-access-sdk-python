# EntitlementMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
## Example

```python
from finbourne_access.models.entitlement_metadata import EntitlementMetadata
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictStr

provider: Optional[StrictStr] = "example_provider"
value: Optional[StrictStr] = "example_value"
entitlement_metadata_instance = EntitlementMetadata(provider=provider, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

