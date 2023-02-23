import pytest
from {{provider_slug}}.operators import {{name | title | replace(from=" ", to="") }}Operator



def test_this_provider_operator_init():
    """this test will fail until you implement the operator"""
    operator = {{name | title | replace(from=" ", to="") }}Operator(task_id="test")
    assert isinstance(operator,{{name | title | replace(from=" ", to="") }}Operator)

