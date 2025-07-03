# AddPolicyCollectionToRoleRequest

Request body used to add Policy Collections to a Role
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) | Identifiers of policy collections to add to a role | 
## Example

```python
from finbourne_access.models.add_policy_collection_to_role_request import AddPolicyCollectionToRoleRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

policy_collections: conlist(PolicyCollectionId) = # Replace with your value
add_policy_collection_to_role_request_instance = AddPolicyCollectionToRoleRequest(policy_collections=policy_collections)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

