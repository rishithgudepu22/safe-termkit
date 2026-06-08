"""Core module for safe_termkit."""

from .types import SafeTermkitOptions, SafeTermkitResult


class SafeTermkit:
    """Generate SAFE notes, cap tables, and dilution reports from structured financing inputs.

    Example::

        from safe_termkit import SafeTermkit

        instance = SafeTermkit()
        result = instance.run()
        print(result)
    """

    def __init__(self, options: SafeTermkitOptions | None = None) -> None:
        self.options = options or SafeTermkitOptions()

    def run(self) -> SafeTermkitResult:
        """Execute the main operation.

        Returns:
            SafeTermkitResult with the operation outcome.
        """
        # TODO: Implement core functionality
        # Key features to implement:
        #   - SAFE variants (post-money, pre-money, MFN) payoff and conversion modeling
        #   - Cap table engine with option pool, pro-rata, and priced-round conversion
        #   - Deterministic dilution reports (JSON + PDF/Markdown render helpers)
        #   - Input validation and scenario comparison (best/base/worst) helpers

        return SafeTermkitResult(
            success=True,
            data={"message": "SafeTermkit is working!"},
        )
