import os
import shutil
import subprocess

import angreal

cwd = os.path.realpath(os.path.join(angreal.get_root(), ".."))
venv_location = os.path.join(cwd, ".venv")
venv_python = os.path.join(venv_location, "bin", "python")
python_version = "3.12"
constraints = (
    "https://raw.githubusercontent.com/apache/airflow/"
    f"constraints-{{ airflow_version }}/constraints-{python_version}.txt"
)

dev = angreal.command_group(name="dev", about="commands for your development environment")


@dev()
@angreal.command(name="setup", about="setup a development environment")
def setup_env():
    uv = shutil.which("uv")
    if uv is None:
        print("uv is required: https://docs.astral.sh/uv/")
        raise SystemExit(1)

    if not os.path.exists(venv_python):
        subprocess.run([uv, "venv", "--python", python_version, venv_location], check=True, cwd=cwd)

    # Install the provider with Airflow's constraints file, as Airflow recommends.
    rc = subprocess.run(
        [uv, "pip", "install", "--python", venv_python, "-e", ".[dev]", "--constraint", constraints],
        cwd=cwd,
    ).returncode
    if rc != 0:
        raise SystemExit(rc)

    subprocess.run(
        f"{venv_location}/bin/pre-commit install && {venv_location}/bin/pre-commit run --all-files",
        shell=True,
        cwd=cwd,
    )
