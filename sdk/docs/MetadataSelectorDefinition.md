# MetadataSelectorDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expressions** | [**List[MetadataExpression]**](MetadataExpression.md) |  | 
**actions** | [**List[ActionId]**](ActionId.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
## Example

```python
from finbourne_access.models.metadata_selector_definition import MetadataSelectorDefinition
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

expressions: conlist(MetadataExpression, min_items=1) = Field(...)
actions: conlist(ActionId, min_items=1) = Field(...)
name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
metadata_selector_definition_instance = MetadataSelectorDefinition(expressions=expressions, actions=actions, name=name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

