# TemplateMetadata

Extra policy template metadata information, used during a generation request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_selection** | [**List[TemplateSelection]**](TemplateSelection.md) | List of policy templates used for a generation request | [optional] 
**build_as_at** | **datetime** | Policy template build AsAt time used for a generation request | [optional] 
## Example

```python
from finbourne_access.models.template_metadata import TemplateMetadata
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

template_selection: Optional[List[TemplateSelection]] = # Replace with your value
build_as_at: Optional[datetime] = # Replace with your value
template_metadata_instance = TemplateMetadata(template_selection=template_selection, build_as_at=build_as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

