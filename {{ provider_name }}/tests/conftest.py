import os
import tempfile

# Configure Airflow before anything imports it. Unit tests do not need a
# metadata database: Airflow 3 task code does not talk to the database.
os.environ.setdefault("AIRFLOW_HOME", tempfile.mkdtemp(prefix="airflow-home-"))
os.environ["AIRFLOW__CORE__UNIT_TEST_MODE"] = "True"
os.environ["AIRFLOW__CORE__LOAD_EXAMPLES"] = "False"
os.environ["AIRFLOW__DATABASE__LOAD_DEFAULT_CONNECTIONS"] = "False"

# Give tests a connection through an environment variable, for example:
# os.environ["AIRFLOW_CONN_{{ name | upper | replace(from=" ", to="_") }}_DEFAULT"] = '{"conn_type": "{{ name | lower | replace(from=" ", to="") }}", "host": "localhost"}'


def pytest_itemcollected(item):
    """Use test docstrings as the test names in the report."""
    doc = getattr(getattr(item, "obj", None), "__doc__", None)
    if doc:
        item._nodeid = f"{doc.strip().ljust(50, ' ')[:50]}{str(item._nodeid).ljust(100, ' ')[:50]}"
