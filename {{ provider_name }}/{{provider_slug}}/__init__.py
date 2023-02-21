
__version__ = "0.0.0a"

def get_provider_info():
    return {
        "package-name": "{{provider_name}}",  # Required
        "name": "{{provider_name}}",  # Required
        "description": "{{short_description}}",  # Required
        "versions": [__version__],  # Required
    }