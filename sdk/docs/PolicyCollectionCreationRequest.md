# PolicyCollectionCreationRequest

Create a PolicyCollection, a logical group of Policies or other PolicyCollections

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The identifier for the PolicyCollection being created | 
**policies** | [**List[PolicyId]**](PolicyId.md) | The identifiers of the Policies in this collection | [optional] 
**metadata** | **Dict[str, List[EntitlementMetadata]]** | Any relevant metadata associated with this resource for controlling access to this resource | [optional] 
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) | The identifiers of the PolicyCollections in this collection | [optional] 
**description** | **str** | A description of this policy collection | [optional] 

## Example

```python
from finbourne_access.models.policy_collection_creation_request import PolicyCollectionCreationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyCollectionCreationRequest from a JSON string
policy_collection_creation_request_instance = PolicyCollectionCreationRequest.from_json(json)
# print the JSON string representation of the object
print PolicyCollectionCreationRequest.to_json()

# convert the object into a dict
policy_collection_creation_request_dict = policy_collection_creation_request_instance.to_dict()
# create an instance of PolicyCollectionCreationRequest from a dict
policy_collection_creation_request_form_dict = policy_collection_creation_request.from_dict(policy_collection_creation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


