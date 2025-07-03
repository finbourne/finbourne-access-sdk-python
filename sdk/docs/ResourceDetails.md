# ResourceDetails

Details about the resource being requested that may be pertinent to the entitlement evaluation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Dict[str, str]** | The identifier of the resource being evaluated | 
**metadata** | **Dict[str, List[EntitlementMetadata]]** | Any metadata associated with the resource being requested | [optional] 
## Example

```python
from finbourne_access.models.resource_details import ResourceDetails
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

id: Dict[str, StrictStr] = # Replace with your value
metadata: Optional[Dict[str, conlist(EntitlementMetadata)]] = # Replace with your value
resource_details_instance = ResourceDetails(id=id, metadata=metadata)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

