# IfFeatureChainExpression


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) |  | 

## Example

```python
from finbourne_access.models.if_feature_chain_expression import IfFeatureChainExpression

# TODO update the JSON string below
json = "{}"
# create an instance of IfFeatureChainExpression from a JSON string
if_feature_chain_expression_instance = IfFeatureChainExpression.from_json(json)
# print the JSON string representation of the object
print IfFeatureChainExpression.to_json()

# convert the object into a dict
if_feature_chain_expression_dict = if_feature_chain_expression_instance.to_dict()
# create an instance of IfFeatureChainExpression from a dict
if_feature_chain_expression_form_dict = if_feature_chain_expression.from_dict(if_feature_chain_expression_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


