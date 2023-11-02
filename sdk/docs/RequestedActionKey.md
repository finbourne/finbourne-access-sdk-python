# RequestedActionKey

A fully qualified action identifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_code** | **str** | The type of the resource on which the activity would be performed | 
**scope** | **str** | The scope/provider/vendor of the activity | 
**activity** | **str** | The identifier of the action to be performed on the resource | 

## Example

```python
from finbourne_access.models.requested_action_key import RequestedActionKey

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedActionKey from a JSON string
requested_action_key_instance = RequestedActionKey.from_json(json)
# print the JSON string representation of the object
print RequestedActionKey.to_json()

# convert the object into a dict
requested_action_key_dict = requested_action_key_instance.to_dict()
# create an instance of RequestedActionKey from a dict
requested_action_key_form_dict = requested_action_key.from_dict(requested_action_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


