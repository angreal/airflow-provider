# Airflow Provider Template

An angreal template for the creation and distribution of Airflow providers.

## Usage 

```
pip install angreal
angreal init https://github.com/angreal/airflow-provider.git
```

## Template Usage

```
angreal 2.0.3

USAGE:
    angreal [OPTIONS] <SUBCOMMAND>

OPTIONS:
    -h, --help       Print help information
    -v, --verbose    verbose level, (may be used multiple times for more verbosity)
    -V, --version    Print version information

SUBCOMMANDS:
    demo-clean      shut down services and remove files
    demo-start      start services for example dags
    demo-stop       stop services for example dags
    dev-setup       setup a development environment
    help            Print this message or the help of the given subcommand(s)
    init            Initialize an Angreal template from source.
    lint            lint our project
    run-tests       run our test suite. default is unit tests only
    static-tests    run static analyses on our project

```
