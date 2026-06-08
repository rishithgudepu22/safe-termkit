"""Type definitions for safe_termkit."""

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class SafeTermkitOptions:
    """Configuration options for SafeTermkit.

    Attributes:
        verbose: Enable verbose logging for debugging.
        feature_1: Configuration for: SAFE variants (post-money, pre-money, MFN) payoff and conversion modeling
        feature_2: Configuration for: Cap table engine with option pool, pro-rata, and priced-round conversion
        feature_3: Configuration for: Deterministic dilution reports (JSON + PDF/Markdown render helpers)
        feature_4: Configuration for: Input validation and scenario comparison (best/base/worst) helpers
    """

    verbose: bool = False
    feature_1: Optional[dict[str, Any]] = None
    feature_2: Optional[dict[str, Any]] = None
    feature_3: Optional[dict[str, Any]] = None
    feature_4: Optional[dict[str, Any]] = None


@dataclass
class SafeTermkitResult:
    """Result returned by SafeTermkit operations.

    Attributes:
        success: Whether the operation succeeded.
        data: The result data, if successful.
        error: Error message, if the operation failed.
    """

    success: bool
    data: Any = field(default=None)
    error: Optional[str] = None
