# EvaluationResponse

The result of an evaluation request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**EvaluationResult**](EvaluationResult.md) |  | 
**detailed_message** | **str** | In the case of the evaluation being denied a message may be returned | [optional] 

## Example

```python
from finbourne_access.models.evaluation_response import EvaluationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluationResponse from a JSON string
evaluation_response_instance = EvaluationResponse.from_json(json)
# print the JSON string representation of the object
print EvaluationResponse.to_json()

# convert the object into a dict
evaluation_response_dict = evaluation_response_instance.to_dict()
# create an instance of EvaluationResponse from a dict
evaluation_response_form_dict = evaluation_response.from_dict(evaluation_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


