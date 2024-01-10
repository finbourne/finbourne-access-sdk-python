# GeneratePolicyFromTemplateRequest

Generate policy from template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_selection** | [**List[TemplateSelection]**](TemplateSelection.md) | List of template selection, identifying policy templates to use for generation | 

## Example

```python
from finbourne_access.models.generate_policy_from_template_request import GeneratePolicyFromTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratePolicyFromTemplateRequest from a JSON string
generate_policy_from_template_request_instance = GeneratePolicyFromTemplateRequest.from_json(json)
# print the JSON string representation of the object
print GeneratePolicyFromTemplateRequest.to_json()

# convert the object into a dict
generate_policy_from_template_request_dict = generate_policy_from_template_request_instance.to_dict()
# create an instance of GeneratePolicyFromTemplateRequest from a dict
generate_policy_from_template_request_form_dict = generate_policy_from_template_request.from_dict(generate_policy_from_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


