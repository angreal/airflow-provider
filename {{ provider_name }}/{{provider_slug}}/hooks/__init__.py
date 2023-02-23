import logging
import typing

from airflow.hooks.base import BaseHook

from {{provider_slug}}.hooks import *
from {{provider_slug}}.triggers import *



logger = logging.getLogger("airflow")




class {{ name | title | replace(from=" ", to="")}}Hook(BaseHook):
    
    default_conn_name = "{{ name | lower | replace(from=" ", to="_") }}_default"

    def __init__(self, **kwargs) -> None:
        
        super().__init__(**kwargs)
        
        # This is where you set all the attributes you need to for the operator to function
        raise NotImplementedError("You need to implement an __init__ method for this class")
    
