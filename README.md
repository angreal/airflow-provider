# Airflow Provider Template

An angreal template for the creation and distribution of Airflow providers.

It targets **Airflow 3** (default `airflow_version` 3.3.2). Rendered projects
need Airflow 3.2 or later and Python 3.10 or later. For Airflow 2, use a commit
of this template from before the Airflow 3 move.

## Usage

```
pip install angreal
angreal init https://github.com/angreal/airflow-provider.git
```

`angreal init` creates a `.venv` with uv (Python 3.12, installed against the
Airflow constraints file) and a git repository.

## What you get

- `pyproject.toml` with the `apache_airflow_provider` entry point, so Airflow
  finds the package as a provider (`airflow providers list`).
- A hook, an operator, a deferrable sensor and a trigger built on the Airflow 3
  base classes (`airflow.sdk.BaseHook`, `airflow.sdk.BaseOperator`,
  `airflow.sdk.BaseSensorOperator`, `airflow.triggers.base.BaseTrigger`).
- `get_provider_info()` with the connection type declared through
  `conn-fields` / `ui-field-behaviour`.
- An example DAG and unit tests.
- A Docker Compose demo stack (`dev/`): Postgres, API server, scheduler,
  DAG processor and triggerer, with the LocalExecutor.

## Template Usage

```
demo    commands for controlling the demo environment
        start | stop | clean
dev     commands for your development environment
        setup
test    commands for executing tests
        run [--integration] [--full] [--open] | static | lint
```

`angreal demo start` serves Airflow at http://localhost:8080 (user `airflow`,
password `airflow`).
