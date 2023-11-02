# RoleResourceRequest

RoleResourceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**non_transitive_supervisor_role_resource** | [**NonTransitiveSupervisorRoleResource**](NonTransitiveSupervisorRoleResource.md) |  | [optional] 
**policy_id_role_resource** | [**PolicyIdRoleResource**](PolicyIdRoleResource.md) |  | [optional] 

## Example

```python
from finbourne_access.models.role_resource_request import RoleResourceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleResourceRequest from a JSON string
role_resource_request_instance = RoleResourceRequest.from_json(json)
# print the JSON string representation of the object
print RoleResourceRequest.to_json()

# convert the object into a dict
role_resource_request_dict = role_resource_request_instance.to_dict()
# create an instance of RoleResourceRequest from a dict
role_resource_request_form_dict = role_resource_request.from_dict(role_resource_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


