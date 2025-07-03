# AddToPolicyCollectionRequest

Base properties to create or update a policy collection
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[PolicyId]**](PolicyId.md) | The identifiers of the Policies to be added to the collection. | [optional] 
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) | The identifiers of the PolicyCollections to be added to the collection. | [optional] 
## Example

```python
from finbourne_access.models.add_to_policy_collection_request import AddToPolicyCollectionRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

policies: Optional[conlist(PolicyId)] = # Replace with your value
policy_collections: Optional[conlist(PolicyCollectionId)] = # Replace with your value
add_to_policy_collection_request_instance = AddToPolicyCollectionRequest(policies=policies, policy_collections=policy_collections)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

