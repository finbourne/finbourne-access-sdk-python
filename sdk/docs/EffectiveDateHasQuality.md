# EffectiveDateHasQuality

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quality** | [**DateQuality**](DateQuality.md) |  | [optional] 
## Example

```python
from finbourne_access.models.effective_date_has_quality import EffectiveDateHasQuality
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel

quality: Optional[DateQuality] = None
effective_date_has_quality_instance = EffectiveDateHasQuality(quality=quality)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

