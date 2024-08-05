# RoleCreationRequest

Request to create a role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The code of the role | 
**description** | **str** | The description of the role | [optional] 
**resource** | [**RoleResourceRequest**](RoleResourceRequest.md) |  | 
**when** | [**WhenSpec**](WhenSpec.md) |  | 

## Example

```python
from finbourne_access.models.role_creation_request import RoleCreationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RoleCreationRequest from a JSON string
role_creation_request_instance = RoleCreationRequest.from_json(json)
# print the JSON string representation of the object
print RoleCreationRequest.to_json()

# convert the object into a dict
role_creation_request_dict = role_creation_request_instance.to_dict()
# create an instance of RoleCreationRequest from a dict
role_creation_request_form_dict = role_creation_request.from_dict(role_creation_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


