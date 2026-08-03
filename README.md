# "Change" refactoring kata in Python

[![CI](https://github.com/Coding-Cuddles/change-refactoring-python-kata/actions/workflows/main.yml/badge.svg)](https://github.com/Coding-Cuddles/change-refactoring-python-kata/actions/workflows/main.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

This kata complements [Clean Code: Fundamentals, Ep. 2 - Names++](https://cleancoders.com/episode/clean-code-episode-2).

## Instructions

The goal of this kata is to refactor the `ChangeItForMe` class methods for better variable names,
structure, and readability. You cannot change the signatures of the class methods or tests.

Setup is complete when the existing test suite passes.

## Prerequisites

Required:

- [Git](https://git-scm.com/downloads)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

Optional:

- [GNU Make](https://www.gnu.org/software/make/), for shorter commands. Every required task also
  has a direct `uv` command.

You do not need to install Python or pytest separately. `uv` installs a compatible Python version
and the locked project dependencies when needed.

## Set up the kata

1. Clone the repository:

   ```console
   git clone https://github.com/Coding-Cuddles/change-refactoring-python-kata.git
   ```

2. Enter the repository directory:

   ```console
   cd change-refactoring-python-kata
   ```

3. Run the existing tests. Use Make when it is installed:

   ```console
   make test
   ```

   Otherwise, run pytest through `uv` directly:

   ```console
   uv run pytest
   ```

   The first run may install Python and the project dependencies. Setup is complete when pytest
   reports `2 passed`.

   If the command fails with `uv: command not found`, install
   [uv](https://docs.astral.sh/uv/getting-started/installation/) and repeat this step.

## Work on the kata

Refactor `change.py` without changing the public method signatures or the tests in
`test_change.py`.

Run the tests after each change. Use Make when it is installed:

```console
make test
```

Otherwise, run pytest through `uv` directly:

```console
uv run pytest
```

Continue when the test run passes.

## Make command reference

Make is optional. Run `make` or `make help` to list these commands in the terminal.

| Command             | Result                                  |
| ------------------- | --------------------------------------- |
| `make all`          | Run the test suite                      |
| `make help`         | Show the command reference              |
| `make test`         | Run the test suite                      |
| `make format`       | Format tracked Python files             |
| `make format-check` | Check formatting without changing files |
| `make clean`        | Remove generated caches                 |
