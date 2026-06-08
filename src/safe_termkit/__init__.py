"""
safe_termkit - Generate SAFE notes, cap tables, and dilution reports from structured financing inputs.
"""

__version__ = "0.1.0"

from .safe_variants_postmoney_premon import SafeTermkit
from .types import SafeTermkitOptions, SafeTermkitResult
from .exceptions import SafeTermkitError, ConfigurationError, ValidationError

__all__ = [
    "SafeTermkit",
    "SafeTermkitOptions",
    "SafeTermkitResult",
    "SafeTermkitError",
    "ConfigurationError",
    "ValidationError",
]
