# PolicyCollectionResponse

A PolicyCollection encapsulating one or more Policies and PolicyCollections
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**PolicyCollectionId**](PolicyCollectionId.md) |  | [optional] 
**policies** | [**List[PolicyId]**](PolicyId.md) | The identifiers of the Policies in this collection | [optional] 
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) | The identifiers of the PolicyCollections in this collection | [optional] 
**description** | **str** | A description of this policy collection | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_access.models.policy_collection_response import PolicyCollectionResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

id: Optional[PolicyCollectionId] = None
policies: Optional[conlist(PolicyId)] = # Replace with your value
policy_collections: Optional[conlist(PolicyCollectionId)] = # Replace with your value
description: Optional[StrictStr] = "example_description"
links: Optional[conlist(Link)] = None
policy_collection_response_instance = PolicyCollectionResponse(id=id, policies=policies, policy_collections=policy_collections, description=description, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

