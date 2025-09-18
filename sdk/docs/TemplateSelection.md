# TemplateSelection

A template selection, identifying a policy template to use for generation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | Scope identifying policy template to use for generation | 
**code** | **str** | Code identifying policy template to use for generation | 
**selector_tags** | **List[str]** | List of selector tags to optionally filter in the template generation  (Eg: Feature, Data, etc) | [optional] 
## Example

```python
from finbourne_access.models.template_selection import TemplateSelection
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

scope: StrictStr = "example_scope"
code: StrictStr = "example_code"
selector_tags: Optional[conlist(StrictStr)] = # Replace with your value
template_selection_instance = TemplateSelection(scope=scope, code=code, selector_tags=selector_tags)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

