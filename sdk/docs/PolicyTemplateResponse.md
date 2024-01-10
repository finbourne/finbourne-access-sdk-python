# PolicyTemplateResponse

Response object for a policy template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | Display name of the policy template being created | [optional] 
**scope** | **str** | The Scope of the policy template being created | [optional] 
**code** | **str** | The Code of the policy template being created | [optional] 
**description** | **str** | Description of the policy template being created | [optional] 
**applications** | **list[str]** | List of applications that this policy template covers | [optional] 
**tags** | **list[str]** | List of policy types that this policy template covers | [optional] 
**templated_selectors** | [**list[PolicyTemplatedSelector]**](PolicyTemplatedSelector.md) | The selector definitions of policies included in this policy template | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


