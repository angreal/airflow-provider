# {{ name }}

{{ short_description }}

An Apache Airflow provider package for Airflow 3 (`apache-airflow>=3.2`).

## Development

```
angreal dev setup      # create .venv and install the package with the dev extras
angreal test run       # unit tests
angreal demo start     # Airflow on http://localhost:8080 (airflow / airflow) with example_dags/
angreal demo clean     # stop the demo and remove its volumes and image
```

Check that Airflow finds the provider:

```
airflow providers list
```
