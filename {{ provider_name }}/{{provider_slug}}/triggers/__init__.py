import logging
import typing

from airflow.triggers.base import BaseTrigger, TriggerEvent

from {{provider_slug}}.hooks import *



logger = logging.getLogger("airflow")




class {{name | title | spaceless ~ "Trigger"}}(BaseTrigger):

    def __init__(self) -> None:
        raise NotImplementedError("You need to implement an __init__ method for this class")
        pass


    def serialize(self) -> typing.Tuple[str,typing.Dict[str,typing.Any]]:

        raise NotImplementedError("You need to implement a serialize method for this class")
        return {
            "{{ provider_slug }}.triggers.{{name | title | spaceless ~ "Trigger"}}",
            {
            
            },
        }

    async def run(self):
        raise NotImplementedError("You need to implement a run method for this class")
        while True:
            rv = check_something()
            if rv :
                yield TriggerEvent(rv)
