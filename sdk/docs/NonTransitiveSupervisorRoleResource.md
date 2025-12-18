# NonTransitiveSupervisorRoleResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **List[Dict[str, str]]** |  | 
## Example

```python
from finbourne_access.models.non_transitive_supervisor_role_resource import NonTransitiveSupervisorRoleResource
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

roles: List[Dict[str, StrictStr]]
non_transitive_supervisor_role_resource_instance = NonTransitiveSupervisorRoleResource(roles=roles)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

