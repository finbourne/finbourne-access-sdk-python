# ForSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_at_range_for_spec** | [**AsAtRangeForSpec**](AsAtRangeForSpec.md) |  | [optional] 
**as_at_relative** | [**AsAtRelative**](AsAtRelative.md) |  | [optional] 
**effective_date_has_quality** | [**EffectiveDateHasQuality**](EffectiveDateHasQuality.md) |  | [optional] 
**effective_date_relative** | [**EffectiveDateRelative**](EffectiveDateRelative.md) |  | [optional] 
**effective_range** | [**EffectiveRange**](EffectiveRange.md) |  | [optional] 
## Example

```python
from finbourne_access.models.for_spec import ForSpec
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field

as_at_range_for_spec: Optional[AsAtRangeForSpec] = # Replace with your value
as_at_relative: Optional[AsAtRelative] = # Replace with your value
effective_date_has_quality: Optional[EffectiveDateHasQuality] = # Replace with your value
effective_date_relative: Optional[EffectiveDateRelative] = # Replace with your value
effective_range: Optional[EffectiveRange] = # Replace with your value
for_spec_instance = ForSpec(as_at_range_for_spec=as_at_range_for_spec, as_at_relative=as_at_relative, effective_date_has_quality=effective_date_has_quality, effective_date_relative=effective_date_relative, effective_range=effective_range)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

