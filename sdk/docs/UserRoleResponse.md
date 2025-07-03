# UserRoleResponse

Response object from the user role API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**RoleResourceRequest**](RoleResourceRequest.md) |  | 
**id** | [**RoleId**](RoleId.md) |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_access.models.user_role_response import UserRoleResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

resource: RoleResourceRequest = # Replace with your value
id: RoleId = # Replace with your value
links: Optional[conlist(Link)] = None
user_role_response_instance = UserRoleResponse(resource=resource, id=id, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

