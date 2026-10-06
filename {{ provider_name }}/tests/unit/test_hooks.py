{% set cls = name | title | replace(from=" ", to="") -%}
from {{ provider_slug }}.hooks import {{ cls }}Hook


def test_hook_init():
    """the hook uses the default connection id"""
    hook = {{ cls }}Hook()
    assert hook.{{ name | lower | replace(from=" ", to="_") }}_conn_id == {{ cls }}Hook.default_conn_name
    assert {{ cls }}Hook.conn_type == "{{ name | lower | replace(from=" ", to="") }}"
