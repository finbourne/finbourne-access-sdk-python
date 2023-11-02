# AddToPolicyCollectionRequest

Base properties to create or update a policy collection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policies** | [**List[PolicyId]**](PolicyId.md) | The identifiers of the Policies to be added to the collection. | [optional] 
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) | The identifiers of the PolicyCollections to be added to the collection. | [optional] 

## Example

```python
from finbourne_access.models.add_to_policy_collection_request import AddToPolicyCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddToPolicyCollectionRequest from a JSON string
add_to_policy_collection_request_instance = AddToPolicyCollectionRequest.from_json(json)
# print the JSON string representation of the object
print AddToPolicyCollectionRequest.to_json()

# convert the object into a dict
add_to_policy_collection_request_dict = add_to_policy_collection_request_instance.to_dict()
# create an instance of AddToPolicyCollectionRequest from a dict
add_to_policy_collection_request_form_dict = add_to_policy_collection_request.from_dict(add_to_policy_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


