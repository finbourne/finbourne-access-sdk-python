# UserRoleResponse

Response object from the user role API

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | [**RoleResourceRequest**](RoleResourceRequest.md) |  | 
**id** | [**RoleId**](RoleId.md) |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_access.models.user_role_response import UserRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleResponse from a JSON string
user_role_response_instance = UserRoleResponse.from_json(json)
# print the JSON string representation of the object
print UserRoleResponse.to_json()

# convert the object into a dict
user_role_response_dict = user_role_response_instance.to_dict()
# create an instance of UserRoleResponse from a dict
user_role_response_form_dict = user_role_response.from_dict(user_role_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


