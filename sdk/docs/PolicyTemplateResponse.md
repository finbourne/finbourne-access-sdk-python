# PolicyTemplateResponse

Response object for a policy template
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display name of the policy template being created | [optional] 
**scope** | **str** | The Scope of the policy template being created | [optional] 
**code** | **str** | The Code of the policy template being created | [optional] 
**description** | **str** | Description of the policy template being created | [optional] 
**applications** | **List[str]** | List of applications that this policy template covers | [optional] 
**tags** | **List[str]** | List of policy types that this policy template covers | [optional] 
**templated_selectors** | [**List[PolicyTemplatedSelector]**](PolicyTemplatedSelector.md) | The selector definitions of policies included in this policy template | [optional] 
## Example

```python
from finbourne_access.models.policy_template_response import PolicyTemplateResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

display_name: Optional[StrictStr] = "example_display_name"
scope: Optional[StrictStr] = "example_scope"
code: Optional[StrictStr] = "example_code"
description: Optional[StrictStr] = "example_description"
applications: Optional[conlist(StrictStr)] = # Replace with your value
tags: Optional[conlist(StrictStr)] = # Replace with your value
templated_selectors: Optional[conlist(PolicyTemplatedSelector)] = # Replace with your value
policy_template_response_instance = PolicyTemplateResponse(display_name=display_name, scope=scope, code=code, description=description, applications=applications, tags=tags, templated_selectors=templated_selectors)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

