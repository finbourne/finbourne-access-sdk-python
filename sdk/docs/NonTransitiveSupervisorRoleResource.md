# NonTransitiveSupervisorRoleResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **List[Dict[str, str]]** |  | 
## Example

```python
from finbourne_access.models.non_transitive_supervisor_role_resource import NonTransitiveSupervisorRoleResource
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

roles: conlist(Dict[str, StrictStr], min_items=1) = Field(...)
non_transitive_supervisor_role_resource_instance = NonTransitiveSupervisorRoleResource(roles=roles)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

