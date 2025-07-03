# AddPolicyToRoleRequest

Request body used to add Policies to a Role
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[PolicyId]**](PolicyId.md) | Identifiers of policies to add to a role | 
## Example

```python
from finbourne_access.models.add_policy_to_role_request import AddPolicyToRoleRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

policies: conlist(PolicyId) = # Replace with your value
add_policy_to_role_request_instance = AddPolicyToRoleRequest(policies=policies)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

