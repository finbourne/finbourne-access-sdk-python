# AddPolicyCollectionToRoleRequest

Request body used to add Policy Collections to a Role

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) | Identifiers of policy collections to add to a role | 

## Example

```python
from finbourne_access.models.add_policy_collection_to_role_request import AddPolicyCollectionToRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPolicyCollectionToRoleRequest from a JSON string
add_policy_collection_to_role_request_instance = AddPolicyCollectionToRoleRequest.from_json(json)
# print the JSON string representation of the object
print AddPolicyCollectionToRoleRequest.to_json()

# convert the object into a dict
add_policy_collection_to_role_request_dict = add_policy_collection_to_role_request_instance.to_dict()
# create an instance of AddPolicyCollectionToRoleRequest from a dict
add_policy_collection_to_role_request_form_dict = add_policy_collection_to_role_request.from_dict(add_policy_collection_to_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


