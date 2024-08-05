# UserRoleUpdateRequest

Dto used to request updating a user's role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**PolicyIdRoleResource**](PolicyIdRoleResource.md) |  | 

## Example

```python
from finbourne_access.models.user_role_update_request import UserRoleUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleUpdateRequest from a JSON string
user_role_update_request_instance = UserRoleUpdateRequest.from_json(json)
# print the JSON string representation of the object
print UserRoleUpdateRequest.to_json()

# convert the object into a dict
user_role_update_request_dict = user_role_update_request_instance.to_dict()
# create an instance of UserRoleUpdateRequest from a dict
user_role_update_request_form_dict = user_role_update_request.from_dict(user_role_update_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


