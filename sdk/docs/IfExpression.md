# IfExpression

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**if_request_header_expression** | [**IfRequestHeaderExpression**](IfRequestHeaderExpression.md) |  | [optional] 
**if_identity_claim_expression** | [**IfIdentityClaimExpression**](IfIdentityClaimExpression.md) |  | [optional] 
**if_identity_scope_expression** | [**IfIdentityScopeExpression**](IfIdentityScopeExpression.md) |  | [optional] 
**if_feature_chain_expression** | [**IfFeatureChainExpression**](IfFeatureChainExpression.md) |  | [optional] 
## Example

```python
from finbourne_access.models.if_expression import IfExpression
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

if_request_header_expression: Optional[IfRequestHeaderExpression] = # Replace with your value
if_identity_claim_expression: Optional[IfIdentityClaimExpression] = # Replace with your value
if_identity_scope_expression: Optional[IfIdentityScopeExpression] = # Replace with your value
if_feature_chain_expression: Optional[IfFeatureChainExpression] = # Replace with your value
if_expression_instance = IfExpression(if_request_header_expression=if_request_header_expression, if_identity_claim_expression=if_identity_claim_expression, if_identity_scope_expression=if_identity_scope_expression, if_feature_chain_expression=if_feature_chain_expression)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

