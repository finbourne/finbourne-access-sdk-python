# PolicyCollectionResponse

A PolicyCollection encapsulating one or more Policies and PolicyCollections

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**PolicyCollectionId**](PolicyCollectionId.md) |  | [optional] 
**policies** | [**List[PolicyId]**](PolicyId.md) | The identifiers of the Policies in this collection | [optional] 
**policy_collections** | [**List[PolicyCollectionId]**](PolicyCollectionId.md) | The identifiers of the PolicyCollections in this collection | [optional] 
**description** | **str** | A description of this policy collection | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from finbourne_access.models.policy_collection_response import PolicyCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyCollectionResponse from a JSON string
policy_collection_response_instance = PolicyCollectionResponse.from_json(json)
# print the JSON string representation of the object
print PolicyCollectionResponse.to_json()

# convert the object into a dict
policy_collection_response_dict = policy_collection_response_instance.to_dict()
# create an instance of PolicyCollectionResponse from a dict
policy_collection_response_form_dict = policy_collection_response.from_dict(policy_collection_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


