# PolicyCreationRequest

Request to create a policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Code of the policy being created | 
**description** | **str** | Description of what the policy will be used for | [optional] 
**applications** | **list[str]** | Applications this policy is used with | [optional] 
**grant** | [**Grant**](Grant.md) |  | 
**selectors** | [**list[SelectorDefinition]**](SelectorDefinition.md) | Selectors that identify what resources this policy qualifies for | 
**_for** | [**list[ForSpec]**](ForSpec.md) | \&quot;For Specification\&quot; for when the policy is to be applied | [optional] 
**_if** | [**list[IfExpression]**](IfExpression.md) | \&quot;If Specification\&quot; for when the policy is to be applied | [optional] 
**when** | [**WhenSpec**](WhenSpec.md) |  | 
**how** | [**HowSpec**](HowSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


