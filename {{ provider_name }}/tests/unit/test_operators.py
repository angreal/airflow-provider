from {{provider_slug}}.operators import {{name | title | replace(from=" ", to="") }}Operator


def test_operator():
    operator = {{name | title | replace(from=" ", to="") }}Operator(task_id="test")
    x = operator.execute(context={})



