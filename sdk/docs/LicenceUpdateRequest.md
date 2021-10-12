# LicenceUpdateRequest

Request to update a licence policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description of the licence&#39;s purpose. | 
**applications** | **list[str]** | The applications that the licence refers to. | 
**selectors** | [**list[LicenceSelectorDefinition]**](LicenceSelectorDefinition.md) | The selectors affected by the licence. | 
**when** | [**WhenSpec**](WhenSpec.md) |  | 
**_for** | [**list[ForSpec]**](ForSpec.md) | The ForSpecs of the licence. | [optional] 
**how** | [**HowSpec**](HowSpec.md) |  | [optional] 
**_if** | [**list[IfExpression]**](IfExpression.md) | The IfSpecs of the licence. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


