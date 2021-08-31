# AttachedPolicyDefinitionResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_role** | [**RoleId**](RoleId.md) |  | [optional] 
**role_hierarchy_index** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
**applications** | **list[str]** |  | [optional] 
**policy_type** | [**PolicyType**](PolicyType.md) |  | [optional] 
**id** | [**PolicyId**](PolicyId.md) |  | [optional] 
**grant** | [**Grant**](Grant.md) |  | [optional] 
**selectors** | [**list[SelectorDefinition]**](SelectorDefinition.md) |  | [optional] 
**_for** | [**list[ForSpec]**](ForSpec.md) |  | [optional] 
**_if** | [**list[IfExpression]**](IfExpression.md) |  | [optional] 
**when** | [**WhenSpec**](WhenSpec.md) |  | [optional] 
**how** | [**HowSpec**](HowSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


