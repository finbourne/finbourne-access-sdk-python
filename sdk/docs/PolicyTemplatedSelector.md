# PolicyTemplatedSelector

Templated selector for a policy template
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** | The application that this selector definition applies to | 
**tag** | **str** | The type of policy that this selector definition applies to | 
**selector** | [**SelectorDefinition**](SelectorDefinition.md) |  | 
## Example

```python
from finbourne_access.models.policy_templated_selector import PolicyTemplatedSelector
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

application: StrictStr = "example_application"
tag: StrictStr = "example_tag"
selector: SelectorDefinition
policy_templated_selector_instance = PolicyTemplatedSelector(application=application, tag=tag, selector=selector)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

