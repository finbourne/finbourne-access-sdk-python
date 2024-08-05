# EntitlementMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from finbourne_access.models.entitlement_metadata import EntitlementMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of EntitlementMetadata from a JSON string
entitlement_metadata_instance = EntitlementMetadata.from_json(json)
# print the JSON string representation of the object
print EntitlementMetadata.to_json()

# convert the object into a dict
entitlement_metadata_dict = entitlement_metadata_instance.to_dict()
# create an instance of EntitlementMetadata from a dict
entitlement_metadata_form_dict = entitlement_metadata.from_dict(entitlement_metadata_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


