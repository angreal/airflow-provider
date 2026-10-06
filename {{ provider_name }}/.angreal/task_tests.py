import os
import subprocess
import webbrowser

import angreal

cwd = os.path.realpath(os.path.join(angreal.get_root(), ".."))
venv_location = os.path.join(cwd, ".venv")
venv_python = os.path.join(venv_location, "bin", "python")

tests = angreal.command_group(name="test", about="commands for executing tests")


def _require_venv():
    if not os.path.exists(venv_python):
        print("No virtual environment found. Run `angreal dev setup` first.")
        raise SystemExit(1)


def _run(cmd):
    rc = subprocess.run(cmd, shell=True, cwd=cwd).returncode
    if rc != 0:
        raise SystemExit(rc)


@tests()
@angreal.command(name="run", about="run our test suite. default is unit tests only")
@angreal.argument(name="integration", long="integration", short="i", takes_value=False, help="run integration tests only")
@angreal.argument(name="full", long="full", short="f", takes_value=False, help="run integration and unit tests")
@angreal.argument(name="open", long="open", short="o", takes_value=False, help="open results in web browser")
def run_tests(integration=False, full=False, open=False):
    _require_venv()

    if full:
        target = "tests/"
    elif integration:
        target = "tests/integration"
    else:
        target = "tests/unit"

    try:
        _run(
            f"{venv_python} -m pytest -vvv --cov={{ provider_slug }} "
            f"--cov-report html --cov-report term {target}"
        )
    finally:
        if open:
            webbrowser.open_new("file://{}".format(os.path.join(cwd, "htmlcov", "index.html")))


@tests()
@angreal.command(name="static", about="run static analyses on our project")
def static():
    _require_venv()
    _run(f"{venv_python} -m mypy {{ provider_slug }} --ignore-missing-imports")


@tests()
@angreal.command(name="lint", about="lint our project")
def lint():
    _require_venv()
    _run(f"{venv_location}/bin/pre-commit run --all-files")
