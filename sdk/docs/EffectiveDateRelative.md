# EffectiveDateRelative

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**PointInTimeSpecification**](PointInTimeSpecification.md) |  | [optional] 
**adjustment** | **int** |  | [optional] 
**unit** | [**DateUnit**](DateUnit.md) |  | [optional] 
**relative_to_date_time** | [**RelativeToDateTime**](RelativeToDateTime.md) |  | [optional] 
## Example

```python
from finbourne_access.models.effective_date_relative import EffectiveDateRelative
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictInt

var_date: Optional[PointInTimeSpecification] = # Replace with your value
adjustment: Optional[StrictInt] = None
adjustment: Optional[StrictInt] = None
unit: Optional[DateUnit] = None
relative_to_date_time: Optional[RelativeToDateTime] = # Replace with your value
effective_date_relative_instance = EffectiveDateRelative(var_date=var_date, adjustment=adjustment, unit=unit, relative_to_date_time=relative_to_date_time)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

