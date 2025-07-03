# PolicyResponse

Response object from the policy API
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**PolicyId**](PolicyId.md) |  | [optional] 
**description** | **str** | Description of what the policy is entitling | [optional] 
**applications** | **List[str]** | Applications to which the policy applies | [optional] 
**grant** | [**Grant**](Grant.md) |  | [optional] 
**selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) | Selectors that this policy will be applied to | [optional] 
**var_for** | [**List[ForSpec]**](ForSpec.md) | \&quot;For Specification\&quot; for when the policy is to be applied | [optional] 
**var_if** | [**List[IfExpression]**](IfExpression.md) | \&quot;If Specification\&quot; for when the policy is to be applied | [optional] 
**when** | [**WhenSpec**](WhenSpec.md) |  | [optional] 
**how** | [**HowSpec**](HowSpec.md) |  | [optional] 
**template_metadata** | [**TemplateMetadata**](TemplateMetadata.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from finbourne_access.models.policy_response import PolicyResponse
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

id: Optional[PolicyId] = None
description: Optional[StrictStr] = "example_description"
applications: Optional[conlist(StrictStr)] = # Replace with your value
grant: Optional[Grant] = None
selectors: Optional[conlist(SelectorDefinition)] = # Replace with your value
var_for: Optional[conlist(ForSpec)] = # Replace with your value
var_if: Optional[conlist(IfExpression)] = # Replace with your value
when: Optional[WhenSpec] = None
how: Optional[HowSpec] = None
template_metadata: Optional[TemplateMetadata] = # Replace with your value
links: Optional[conlist(Link)] = None
policy_response_instance = PolicyResponse(id=id, description=description, applications=applications, grant=grant, selectors=selectors, var_for=var_for, var_if=var_if, when=when, how=how, template_metadata=template_metadata, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

