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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

result: EvaluationResult
detailed_message: Optional[StrictStr] = "example_detailed_message"
evaluation_response_instance = EvaluationResponse(result=result, detailed_message=detailed_message)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

