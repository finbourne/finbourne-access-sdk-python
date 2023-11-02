# RoleUpdateRequest

Role update does not allow the changing of the id

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the role | [optional] 
**resource** | [**RoleResourceRequest**](RoleResourceRequest.md) |  | 
**when** | [**WhenSpec**](WhenSpec.md) |  | 

## Example

```python
from finbourne_access.models.role_update_request import RoleUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleUpdateRequest from a JSON string
role_update_request_instance = RoleUpdateRequest.from_json(json)
# print the JSON string representation of the object
print RoleUpdateRequest.to_json()

# convert the object into a dict
role_update_request_dict = role_update_request_instance.to_dict()
# create an instance of RoleUpdateRequest from a dict
role_update_request_form_dict = role_update_request.from_dict(role_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


