# PolicyCreationRequest

Request to create a policy
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the policy being created | 
**description** | **str** | Description of what the policy will be used for | [optional] 
**applications** | **List[str]** | Applications this policy is used with | [optional] 
**grant** | [**Grant**](Grant.md) |  | 
**selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) | Selectors that identify what resources this policy qualifies for | 
**var_for** | [**List[ForSpec]**](ForSpec.md) | \&quot;For Specification\&quot; for when the policy is to be applied | [optional] 
**var_if** | [**List[IfExpression]**](IfExpression.md) | \&quot;If Specification\&quot; for when the policy is to be applied | [optional] 
**when** | [**WhenSpec**](WhenSpec.md) |  | 
**how** | [**HowSpec**](HowSpec.md) |  | [optional] 
**template_metadata** | [**TemplateMetadata**](TemplateMetadata.md) |  | [optional] 
## Example

```python
from finbourne_access.models.policy_creation_request import PolicyCreationRequest
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr, validator

code: StrictStr = "example_code"
description: Optional[StrictStr] = "example_description"
applications: Optional[conlist(StrictStr)] = # Replace with your value
grant: Grant = # Replace with your value
selectors: conlist(SelectorDefinition) = # Replace with your value
var_for: Optional[conlist(ForSpec)] = # Replace with your value
var_if: Optional[conlist(IfExpression)] = # Replace with your value
when: WhenSpec = # Replace with your value
how: Optional[HowSpec] = None
template_metadata: Optional[TemplateMetadata] = # Replace with your value
policy_creation_request_instance = PolicyCreationRequest(code=code, description=description, applications=applications, grant=grant, selectors=selectors, var_for=var_for, var_if=var_if, when=when, how=how, template_metadata=template_metadata)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

