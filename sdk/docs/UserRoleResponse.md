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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

resource: RoleResourceRequest
id: RoleId
links: Optional[List[Link]] = None
user_role_response_instance = UserRoleResponse(resource=resource, id=id, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

