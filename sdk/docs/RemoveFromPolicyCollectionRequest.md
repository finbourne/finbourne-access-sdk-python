# RemoveFromPolicyCollectionRequest

Base properties to create or update a policy collection
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[PolicyId]**](PolicyId.md) | The identifiers of the Policies to be removed from the collection. | [optional] 
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) | The identifiers of the PolicyCollections to be removed from the collection. | [optional] 
## Example

```python
from finbourne_access.models.remove_from_policy_collection_request import RemoveFromPolicyCollectionRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

policies: Optional[List[PolicyId]] = # Replace with your value
policy_collections: Optional[List[PolicyCollectionId]] = # Replace with your value
remove_from_policy_collection_request_instance = RemoveFromPolicyCollectionRequest(policies=policies, policy_collections=policy_collections)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

