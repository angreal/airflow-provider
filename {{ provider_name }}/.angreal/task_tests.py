import angreal
from angreal.integrations.venv import venv_required

import os
import subprocess

venv_location = os.path.join(angreal.get_root(),'..','.venv')
cwd = os.path.join(angreal.get_root(), '..')

@venv_required(venv_location)
@angreal.command(name='run-tests', about="run our test suite. default is unit tests only")
@angreal.argument(name="integration", long="integration", short='i', takes_value=False, help="run integration tests only")
@angreal.argument(name="full", long="full", short='f', takes_value=False, help="run integration and unit tests")
@angreal.argument(name="open", long="open", short='o', takes_value=False, help="open results in web browser")
def run_tests(integration=False,full=False,open=False):
    
    if full:
        integration=False

    output_file = os.path.realpath(os.path.join(one_up,'htmlcov','index.html'))

    if integration: 
        subprocess.run('pytest -vvv --cov={{ provider_slug }} --cov-report html --cov-report term tests/integration',shell=True, cwd=one_up)
    if full:
        subprocess.run('pytest -vvv --cov={{ provider_slug }} --cov-report html --cov-report term tests/',shell=True, cwd=one_up)
    if not integration and not full:
        subprocess.run('pytest -vvv --cov={{ provider_slug }} --cov-report html --cov-report term tests/unit',shell=True, cwd=one_up)    
    if open:
        webbrowser.open_new('file://{}'.format(output_file))


@venv_required(venv_location)
@angreal.command(name='static-tests', about="run static analyses on our project")
@angreal.argument(name="open", long="open", short='o', takes_value=False, help="open results in web browser")
def static(open):
    subprocess.run(
        (
            "mypy {{ provider_slug }} --ignore-missing-imports --html-report typing_report"
        ),
        shell=True,
        cwd=cwd
    )

    if open:
        webbrowser.open(f'file:://{os.path.join(one_up,"typing_report","index.html")}')


@venv_required(venv_location)
@angreal.command(name='lint', about="lint our project")
def lint(open):
    subprocess.run(
        (
        "pre-commit run --all-files"
        ),
        shell=True,
        cwd=cwd
    )

    if open:
        webbrowser.open(f'file:://{os.path.join(one_up,"typing_report","index.html")}')




