ARG IMAGE_NAME="apache/airflow:{{airflow_version}}"
FROM ${IMAGE_NAME}

USER airflow
COPY --chown=airflow:airflow . ${AIRFLOW_HOME}/{{provider_slug}}

RUN chown airflow ${AIRFLOW_HOME}/logs
RUN pip install --upgrade pip
RUN pip install -e ${AIRFLOW_HOME}/{{provider_slug}}/[dev]
