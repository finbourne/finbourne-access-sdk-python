# GeneratedPolicyComponents

Response object for policy generated from template
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | **List[str]** | Applications to which the policy applies | [optional] 
**template_metadata** | [**TemplateMetadata**](TemplateMetadata.md) |  | [optional] 
**selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) | Selectors that this policy will be applied to | [optional] 
## Example

```python
from finbourne_access.models.generated_policy_components import GeneratedPolicyComponents
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

applications: Optional[List[StrictStr]] = # Replace with your value
template_metadata: Optional[TemplateMetadata] = # Replace with your value
selectors: Optional[List[SelectorDefinition]] = # Replace with your value
generated_policy_components_instance = GeneratedPolicyComponents(applications=applications, template_metadata=template_metadata, selectors=selectors)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

