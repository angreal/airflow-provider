import os
import shutil
import subprocess

import angreal

cwd = os.path.realpath(os.path.join(angreal.get_root(), ".."))
docker_compose = os.path.join(cwd, "dev", "docker-compose.yaml")
logs = os.path.join(cwd, "dev", "logs")

demo = angreal.command_group(name="demo", about="commands for controlling the demo environment")


def _compose(*args):
    rc = subprocess.run(["docker", "compose", "-f", docker_compose, *args], cwd=cwd).returncode
    if rc != 0:
        raise SystemExit(rc)


@demo()
@angreal.command(name="start", about="start services for example dags")
def demo_start():
    _compose("build")
    _compose("up", "-d", "--wait")
    print("Airflow is up at http://localhost:8080 (user: airflow, password: airflow)")


@demo()
@angreal.command(name="stop", about="stop services for example dags")
def demo_stop():
    _compose("down")


@demo()
@angreal.command(name="clean", about="shut down services and remove files")
def demo_clean():
    _compose("down", "--volumes", "--remove-orphans", "--rmi", "local")
    shutil.rmtree(logs, ignore_errors=True)
