from contextlib import contextmanager
import logging
import pytest

import os
import shutil

import pytest

os.environ["AIRFLOW__DATABASE__LOAD_DEFAULT_CONNECTIONS"] = "False"
os.environ['AIRFLOW__CORE__UNIT_TEST_MODE'] = 'True'
os.environ['AIRFLOW__CORE__LOAD_EXAMPLES'] = 'False'
os.environ['AIRFLOW_HOME'] = os.path.join(os.path.dirname(__file__),'airflow')

@contextmanager
def suppress_logging(namespace):
    """
    Suppress logging within a specific namespace to keep tests "clean" during build
    """
    logger = logging.getLogger(namespace)
    old_value = logger.disabled
    logger.disabled = True
    try:
        yield
    finally:
        logger.disabled = old_value



@pytest.fixture(autouse=True,scope='session')
def initdb():
    """Create a database for every testing session and add connections to it."""

    from airflow.models import Connection
    from airflow.utils import db

    with suppress_logging("alembic.runtime.migration"):
        db.initdb(load_connections=False)

    # #Add Connections for Testing in here
    # db.merge_conn(
    #     Connection(
    #     )
    # )


    yield

    #clean up behind ourselves
    shutil.rmtree(os.environ["AIRFLOW_HOME"])


def pytest_itemcollected(item):
    """
    use test doc strings as messages for the testing suite
    """
    if item._obj.__doc__:
        item._nodeid = f"{item.obj.__doc__.strip().ljust(50,' ')[:50]}{str(item._nodeid).ljust(100,' ')[:50]}"
