{% set cls = name | title | replace(from=" ", to="") -%}
from __future__ import annotations

import asyncio
import typing

from airflow.triggers.base import BaseTrigger, TriggerEvent


def check_something() -> typing.Any:
    """A blocking check on the external service. Return a truthy value when
    the condition you wait for is met."""
    return True


class {{ cls }}Trigger(BaseTrigger):
    """Poll ``check_something`` every ``poll_interval`` seconds and fire a
    TriggerEvent when it returns a truthy value."""

    def __init__(self, poll_interval: float = 5.0) -> None:
        super().__init__()
        self.poll_interval = poll_interval

    def serialize(self) -> tuple[str, dict[str, typing.Any]]:
        return (
            "{{ provider_slug }}.triggers.{{ cls }}Trigger",
            {"poll_interval": self.poll_interval},
        )

    async def run(self) -> typing.AsyncIterator[TriggerEvent]:
        while True:
            # Run blocking code in a thread so the triggerer's event loop is not blocked.
            result = await asyncio.to_thread(check_something)
            if result:
                yield TriggerEvent({"status": "success", "result": result})
                return
            await asyncio.sleep(self.poll_interval)
