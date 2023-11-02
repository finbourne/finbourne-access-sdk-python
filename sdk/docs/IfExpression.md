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

# TODO update the JSON string below
json = "{}"
# create an instance of IfExpression from a JSON string
if_expression_instance = IfExpression.from_json(json)
# print the JSON string representation of the object
print IfExpression.to_json()

# convert the object into a dict
if_expression_dict = if_expression_instance.to_dict()
# create an instance of IfExpression from a dict
if_expression_form_dict = if_expression.from_dict(if_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


