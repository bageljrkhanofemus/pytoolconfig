"""Universal Configuration base model."""
from typing import Dict, List, Optional, Tuple

from packaging.requirements import Requirement

from .fields import field
from .types import dataclass


@dataclass
class UniversalConfig:
    """Universal Configuration base model."""

    formatter: Optional[str] = field(None, "Formatter used to format this File")
    max_line_length: Optional[int] = field(None, description="Maximum line length")

    min_py_version: Optional[Tuple[int, int]] = field(
        None, "Mimimum target python version. Requires PEP 621."
    )
    max_py_version: Optional[Tuple[int, int]] = field(
        None, "Maximum target python version. Requires PEP 621."
    )
    dependencies: Optional[List[Requirement]] = field(
        None, "Dependencies of project. Requires PEP 621."
    )
    optional_dependencies: Optional[Dict[str, List[Requirement]]] = field(
        None, "Optional dependencies of project. Requires PEP 621."
    )
