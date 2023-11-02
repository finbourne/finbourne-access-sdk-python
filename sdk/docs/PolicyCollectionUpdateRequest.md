# PolicyCollectionUpdateRequest

Update an existing PolicyCollection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[PolicyId]**](PolicyId.md) | The identifiers of the Policies in this collection | [optional] 
**metadata** | **Dict[str, List[EntitlementMetadata]]** | Any relevant metadata associated with this resource for controlling access to this resource | [optional] 
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) | The identifiers of the PolicyCollections in this collection | [optional] 
**description** | **str** | A description of this policy collection | [optional] 

## Example

```python
from finbourne_access.models.policy_collection_update_request import PolicyCollectionUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyCollectionUpdateRequest from a JSON string
policy_collection_update_request_instance = PolicyCollectionUpdateRequest.from_json(json)
# print the JSON string representation of the object
print PolicyCollectionUpdateRequest.to_json()

# convert the object into a dict
policy_collection_update_request_dict = policy_collection_update_request_instance.to_dict()
# create an instance of PolicyCollectionUpdateRequest from a dict
policy_collection_update_request_form_dict = policy_collection_update_request.from_dict(policy_collection_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


