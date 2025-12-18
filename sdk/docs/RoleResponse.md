# RoleResponse

Response object from the role API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**RoleId**](RoleId.md) |  | 
**role_hierarchy_index** | **int** | The hierarchical index of the role | 
**description** | **str** | The description of the role | [optional] 
**resource** | [**RoleResourceRequest**](RoleResourceRequest.md) |  | 
**when** | [**WhenSpec**](WhenSpec.md) |  | 
**permission** | **str** | The action key of the role | 
**limit** | **Dict[str, str]** | The identifiers of the role with the maximum privileges that this role can have | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_access.models.role_response import RoleResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: RoleId
role_hierarchy_index: StrictInt = # Replace with your value
role_hierarchy_index: StrictInt = 42
description: Optional[StrictStr] = "example_description"
resource: RoleResourceRequest
when: WhenSpec
permission: StrictStr = "example_permission"
limit: Optional[Dict[str, StrictStr]] = # Replace with your value
links: Optional[List[Link]] = None
role_response_instance = RoleResponse(id=id, role_hierarchy_index=role_hierarchy_index, description=description, resource=resource, when=when, permission=permission, limit=limit, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

