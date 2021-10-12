# RoleResponse

Response object from the role API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**RoleId**](RoleId.md) |  | 
**role_hierarchy_index** | **int** | The hierarchical index of the role | 
**description** | **str** | The description of the role | [optional] 
**resource** | [**RoleResourceRequest**](RoleResourceRequest.md) |  | 
**when** | [**WhenSpec**](WhenSpec.md) |  | 
**permission** | **str** | The action key of the role | 
**limit** | **dict(str, str)** | The identifiers of the role with the maximum privileges that this role can have | [optional] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


