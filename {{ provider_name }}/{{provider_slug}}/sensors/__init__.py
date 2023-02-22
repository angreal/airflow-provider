from airflow.sensors.base import BaseSensorOperator, PokeReturnValue


class {{name | title | spaceless ~ "Sensor"}}(BaseSensorOperator):

    template_fields

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        raise NotImplementedError("You need to implement an __init__ method for this class")

    def poke(self, context) -> PokeReturnValue | bool:

        raise NotImplementedError("You need to implement a poke method for this class")
        return_value = method_for_checking_state()
        return PokeReturnValue(bool(return_value))