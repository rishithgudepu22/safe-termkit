"""Custom exceptions for safe_termkit."""

from __future__ import annotations


class SafeTermkitError(Exception):
    """Base exception for all SafeTermkit errors.

    Attributes:
        message: Human-readable error description.
        code: Optional machine-readable error code.
    """

    def __init__(self, message: str, code: str | None = None) -> None:
        super().__init__(message)
        self.code = code


class ConfigurationError(SafeTermkitError):
    """Raised when the SDK is misconfigured."""


class ValidationError(SafeTermkitError):
    """Raised when input validation fails."""


class TimeoutError(SafeTermkitError):
    """Raised when an operation exceeds its time limit."""
