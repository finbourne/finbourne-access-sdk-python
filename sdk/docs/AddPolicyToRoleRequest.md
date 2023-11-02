# AddPolicyToRoleRequest

Request body used to add Policies to a Role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[PolicyId]**](PolicyId.md) | Identifiers of policies to add to a role | 

## Example

```python
from finbourne_access.models.add_policy_to_role_request import AddPolicyToRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPolicyToRoleRequest from a JSON string
add_policy_to_role_request_instance = AddPolicyToRoleRequest.from_json(json)
# print the JSON string representation of the object
print AddPolicyToRoleRequest.to_json()

# convert the object into a dict
add_policy_to_role_request_dict = add_policy_to_role_request_instance.to_dict()
# create an instance of AddPolicyToRoleRequest from a dict
add_policy_to_role_request_form_dict = add_policy_to_role_request.from_dict(add_policy_to_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


