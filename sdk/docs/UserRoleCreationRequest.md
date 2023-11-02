# UserRoleCreationRequest

Dto used to request creating a user's role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The Id of the user for whom to create the role. | 
**resource** | [**PolicyIdRoleResource**](PolicyIdRoleResource.md) |  | 

## Example

```python
from finbourne_access.models.user_role_creation_request import UserRoleCreationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserRoleCreationRequest from a JSON string
user_role_creation_request_instance = UserRoleCreationRequest.from_json(json)
# print the JSON string representation of the object
print UserRoleCreationRequest.to_json()

# convert the object into a dict
user_role_creation_request_dict = user_role_creation_request_instance.to_dict()
# create an instance of UserRoleCreationRequest from a dict
user_role_creation_request_form_dict = user_role_creation_request.from_dict(user_role_creation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


