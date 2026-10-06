{% set cls = name | title | replace(from=" ", to="") -%}
{% set conn_base = name | lower | replace(from=" ", to="_") -%}
{% set conn_id = conn_base ~ "_conn_id" -%}
from __future__ import annotations

import typing

from airflow.sdk import BaseHook


class {{ cls }}Hook(BaseHook):
    """Interact with {{ name }}.

    The connection form for this hook (extra fields, hidden fields, labels) is
    declared in ``{{ provider_slug }}.provider.get_provider_info`` under
    ``connection-types``.
    """

    conn_name_attr = "{{ conn_id }}"
    default_conn_name = "{{ name | lower | replace(from=" ", to="_") }}_default"
    conn_type = "{{ name | lower | replace(from=" ", to="") }}"
    hook_name = "{{ name }}"

    def __init__(self, {{ conn_id }}: str = default_conn_name, **kwargs: typing.Any) -> None:
        super().__init__(**kwargs)
        self.{{ conn_id }} = {{ conn_id }}

    def get_conn(self) -> typing.Any:
        """Return a client for the external service, built from the connection."""
        conn = self.get_connection(self.{{ conn_id }})
        # Build and return your client from conn.host, conn.login, conn.password,
        # conn.extra_dejson, ...
        return conn

    def test_connection(self) -> tuple[bool, str]:
        """Test the connection (used by the "Test" button in the UI)."""
        return False, "test_connection is not implemented for {{ cls }}Hook"
