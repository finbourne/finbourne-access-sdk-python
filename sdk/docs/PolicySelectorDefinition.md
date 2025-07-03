# PolicySelectorDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identity_restriction** | **Dict[str, str]** |  | [optional] 
**restriction_selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) |  | [optional] 
**actions** | [**List[ActionId]**](ActionId.md) |  | 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
## Example

```python
from finbourne_access.models.policy_selector_definition import PolicySelectorDefinition
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr

identity_restriction: Optional[Dict[str, StrictStr]] = # Replace with your value
restriction_selectors: Optional[conlist(SelectorDefinition)] = # Replace with your value
actions: conlist(ActionId, min_items=1) = Field(...)
name: Optional[StrictStr] = "example_name"
description: Optional[StrictStr] = "example_description"
policy_selector_definition_instance = PolicySelectorDefinition(identity_restriction=identity_restriction, restriction_selectors=restriction_selectors, actions=actions, name=name, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

