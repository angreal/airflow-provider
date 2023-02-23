import pytest
from {{provider_slug}}.hooks import {{ name | title | replace(from=" ", to="")}}Hook



def test_this_provider_hook_init():
    """this test will fail until you implement the hook"""
    
    hook = {{ name | title | replace(from=" ", to="")}}Hook()
    assert isinstance(hook,{{ name | title | replace(from=" ", to="")}}Hook)