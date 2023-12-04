from {{provider_slug}}.sensors import {{name | title | replace(from=" ", to="") }}Sensor


def test_operator_defers():
    operator = {{name | title | replace(from=" ", to="") }}Sensor(task_id="test")
    
    with pytest.raises(TaskDeferred):
        x = operator.execute(context={})



def test_operator_execute_complete():

    operator = {{name | title | replace(from=" ", to="") }}Sensor(task_id="test")
    
    event = {} 
    x = operator.execute(context={}, event=event)