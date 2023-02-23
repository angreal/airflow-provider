import pytest
from {{provider_slug}}.triggers import {{name | title | replace(from=" ", to="") }}Trigger



def test_this_provider_trigger_init():
    """this test will fail until you implement the trigger"""
    trigger = {{name | title | replace(from=" ", to="") }}Trigger()
    assert isinstance(trigger,{{name | title | replace(from=" ", to="") }}Trigger)

