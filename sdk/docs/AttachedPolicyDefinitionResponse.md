# AttachedPolicyDefinitionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_role** | [**RoleId**](RoleId.md) |  | [optional] 
**role_hierarchy_index** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**applications** | **List[str]** |  | [optional] 
**policy_type** | [**PolicyType**](PolicyType.md) |  | [optional] 
**id** | [**PolicyId**](PolicyId.md) |  | [optional] 
**grant** | [**Grant**](Grant.md) |  | [optional] 
**selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) |  | [optional] 
**var_for** | [**List[ForSpec]**](ForSpec.md) |  | [optional] 
**var_if** | [**List[IfExpression]**](IfExpression.md) |  | [optional] 
**when** | [**WhenSpec**](WhenSpec.md) |  | [optional] 
**how** | [**HowSpec**](HowSpec.md) |  | [optional] 
## Example

```python
from finbourne_access.models.attached_policy_definition_response import AttachedPolicyDefinitionResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

source_role: Optional[RoleId] = # Replace with your value
role_hierarchy_index: Optional[StrictInt] = # Replace with your value
role_hierarchy_index: Optional[StrictInt] = None
description: Optional[StrictStr] = "example_description"
applications: Optional[List[StrictStr]] = None
policy_type: Optional[PolicyType] = # Replace with your value
id: Optional[PolicyId] = None
grant: Optional[Grant] = None
selectors: Optional[List[SelectorDefinition]] = None
var_for: Optional[List[ForSpec]] = # Replace with your value
var_if: Optional[List[IfExpression]] = # Replace with your value
when: Optional[WhenSpec] = None
how: Optional[HowSpec] = None
attached_policy_definition_response_instance = AttachedPolicyDefinitionResponse(source_role=source_role, role_hierarchy_index=role_hierarchy_index, description=description, applications=applications, policy_type=policy_type, id=id, grant=grant, selectors=selectors, var_for=var_for, var_if=var_if, when=when, how=how)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

