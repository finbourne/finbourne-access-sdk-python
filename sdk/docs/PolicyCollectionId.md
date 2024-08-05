# PolicyCollectionId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | [optional] 
**code** | **str** |  | 

## Example

```python
from finbourne_access.models.policy_collection_id import PolicyCollectionId

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyCollectionId from a JSON string
policy_collection_id_instance = PolicyCollectionId.from_json(json)
# print the JSON string representation of the object
print PolicyCollectionId.to_json()

# convert the object into a dict
policy_collection_id_dict = policy_collection_id_instance.to_dict()
# create an instance of PolicyCollectionId from a dict
policy_collection_id_form_dict = policy_collection_id.from_dict(policy_collection_id_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


