import logging
import typing


from airflow.models import BaseOperator

from {{provider_slug}}.hooks import *
from {{provider_slug}}.triggers import *



logger = logging.getLogger("airflow")




class {{name | title | spaceless ~ "Operator"}}(BaseOperator):
    """
    {{name | title | spaceless ~ "Operator"}}
    """
    template_fields = ()

    def __init__(self, **kwargs) -> None:
        
        super().__init__(**kwargs)
        
        # This is where you set all the attributes you need to for the operator to function
        raise NotImplementedError("You need to implement an __init__ method for this class")
    

    def execute(self,context) -> Any:

        # This is where you write the python code that gets executed on a schedule
        raise NotImplementedError("You need to implement an execute method for this class")

