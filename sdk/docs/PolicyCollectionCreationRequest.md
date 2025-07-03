# PolicyCollectionCreationRequest

Create a PolicyCollection, a logical group of Policies or other PolicyCollections
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The identifier for the PolicyCollection being created | 
**policies** | [**List[PolicyId]**](PolicyId.md) | The identifiers of the Policies in this collection | [optional] 
**metadata** | **Dict[str, List[EntitlementMetadata]]** | Any relevant metadata associated with this resource for controlling access to this resource | [optional] 
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) | The identifiers of the PolicyCollections in this collection | [optional] 
**description** | **str** | A description of this policy collection | [optional] 
## Example

```python
from finbourne_access.models.policy_collection_creation_request import PolicyCollectionCreationRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr, validator

code: StrictStr = "example_code"
policies: Optional[conlist(PolicyId)] = # Replace with your value
metadata: Optional[Dict[str, conlist(EntitlementMetadata)]] = # Replace with your value
policy_collections: Optional[conlist(PolicyCollectionId)] = # Replace with your value
description: Optional[StrictStr] = "example_description"
policy_collection_creation_request_instance = PolicyCollectionCreationRequest(code=code, policies=policies, metadata=metadata, policy_collections=policy_collections, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

