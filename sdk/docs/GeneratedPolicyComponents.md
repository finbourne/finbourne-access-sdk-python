# GeneratedPolicyComponents

Response object for policy generated from template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | **List[str]** | Applications to which the policy applies | [optional] 
**template_metadata** | [**TemplateMetadata**](TemplateMetadata.md) |  | [optional] 
**selectors** | [**List[SelectorDefinition]**](SelectorDefinition.md) | Selectors that this policy will be applied to | [optional] 

## Example

```python
from finbourne_access.models.generated_policy_components import GeneratedPolicyComponents

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratedPolicyComponents from a JSON string
generated_policy_components_instance = GeneratedPolicyComponents.from_json(json)
# print the JSON string representation of the object
print GeneratedPolicyComponents.to_json()

# convert the object into a dict
generated_policy_components_dict = generated_policy_components_instance.to_dict()
# create an instance of GeneratedPolicyComponents from a dict
generated_policy_components_form_dict = generated_policy_components.from_dict(generated_policy_components_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


