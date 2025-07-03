# MatchAllSelectorDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[ActionId]**](ActionId.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
## Example

```python
from finbourne_access.models.match_all_selector_definition import MatchAllSelectorDefinition
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

actions: conlist(ActionId, min_items=1) = Field(...)
name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
match_all_selector_definition_instance = MatchAllSelectorDefinition(actions=actions, name=name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

