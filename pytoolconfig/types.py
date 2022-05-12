import sys
from datetime import date, datetime, time
from typing import Dict, List, Optional, Union, Tuple

from pydantic import BaseModel, Field

_base_types = Union[str, int, float, datetime, date, time, bool]
_base_types_with_list = Union[_base_types, List[_base_types]]
key = Union[Dict[str, _base_types_with_list], _base_types_with_list]


class UniversalConfig(BaseModel):
    """Universal Configuration base model."""

    formatter: Optional[str] = Field(
        default=None, description="Formatter used to format this File."
    )
    max_line_length: int = Field(default=80, gt=5, description="Maximum line length.")
    min_py_version: Tuple[int, int] = Field(
        default=(sys.version_info.major, sys.version_info.minor),
        description="Mimimum target python version. Taken from requires-python.",
    )