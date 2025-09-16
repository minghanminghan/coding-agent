# Setup
```bash
git clone https://github.com/minghanminghan/coding-agent
cd coding-agent
uv sync --dev
```

## Development
```bash
# Run tests
uv run python -m pytest src/ -v

# Run linter
uv run ruff check src

# Run linter with auto-fix
uv run ruff check src --fix
```