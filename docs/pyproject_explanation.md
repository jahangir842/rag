# Understanding pyproject.toml

TOML (Tom's Obvious, Minimal Language) is a config file format designed to be easy to read and write.

The `pyproject.toml` file is the modern way to configure Python projects and manage dependencies. Here's what each section means:

## [project]

- `name`: The name of your project
- `version`: Current version of your project
- `description`: Brief description of what your project does
- `requires-python`: Specifies the Python version requirements
- `authors`: List of project authors

## [build-system]

Specifies the build requirements and backend used to build the project:

- `requires`: List of packages needed to build the project
- `build-backend`: The build backend to use

## [tool.poetry.dependencies]

Lists all project dependencies with their version constraints:

- `^` means "compatible with": `^3.12` means >=3.12.0, <4.0.0
- Direct version numbers like `0.1.0` specify exact versions
- `~=` means "approximately equal": allows patch-level changes

## Version Constraints

- `^3.12`: Compatible with 3.12.x
- `>=3.12`: 3.12 or higher
- `~=3.12`: Approximately equal to 3.12.x
- `3.12`: Exactly version 3.12

## Installing Dependencies

You can install dependencies using either of these methods:

### Using pip
```bash
pip install .
```

### Using Poetry (Recommended)
1. Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

Poetry is recommended as it provides better dependency resolution and virtual environment management.
