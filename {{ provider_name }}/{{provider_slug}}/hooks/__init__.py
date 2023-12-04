






from __future__ import annotations
import logging
import typing

from airflow.hooks.base import BaseHook
from airflow.compat.functools import cached_property

logger = logging.getLogger("airflow")

class {{ name | title | replace(from=" ", to="")}}Hook(BaseHook):
    """
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
        """Add fields to the connection form of the UI. These connection attributes are put into the extras field."""
        from flask_appbuilder.fieldwidgets import BS3PasswordFieldWidget, BS3TextFieldWidget
        from flask_babel import lazy_gettext
        from wtforms import PasswordFIeld, StringField

        # object entries have the format
        # attribute_name : wtform.Field(lazy_gettext("Display Text"), widget=FieldWidget())

        return {
            }

    @staticmethod
    def get_ui_field_behaviour() -> dict:
        """Customize the behavior of the connection for of the UI."""
        
        return {
            "hidden_fields": [], # fields we want to hide
            "placeholders": { # fields we provide examples for
                    #field_name : example_value
                    },
            "relabeling" : {} # fields we want to relabel in the UI (ie schema become protocol) 
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
            return (True, "Alive")
        return (False, "Not Alive")
