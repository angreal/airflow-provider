from {{provider_slug}}.hooks import {{ name | title | replace(from=" ", to="")}}Hook


def test_hook_init():
    """test initialization"""

    hook = {{ name | title | replace(from=" ", to="")}}Hook()

    

