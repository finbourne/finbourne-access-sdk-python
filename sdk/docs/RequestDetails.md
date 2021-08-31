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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


