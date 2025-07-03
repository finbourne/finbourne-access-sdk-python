# EvaluationRequest

Specification for a server side evaluation of entitlement.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**RequestDetails**](RequestDetails.md) |  | 
**resource** | [**ResourceDetails**](ResourceDetails.md) |  | 
## Example

```python
from finbourne_access.models.evaluation_request import EvaluationRequest
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field

request: RequestDetails = # Replace with your value
resource: ResourceDetails = # Replace with your value
evaluation_request_instance = EvaluationRequest(request=request, resource=resource)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

