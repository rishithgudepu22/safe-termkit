"""Tests for safe_termkit."""

from safe_termkit import SafeTermkit, SafeTermkitOptions


class TestSafeTermkit:
    def test_create_instance_with_defaults(self) -> None:
        instance = SafeTermkit()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = SafeTermkitOptions(verbose=True)
        instance = SafeTermkit(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = SafeTermkit()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = SafeTermkit()
        result = instance.run()
        assert result.error is None
