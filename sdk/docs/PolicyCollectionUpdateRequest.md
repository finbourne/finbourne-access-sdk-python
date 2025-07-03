# PolicyCollectionUpdateRequest

Update an existing PolicyCollection
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[PolicyId]**](PolicyId.md) | The identifiers of the Policies in this collection | [optional] 
**metadata** | **Dict[str, List[EntitlementMetadata]]** | Any relevant metadata associated with this resource for controlling access to this resource | [optional] 
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) | The identifiers of the PolicyCollections in this collection | [optional] 
**description** | **str** | A description of this policy collection | [optional] 
## Example

```python
from finbourne_access.models.policy_collection_update_request import PolicyCollectionUpdateRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

policies: Optional[conlist(PolicyId)] = # Replace with your value
metadata: Optional[Dict[str, conlist(EntitlementMetadata)]] = # Replace with your value
policy_collections: Optional[conlist(PolicyCollectionId)] = # Replace with your value
description: Optional[StrictStr] = "example_description"
policy_collection_update_request_instance = PolicyCollectionUpdateRequest(policies=policies, metadata=metadata, policy_collections=policy_collections, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

