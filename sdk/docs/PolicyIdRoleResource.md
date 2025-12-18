# PolicyIdRoleResource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[PolicyId]**](PolicyId.md) |  | [optional] 
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) |  | [optional] 
## Example

```python
from finbourne_access.models.policy_id_role_resource import PolicyIdRoleResource
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

policies: Optional[List[PolicyId]] = None
policy_collections: Optional[List[PolicyCollectionId]] = # Replace with your value
policy_id_role_resource_instance = PolicyIdRoleResource(policies=policies, policy_collections=policy_collections)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

