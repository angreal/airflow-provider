
__version__ = "0.0.0a"

def get_provider_info():
    return {
        "package-name": "airflow-provider-{{provider-name}}",  # Required
        "name": "{{provider-name}}",  # Required
        "description": "{{short_description}}",  # Required
        "versions": [__version__],  # Required
    }