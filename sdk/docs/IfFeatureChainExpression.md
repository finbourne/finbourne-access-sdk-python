# IfFeatureChainExpression

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) |  | 
## Example

```python
from finbourne_access.models.if_feature_chain_expression import IfFeatureChainExpression
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

selectors: List[SelectorDefinition]
if_feature_chain_expression_instance = IfFeatureChainExpression(selectors=selectors)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

