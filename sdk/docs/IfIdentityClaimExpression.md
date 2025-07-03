# IfIdentityClaimExpression

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claim_type** | **str** |  | 
**claim_value_type** | **str** |  | [optional] 
**claim_issuer** | **str** |  | [optional] 
**claim_original_issuer** | **str** |  | [optional] 
**operator** | [**TextOperator**](TextOperator.md) |  | 
**value** | **str** |  | [optional] 
## Example

```python
from finbourne_access.models.if_identity_claim_expression import IfIdentityClaimExpression
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, constr

claim_type: StrictStr = "example_claim_type"
claim_value_type: Optional[StrictStr] = "example_claim_value_type"
claim_issuer: Optional[StrictStr] = "example_claim_issuer"
claim_original_issuer: Optional[StrictStr] = "example_claim_original_issuer"
operator: TextOperator = # Replace with your value
value: Optional[StrictStr] = "example_value"
if_identity_claim_expression_instance = IfIdentityClaimExpression(claim_type=claim_type, claim_value_type=claim_value_type, claim_issuer=claim_issuer, claim_original_issuer=claim_original_issuer, operator=operator, value=value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

