# RemoveFromPolicyCollectionRequest

Base properties to create or update a policy collection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[PolicyId]**](PolicyId.md) | The identifiers of the Policies to be removed from the collection. | [optional] 
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) | The identifiers of the PolicyCollections to be removed from the collection. | [optional] 

## Example

```python
from finbourne_access.models.remove_from_policy_collection_request import RemoveFromPolicyCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveFromPolicyCollectionRequest from a JSON string
remove_from_policy_collection_request_instance = RemoveFromPolicyCollectionRequest.from_json(json)
# print the JSON string representation of the object
print RemoveFromPolicyCollectionRequest.to_json()

# convert the object into a dict
remove_from_policy_collection_request_dict = remove_from_policy_collection_request_instance.to_dict()
# create an instance of RemoveFromPolicyCollectionRequest from a dict
remove_from_policy_collection_request_form_dict = remove_from_policy_collection_request.from_dict(remove_from_policy_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


