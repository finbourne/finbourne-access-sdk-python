# ResourceDetails

Details about the resource being requested that may be pertinent to the entitlement evaluation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **Dict[str, str]** | The identifier of the resource being evaluated | 
**metadata** | **Dict[str, Optional[List[EntitlementMetadata]]]** | Any metadata associated with the resource being requested | [optional] 
## Example

```python
from finbourne_access.models.resource_details import ResourceDetails
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: Dict[str, StrictStr] = # Replace with your value
metadata: Optional[Dict[str, Optional[List[EntitlementMetadata]]]] = # Replace with your value
resource_details_instance = ResourceDetails(id=id, metadata=metadata)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

