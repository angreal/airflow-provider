{% set cls = name | title | replace(from=" ", to="") -%}
from __future__ import annotations

import typing

from airflow.sdk import BaseSensorOperator

from {{ provider_slug }}.triggers import {{ cls }}Trigger

if typing.TYPE_CHECKING:
    from airflow.sdk import Context


class {{ cls }}Sensor(BaseSensorOperator):
    """A deferrable sensor: it hands the wait to {{ cls }}Trigger, which runs
    in the triggerer, and resumes in ``execute_complete`` when the trigger fires.

    :param poll_interval: seconds between checks in the trigger.
    """

    template_fields: typing.Sequence[str] = ()

    def __init__(self, *, poll_interval: float = 5.0, **kwargs: typing.Any) -> None:
        super().__init__(**kwargs)
        self.poll_interval = poll_interval

    def execute(self, context: Context) -> None:
        self.defer(
            trigger={{ cls }}Trigger(poll_interval=self.poll_interval),
            method_name="execute_complete",
        )

    def poke(self, context: Context) -> bool:
        # Used only if the sensor runs without deferring.
        return True

    def execute_complete(self, context: Context, event: dict[str, typing.Any] | None = None) -> typing.Any:
        return event
