ARG IMAGE_NAME="apache/airflow:{{airflow-version}}"
FROM ${IMAGE_NAME}

USER root
COPY airflow_provider_{{provider-slug}} ${AIRFLOW_HOME}/airflow_provider_{{provider-slug}}
COPY setup.cfg ${AIRFLOW_HOME}/airflow_provider_{{provider-slug}}/setup.cfg
COPY setup.py ${AIRFLOW_HOME}/airflow_provider_{{provider-slug}}/setup.py

RUN pip install -e ${AIRFLOW_HOME}/airflow_provider_{{provider-slug}}[dev]
USER astro