# IfFeatureChainExpression

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) |  | 
## Example

```python
from finbourne_access.models.if_feature_chain_expression import IfFeatureChainExpression
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, conlist

selectors: conlist(SelectorDefinition) = # Replace with your value
if_feature_chain_expression_instance = IfFeatureChainExpression(selectors=selectors)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

