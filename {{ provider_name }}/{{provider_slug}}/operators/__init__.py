{% set cls = name | title | replace(from=" ", to="") -%}
{% set conn_base = name | lower | replace(from=" ", to="_") -%}
{% set conn_id = conn_base ~ "_conn_id" -%}
from __future__ import annotations

import typing
from collections.abc import Sequence

from airflow.sdk import BaseOperator

from {{ provider_slug }}.hooks import {{ cls }}Hook

if typing.TYPE_CHECKING:
    from airflow.sdk import Context


class {{ cls }}Operator(BaseOperator):
    """A starting point for an operator that works with {{ name }}.

    :param message: a templated message that the operator logs and returns.
    :param {{ conn_id }}: the Airflow connection to use.
    """

    template_fields: Sequence[str] = ("message",)

    def __init__(
        self,
        *,
        message: str = "Hello from {{ name }}",
        {{ conn_id }}: str = {{ cls }}Hook.default_conn_name,
        **kwargs: typing.Any,
    ) -> None:
        super().__init__(**kwargs)
        self.message = message
        self.{{ conn_id }} = {{ conn_id }}

    def execute(self, context: Context) -> typing.Any:
        # Replace this with the work the operator does, for example:
        #   hook = {{ cls }}Hook({{ conn_id }}=self.{{ conn_id }})
        #   client = hook.get_conn()
        self.log.info("%s", self.message)
        return self.message
