{% set cls = name | title | replace(from=" ", to="") -%}
{% set conn_type = name | lower | replace(from=" ", to="") -%}
from __future__ import annotations

import typing


def get_provider_info() -> dict[str, typing.Any]:
    """Return the provider metadata that Airflow reads through the
    ``apache_airflow_provider`` entry point.

    ``package-name``, ``name`` and ``description`` are required. The provider
    version is taken from the installed distribution, so it is not listed here.
    """
    return {
        "package-name": "{{ provider_name }}",
        "name": "{{ name }}",
        "description": "{{ short_description }}",
        "integrations": [
            {
                "integration-name": "{{ name }}",
                "tags": ["service"],
            }
        ],
        "hooks": [
            {
                "integration-name": "{{ name }}",
                "python-modules": ["{{ provider_slug }}.hooks"],
            }
        ],
        "operators": [
            {
                "integration-name": "{{ name }}",
                "python-modules": ["{{ provider_slug }}.operators"],
            }
        ],
        "sensors": [
            {
                "integration-name": "{{ name }}",
                "python-modules": ["{{ provider_slug }}.sensors"],
            }
        ],
        "triggers": [
            {
                "integration-name": "{{ name }}",
                "python-modules": ["{{ provider_slug }}.triggers"],
            }
        ],
        "connection-types": [
            {
                "connection-type": "{{ conn_type }}",
                "hook-class-name": "{{ provider_slug }}.hooks.{{ cls }}Hook",
                "hook-name": "{{ name }}",
                # Extra fields for the connection form. Each one is stored in the
                # connection's "extra" JSON. The schema is JSON Schema.
                "conn-fields": {
                    # "api_token": {
                    #     "label": "API token",
                    #     "schema": {"type": ["string", "null"], "format": "password"},
                    # },
                },
                # Hide, relabel or give placeholders to the standard fields.
                "ui-field-behaviour": {
                    "hidden-fields": [],
                    "relabeling": {},
                    "placeholders": {},
                },
            }
        ],
    }
