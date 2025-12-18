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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

request: RequestDetails
resource: ResourceDetails
evaluation_request_instance = EvaluationRequest(request=request, resource=resource)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

