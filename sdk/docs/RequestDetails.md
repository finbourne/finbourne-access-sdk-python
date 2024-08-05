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

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDetails from a JSON string
request_details_instance = RequestDetails.from_json(json)
# print the JSON string representation of the object
print RequestDetails.to_json()

# convert the object into a dict
request_details_dict = request_details_instance.to_dict()
# create an instance of RequestDetails from a dict
request_details_form_dict = request_details.from_dict(request_details_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


