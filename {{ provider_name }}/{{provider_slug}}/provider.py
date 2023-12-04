import typing
import {{provider_slug}}


def get_provider_info() -> typing.Dict[str,typing.Any]:
    return {
        "package-name": "{{provider_name}}",  # Required
        "name": "{{name}}",  # Required
        "description": "{{short_description}}",  # Required
        "versions": {{provider_slug}}.__version__,  # Required
        "connection-types" : [
             {
                "connection-type": "{{ name | lower | replace(from=" ", to="")}}",
                "hook-class-name": "{{provider_slug}}.hooks.{{ name | title | replace(from=" ", to="")}}Hook"
            }
        ]
    }
