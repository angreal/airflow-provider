ARG IMAGE_NAME="apache/airflow:{{airflow_version}}}"
FROM ${IMAGE_NAME}

ENV VIRTUAL_ENV=/usr/local
ADD --chmod=655 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

USER airflow
COPY --chown=airflow:airflow . ${AIRFLOW_HOME}/{{ provider_name }}
COPY --chown=airflow:airflow example_dags/ /opt/airflow/dags

RUN /root/.cargo/bin/uv pip install --no-cache -e {{provider_name}}@${AIRFLOW_HOME}/{{provider_name}}/.
