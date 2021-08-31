# PolicyResponse

Response object from the policy API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**PolicyId**](PolicyId.md) |  | [optional] 
**description** | **str** | Description of what the policy is entitling | [optional] 
**applications** | **list[str]** | Applications to which the policy applies | [optional] 
**grant** | [**Grant**](Grant.md) |  | [optional] 
**selectors** | [**list[SelectorDefinition]**](SelectorDefinition.md) | Selectors that this policy will be applied to | [optional] 
**_for** | [**list[ForSpec]**](ForSpec.md) | \&quot;For Specification\&quot; for when the policy is to be applied | [optional] 
**_if** | [**list[IfExpression]**](IfExpression.md) | \&quot;If Specification\&quot; for when the policy is to be applied | [optional] 
**when** | [**WhenSpec**](WhenSpec.md) |  | [optional] 
**how** | [**HowSpec**](HowSpec.md) |  | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


