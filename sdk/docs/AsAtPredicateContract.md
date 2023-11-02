# AsAtPredicateContract


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**date_time_offset** | **datetime** |  | [optional] 

## Example

```python
from finbourne_access.models.as_at_predicate_contract import AsAtPredicateContract

# TODO update the JSON string below
json = "{}"
# create an instance of AsAtPredicateContract from a JSON string
as_at_predicate_contract_instance = AsAtPredicateContract.from_json(json)
# print the JSON string representation of the object
print AsAtPredicateContract.to_json()

# convert the object into a dict
as_at_predicate_contract_dict = as_at_predicate_contract_instance.to_dict()
# create an instance of AsAtPredicateContract from a dict
as_at_predicate_contract_form_dict = as_at_predicate_contract.from_dict(as_at_predicate_contract_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


