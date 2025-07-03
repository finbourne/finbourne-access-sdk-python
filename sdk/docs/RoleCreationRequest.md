# RoleCreationRequest

Request to create a role
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the role | 
**description** | **str** | The description of the role | [optional] 
**resource** | [**RoleResourceRequest**](RoleResourceRequest.md) |  | 
**when** | [**WhenSpec**](WhenSpec.md) |  | 
## Example

```python
from finbourne_access.models.role_creation_request import RoleCreationRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr, validator

code: StrictStr = "example_code"
description: Optional[StrictStr] = "example_description"
resource: RoleResourceRequest = # Replace with your value
when: WhenSpec = # Replace with your value
role_creation_request_instance = RoleCreationRequest(code=code, description=description, resource=resource, when=when)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

