# safe_termkit

Generate SAFE notes, cap tables, and dilution reports from structured financing inputs.

## Installation

```bash
pip install safe_termkit
```

## Quick Start

```python
from safe_termkit import SafeTermkit

instance = SafeTermkit()
result = instance.run()
print(result)
```

## Features

- SAFE variants (post-money, pre-money, MFN) payoff and conversion modeling
- Cap table engine with option pool, pro-rata, and priced-round conversion
- Deterministic dilution reports (JSON + PDF/Markdown render helpers)
- Input validation and scenario comparison (best/base/worst) helpers

## API Reference

### `SafeTermkit`

#### Constructor

```python
SafeTermkit(options: SafeTermkitOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `SafeTermkitResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/safe_termkit/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT
