# RoleUpdateRequest

Role update does not allow the changing of the id
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the role | [optional] 
**resource** | [**RoleResourceRequest**](RoleResourceRequest.md) |  | 
**when** | [**WhenSpec**](WhenSpec.md) |  | 
## Example

```python
from finbourne_access.models.role_update_request import RoleUpdateRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

description: Optional[StrictStr] = "example_description"
resource: RoleResourceRequest = # Replace with your value
when: WhenSpec = # Replace with your value
role_update_request_instance = RoleUpdateRequest(description=description, resource=resource, when=when)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

