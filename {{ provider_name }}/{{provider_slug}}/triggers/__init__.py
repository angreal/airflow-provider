import logging
import typing

from airflow.triggers.base import BaseTrigger, TriggerEvent
from asgiref.sync import sync_to_async

from {{provider_slug}}.hooks import *



logger = logging.getLogger("airflow")


def check_something():
    """A method that checks on something"""
    return

class {{name | title | replace(from=" ", to="")}}Trigger(BaseTrigger):

    def __init__(self) -> None:
        raise NotImplementedError("You need to implement an __init__ method for this class")
        pass


    def serialize(self) -> typing.Tuple[str,typing.Dict[str,typing.Any]]:

        raise NotImplementedError("You need to implement a serialize method for this class")
        return {
            "{{ provider_slug }}.triggers.{{name | title | replace(from=" ", to="")}}Trigger",
            {
            
            },
        }

    async def run(self):
        raise NotImplementedError("You need to implement a run method for this class")
        while True:
            check_something_call = sync_to_async(check_something)
            rv = await check_something_call()
            if rv :
                yield TriggerEvent(rv)
