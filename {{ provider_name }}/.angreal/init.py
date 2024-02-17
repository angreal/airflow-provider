import subprocess




def init():
    subprocess.run(
        (
         "git config --global init.defaultBranch main;"
         "git init .;"
         "git add .;"
         "pip install uv;"
         "uv venv;"
         ". .venv/bin/activate;"
        "uv pip install -e .[dev];"
        "pre-commit install;"
        "pre-commit run --all-files;"
        "git commit -am '{{ provider_slug }} initialized via angreal';"
        ),
        shell=True,
        cwd = "{{ provider_name }}"
    )

    pass