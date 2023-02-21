ARG IMAGE_NAME="apache/airflow:{{airflow_version}}"
FROM ${IMAGE_NAME}

USER root
COPY {{provider_slug}} ${AIRFLOW_HOME}/{{provider_slug}}
COPY setup.cfg ${AIRFLOW_HOME}/{{provider_slug}}/setup.cfg
COPY setup.py ${AIRFLOW_HOME}/{{provider_slug}}/setup.py

RUN pip install -e ${AIRFLOW_HOME}/{{provider_slug}}[dev]
USER astro