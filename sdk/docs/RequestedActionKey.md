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
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, constr, validator

entity_code: StrictStr = "example_entity_code"
scope: StrictStr = "example_scope"
activity: StrictStr = "example_activity"
requested_action_key_instance = RequestedActionKey(entity_code=entity_code, scope=scope, activity=activity)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

