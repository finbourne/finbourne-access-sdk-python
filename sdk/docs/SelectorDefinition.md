# SelectorDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_selector_definition** | [**MetadataSelectorDefinition**](MetadataSelectorDefinition.md) |  | [optional] 
**id_selector_definition** | [**IdSelectorDefinition**](IdSelectorDefinition.md) |  | [optional] 
**match_all_selector_definition** | [**MatchAllSelectorDefinition**](MatchAllSelectorDefinition.md) |  | [optional] 
**policy_selector_definition** | [**PolicySelectorDefinition**](PolicySelectorDefinition.md) |  | [optional] 
## Example

```python
from finbourne_access.models.selector_definition import SelectorDefinition
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

metadata_selector_definition: Optional[MetadataSelectorDefinition] = # Replace with your value
id_selector_definition: Optional[IdSelectorDefinition] = # Replace with your value
match_all_selector_definition: Optional[MatchAllSelectorDefinition] = # Replace with your value
policy_selector_definition: Optional[PolicySelectorDefinition] = # Replace with your value
selector_definition_instance = SelectorDefinition(metadata_selector_definition=metadata_selector_definition, id_selector_definition=id_selector_definition, match_all_selector_definition=match_all_selector_definition, policy_selector_definition=policy_selector_definition)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

