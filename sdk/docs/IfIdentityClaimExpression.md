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

# TODO update the JSON string below
json = "{}"
# create an instance of IfIdentityClaimExpression from a JSON string
if_identity_claim_expression_instance = IfIdentityClaimExpression.from_json(json)
# print the JSON string representation of the object
print IfIdentityClaimExpression.to_json()

# convert the object into a dict
if_identity_claim_expression_dict = if_identity_claim_expression_instance.to_dict()
# create an instance of IfIdentityClaimExpression from a dict
if_identity_claim_expression_form_dict = if_identity_claim_expression.from_dict(if_identity_claim_expression_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


