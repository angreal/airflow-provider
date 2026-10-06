import os
import shutil
import subprocess


def init():
    # angreal runs this from the rendered project's .angreal directory.
    project_root = os.path.abspath(os.path.join(os.getcwd(), ".."))
    os.chdir(project_root)

    # Create the development environment (the same steps as `angreal dev setup`,
    # without pre-commit). A failure here does not fail the render.
    uv = shutil.which("uv")
    if uv:
        venv_python = os.path.join(project_root, ".venv", "bin", "python")
        constraints = (
            "https://raw.githubusercontent.com/apache/airflow/"
            "constraints-{{ airflow_version }}/constraints-3.12.txt"
        )
        rc = subprocess.run([uv, "venv", "--python", "3.12", ".venv"]).returncode
        if rc == 0:
            rc = subprocess.run(
                [uv, "pip", "install", "--python", venv_python, "-e", ".[dev]", "--constraint", constraints]
            ).returncode
        if rc != 0:
            print("Could not set up the virtual environment. Run `angreal dev setup` later.")
    else:
        print("uv was not found. Install uv, then run `angreal dev setup`.")

    if shutil.which("git"):
        subprocess.run(["git", "init", "-q"])
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-q", "-m", "{{ provider_name }} initialized via angreal"])
