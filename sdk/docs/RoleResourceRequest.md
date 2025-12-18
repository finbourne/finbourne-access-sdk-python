# RoleResourceRequest

RoleResourceRequest
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_transitive_supervisor_role_resource** | [**NonTransitiveSupervisorRoleResource**](NonTransitiveSupervisorRoleResource.md) |  | [optional] 
**policy_id_role_resource** | [**PolicyIdRoleResource**](PolicyIdRoleResource.md) |  | [optional] 
## Example

```python
from finbourne_access.models.role_resource_request import RoleResourceRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

non_transitive_supervisor_role_resource: Optional[NonTransitiveSupervisorRoleResource] = # Replace with your value
policy_id_role_resource: Optional[PolicyIdRoleResource] = # Replace with your value
role_resource_request_instance = RoleResourceRequest(non_transitive_supervisor_role_resource=non_transitive_supervisor_role_resource, policy_id_role_resource=policy_id_role_resource)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

