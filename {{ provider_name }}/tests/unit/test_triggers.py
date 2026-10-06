{% set cls = name | title | replace(from=" ", to="") -%}
import asyncio

import pytest
from airflow.triggers.base import TriggerEvent

import {{ provider_slug }}.triggers
from {{ provider_slug }}.triggers import {{ cls }}Trigger


def test_trigger_serialize():
    """the trigger serializes its class path and arguments"""
    trigger = {{ cls }}Trigger(poll_interval=3.0)
    classpath, kwargs = trigger.serialize()
    assert classpath == "{{ provider_slug }}.triggers.{{ cls }}Trigger"
    assert kwargs == {"poll_interval": 3.0}


@pytest.mark.asyncio
async def test_trigger_fires(monkeypatch):
    """the trigger fires when the check succeeds"""
    monkeypatch.setattr({{ provider_slug }}.triggers, "check_something", lambda: "done")
    trigger = {{ cls }}Trigger(poll_interval=0.01)

    event = await asyncio.wait_for(trigger.run().__anext__(), timeout=5)

    assert event == TriggerEvent({"status": "success", "result": "done"})


@pytest.mark.asyncio
async def test_trigger_waits(monkeypatch):
    """the trigger keeps waiting while the check fails"""
    monkeypatch.setattr({{ provider_slug }}.triggers, "check_something", lambda: None)
    trigger = {{ cls }}Trigger(poll_interval=0.01)

    task = asyncio.create_task(trigger.run().__anext__())
    await asyncio.sleep(0.2)
    assert task.done() is False
    task.cancel()
