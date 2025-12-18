# UserRoleCreationRequest

Dto used to request creating a user's role
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The Id of the user for whom to create the role. | 
**resource** | [**PolicyIdRoleResource**](PolicyIdRoleResource.md) |  | 
## Example

```python
from finbourne_access.models.user_role_creation_request import UserRoleCreationRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

user_id: StrictStr = "example_user_id"
resource: PolicyIdRoleResource
user_role_creation_request_instance = UserRoleCreationRequest(user_id=user_id, resource=resource)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

