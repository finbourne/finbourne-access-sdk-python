# PolicyIdRoleResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[PolicyId]**](PolicyId.md) |  | [optional] 
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) |  | [optional] 

## Example

```python
from finbourne_access.models.policy_id_role_resource import PolicyIdRoleResource

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyIdRoleResource from a JSON string
policy_id_role_resource_instance = PolicyIdRoleResource.from_json(json)
# print the JSON string representation of the object
print PolicyIdRoleResource.to_json()

# convert the object into a dict
policy_id_role_resource_dict = policy_id_role_resource_instance.to_dict()
# create an instance of PolicyIdRoleResource from a dict
policy_id_role_resource_form_dict = policy_id_role_resource.from_dict(policy_id_role_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


