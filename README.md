# Workflow
1. Issue Analysis
    - Give LLM Github issue + relevant context
    - Generate high-level Plan
    - Break down Plan into executable Tasks
    - Refine Tasks with codespace details
2. Execution
    - Try to implement a Task
    - Validate Task implementation
    - If successful: continue to next Task
    - If unsuccessful: debug + re-validate
3. Review
    - Ensure components make sense and still run as intended
    - Ensure code quality (lint) and functionality (unit tests)
4. Cleanup
    - Push code to Github under a new branch
    - Clean up cloned files


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