import importlib.util
import pathlib

EXAMPLE_DAGS = pathlib.Path(__file__).parents[2] / "example_dags"


def test_example_dags_load():
    """every example DAG file imports and defines a DAG"""
    from airflow.sdk import DAG

    files = sorted(EXAMPLE_DAGS.glob("*.py"))
    assert files, f"no example DAGs found in {EXAMPLE_DAGS}"
    for path in files:
        spec = importlib.util.spec_from_file_location(path.stem, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        dags = [obj for obj in vars(module).values() if isinstance(obj, DAG)]
        assert dags, f"{path.name} defines no DAG"
        for dag in dags:
            assert dag.task_ids
