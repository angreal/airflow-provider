ARG IMAGE_NAME="apache/airflow:{{airflow_version}}}"
FROM ${IMAGE_NAME}

USER airflow
COPY --chown=airflow:airflow . ${AIRFLOW_HOME}/{{ provider_name }}
COPY --chown=airflow:airflow example_dags/ /opt/airflow/dags
RUN pip install --no-cache-dir --user ${AIRFLOW_HOME}/{{provider_name}}/.
