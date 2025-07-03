# RequestDetails

The details of the requested evaluation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**RequestedActionKey**](RequestedActionKey.md) |  | 
**from_effective_date** | **datetime** | The start date for the requested effective date range for the resource (if null, UtcNow) | [optional] 
**to_effective_date** | **datetime** | The end date for the requested effective date range for the resource (if null, same as from date) | [optional] 
**from_as_at** | **datetime** | The requested AsAt date for the resource (if null, Latest). If specifying a range of AsAt dates, this is the lower bounds. | [optional] 
**to_as_at** | **datetime** | Upper bound if specifying a request that requires a range of AsAt dates. This is used if specifying the desire to grant access for a user between an AsAt range. | [optional] 
## Example

```python
from finbourne_access.models.request_details import RequestDetails
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field
from datetime import datetime
action: RequestedActionKey = # Replace with your value
from_effective_date: Optional[datetime] = # Replace with your value
to_effective_date: Optional[datetime] = # Replace with your value
from_as_at: Optional[datetime] = # Replace with your value
to_as_at: Optional[datetime] = # Replace with your value
request_details_instance = RequestDetails(action=action, from_effective_date=from_effective_date, to_effective_date=to_effective_date, from_as_at=from_as_at, to_as_at=to_as_at)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

