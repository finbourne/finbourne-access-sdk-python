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
**limit** | **Dict[str, str]** | The identifiers of the role with the maximum privileges that this role can have | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_access.models.role_response import RoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoleResponse from a JSON string
role_response_instance = RoleResponse.from_json(json)
# print the JSON string representation of the object
print RoleResponse.to_json()

# convert the object into a dict
role_response_dict = role_response_instance.to_dict()
# create an instance of RoleResponse from a dict
role_response_form_dict = role_response.from_dict(role_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


