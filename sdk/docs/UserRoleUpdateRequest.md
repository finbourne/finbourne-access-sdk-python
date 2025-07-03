# UserRoleUpdateRequest

Dto used to request updating a user's role
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**PolicyIdRoleResource**](PolicyIdRoleResource.md) |  | 
## Example

```python
from finbourne_access.models.user_role_update_request import UserRoleUpdateRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

resource: PolicyIdRoleResource = # Replace with your value
user_role_update_request_instance = UserRoleUpdateRequest(resource=resource)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

