# PolicyCollectionUpdateRequest

Update an existing PolicyCollection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**list[PolicyId]**](PolicyId.md) | The identifiers of the Policies in this collection | [optional] 
**metadata** | **dict(str, list[EntitlementMetadata])** | Any relevant metadata associated with this resource for controlling access to this resource | [optional] 
**policy_collections** | [**list[PolicyCollectionId]**](PolicyCollectionId.md) | The identifiers of the PolicyCollections in this collection | [optional] 
**description** | **str** | A description of this policy collection | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


