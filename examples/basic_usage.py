#!/usr/bin/env python3
"""Basic usage example for safe_termkit."""

from safe_termkit import SafeTermkit, SafeTermkitOptions


def main() -> None:
    # Create with default options
    instance = SafeTermkit()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = SafeTermkitOptions(verbose=True)
    instance = SafeTermkit(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()
