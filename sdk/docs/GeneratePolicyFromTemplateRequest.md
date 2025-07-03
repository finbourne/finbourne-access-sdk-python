# GeneratePolicyFromTemplateRequest

Generate policy from template
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_selection** | [**List[TemplateSelection]**](TemplateSelection.md) | List of template selection, identifying policy templates to use for generation | 
**selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) | List of additional selectors to be included in the policy | [optional] 
## Example

```python
from finbourne_access.models.generate_policy_from_template_request import GeneratePolicyFromTemplateRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist

template_selection: conlist(TemplateSelection, max_items=100) = Field(..., alias="templateSelection", description="List of template selection, identifying policy templates to use for generation")
selectors: Optional[conlist(SelectorDefinition, max_items=100)] = Field(None, description="List of additional selectors to be included in the policy")
generate_policy_from_template_request_instance = GeneratePolicyFromTemplateRequest(template_selection=template_selection, selectors=selectors)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

