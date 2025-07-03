# PolicyTemplateUpdateRequest

Update policy template request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | The display name of the policy template being created | 
**description** | **str** | Description of the policy template being craeted | 
**templated_selectors** | [**List[PolicyTemplatedSelector]**](PolicyTemplatedSelector.md) | The selector definitions of policies included in this policy template | 
## Example

```python
from finbourne_access.models.policy_template_update_request import PolicyTemplateUpdateRequest
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist, constr

display_name: StrictStr = "example_display_name"
description: StrictStr = "example_description"
templated_selectors: conlist(PolicyTemplatedSelector) = # Replace with your value
policy_template_update_request_instance = PolicyTemplateUpdateRequest(display_name=display_name, description=description, templated_selectors=templated_selectors)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

