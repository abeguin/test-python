# Python nix template

Python project template to start developing without the boilerplate work

### Dependencies

We use [uv](https://docs.astral.sh/uv/) as a decent python package manager,
and [xc](https://xcfile.dev/) to execute the scripts defined in this file. If
you use [nix](https://nixos.org), you can also easily use the tools defined in
the flake.nix.

### Build system

We use [hatchling](https://pypi.org/project/hatchling/) as a build backend, ran
via the `uv build` command.

### Python good practices

- [`__init__` files](https://www.reddit.com/r/learnpython/comments/lgbxry/what_do_you_have_in_your_init_py_files/)
- [`__main__` file](https://docs.python.org/3/library/__main__.html#main-py-in-python-packages)
- [packaging.python.org tool recommendations](https://packaging.python.org/en/latest/guides/tool-recommendations/#)

## Tasks

### py-sync

Installs the required dependencies.

```
uv sync
```

### py-lint

Runs the typechecker, linter and checks formatting. This is the lint target in the CI.

```
uv run ruff check -q
uv run ruff format --check -q
uv run basedpyright
```

### py-lint-fix

Runs linter and formatter to fix issues. Then runs the typechecker.

```
uv run ruff check --fix
uv run ruff format
uv run basedpyright
```

### py-test

Runs the unit tests. This is the test target in the CI.

```
uv run pytest --cov=sfy_python_template
```

### nix-fmt

```bash
nix fmt .
```

### nix-flake-check

```bash
nix flake check --all-systems
```

### cog-check

```bash
cog check --from-latest-tag
```

### cog-check-full

```bash
cog check
```
