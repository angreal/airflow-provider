ARG IMAGE_NAME="apache/airflow:{{ airflow_version }}"
FROM ${IMAGE_NAME}

USER airflow
COPY --chown=airflow:0 . /opt/airflow/{{ provider_name }}
# Pin apache-airflow to the image's version so that installing the provider
# cannot upgrade or downgrade Airflow.
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" /opt/airflow/{{ provider_name }}
