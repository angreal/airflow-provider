






from __future__ import annotations
import logging
import typing

from airflow.hooks.base import BaseHook

logger = logging.getLogger("airflow")

class {{ name | title | replace(from=" ", to="")}}Hook(BaseHook):
    """
    Sample Hook that interacts with an HTTP endpoint the Python requests library.

    :param method: the API method to be called
    :type method: str
    :param sample_conn_id: connection that has the base API url i.e https://www.google.com/
        and optional authentication credentials. Default headers can also be specified in
        the Extra field in json format.
    :type sample_conn_id: str
    :param auth_type: The auth type for the service
    :type auth_type: AuthBase of python requests lib
    """

    conn_name_attr = "{{ name | lower | replace(from=" ", to="_") }}_conn_id"
    default_conn_name = "{{ name | lower | replace(from=" ", to="_") }}_default"
    conn_type = "{{ name | lower | replace(from=" ", to="")}}"
    hook_name = "{{ name | title | replace(from=" ", to="")}}"

 
    def __init__(
        self,
        {{ name | lower | replace(from=" ", to="_") }}_conn_id: str = default_conn_name,
    ) -> None:
        super().__init__()
        self.{{ name | lower | replace(from=" ", to="_") }}_conn_id = {{ name | lower | replace(from=" ", to="_") }}_conn_id


 
    @staticmethod
    def get_connection_form_widgets() -> dict[str, typing.Any]:
        """Returns connection widgets to add to connection form"""
        return {
            }

    @staticmethod
    def get_ui_field_behaviour() -> dict:
        """Returns custom field behaviour"""
        import json
        return {
            }


    def get_conn(self) -> typing.Any:
        """
        A method for getting a connection to an external service given your connection information.
        """        
        conn = self.get_connection(self.sample_conn_id)
        raise NotImplementedError
    


    def test_connection(self) -> typing.Tuple[bool, str]:
        """Test a connection"""

        raise NotImplementedError

        x = self.get_conn()
        alive = x.test_alive()
        if alive:
            return [True, "Alive"]
        return [False, "Not Alive"]