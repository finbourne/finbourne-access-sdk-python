# EvaluationRequest

Specification for a server side evaluation of entitlement.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | [**RequestDetails**](RequestDetails.md) |  | 
**resource** | [**ResourceDetails**](ResourceDetails.md) |  | 

## Example

```python
from finbourne_access.models.evaluation_request import EvaluationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationRequest from a JSON string
evaluation_request_instance = EvaluationRequest.from_json(json)
# print the JSON string representation of the object
print EvaluationRequest.to_json()

# convert the object into a dict
evaluation_request_dict = evaluation_request_instance.to_dict()
# create an instance of EvaluationRequest from a dict
evaluation_request_form_dict = evaluation_request.from_dict(evaluation_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


