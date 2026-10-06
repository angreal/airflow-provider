{% set cls = name | title | replace(from=" ", to="") -%}
import pytest
from airflow.sdk.exceptions import TaskDeferred

from {{ provider_slug }}.sensors import {{ cls }}Sensor
from {{ provider_slug }}.triggers import {{ cls }}Trigger


def test_sensor_defers():
    """the sensor defers to its trigger"""
    sensor = {{ cls }}Sensor(task_id="test", poll_interval=2.0)

    with pytest.raises(TaskDeferred) as deferred:
        sensor.execute(context={})

    assert isinstance(deferred.value.trigger, {{ cls }}Trigger)
    assert deferred.value.method_name == "execute_complete"


def test_sensor_execute_complete():
    """the sensor returns the trigger event"""
    sensor = {{ cls }}Sensor(task_id="test")
    event = {"status": "success"}
    assert sensor.execute_complete(context={}, event=event) == event
