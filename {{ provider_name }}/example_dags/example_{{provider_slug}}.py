{% set cls = name | title | replace(from=" ", to="") -%}
"""An example DAG that uses the {{ name }} provider."""

from __future__ import annotations

import datetime

from airflow.sdk import dag

from {{ provider_slug }}.operators import {{ cls }}Operator
from {{ provider_slug }}.sensors import {{ cls }}Sensor


@dag(
    schedule=None,
    start_date=datetime.datetime(2024, 1, 1, tzinfo=datetime.timezone.utc),
    catchup=False,
    tags=["example", "{{ provider_slug }}"],
)
def example_{{ provider_slug }}():
    wait = {{ cls }}Sensor(task_id="wait", poll_interval=1.0)
    say_hello = {{ cls }}Operator(task_id="say_hello", message="run {% raw %}{{ run_id }}{% endraw %}")
    wait >> say_hello


example_dag = example_{{ provider_slug }}()
