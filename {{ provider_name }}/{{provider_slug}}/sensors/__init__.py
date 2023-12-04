import typing
from airflow.models import BaseOperator

from {{project_slug}}.triggers import {{name | title | replace(from=" ", to="")}}Trigger


class {{name | title | replace(from=" ", to="")}}Sensor(BaseOperator):

    template_fields = ()

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        raise NotImplementedError("You need to implement an __init__ method for this class")

    def execute(self,context) -> typing.Any:

        self.defer(
            trigger = {{name | title | replace(from=" ", to="")}}Trigger(),
            method_name="execute_complete"
        )

    def execute_complete(self,context,event=None):
        return event


