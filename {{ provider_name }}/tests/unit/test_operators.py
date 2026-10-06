{% set cls = name | title | replace(from=" ", to="") -%}
from {{ provider_slug }}.operators import {{ cls }}Operator


def test_operator_execute():
    """the operator returns its message"""
    operator = {{ cls }}Operator(task_id="test", message="hello")
    assert operator.execute(context={}) == "hello"
