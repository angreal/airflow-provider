import pytest
from {{provider_slug}}.sensors import {{name | title | replace(from=" ", to="") }}Sensor



def test_this_provider_sensor_init():
    """this test will fail until you implement the sensor"""
    sensor = {{name | title | replace(from=" ", to="") }}Sensor(task_id="test")
    assert isinstance(sensor,{{name | title | replace(from=" ", to="") }}Sensor)

