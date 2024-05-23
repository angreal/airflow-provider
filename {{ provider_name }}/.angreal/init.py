import angreal
from angreal.integrations.git import Git
from angreal.integrations.venv import VirtualEnv

import subprocess
import os




def init():
    os.chdir("{{provider_name}}")
    
    try:
     VirtualEnv(".venv", now=True, requirements=".[dev]").install_requirements()
        g = Git()
        g.init()
        g.add('.')
    
        subprocess.run(
            (
            "pre-commit install;"
            "pre-commit run --all-files;"
            "pre-commit run --all-files;" 
            ),
            shell=True,
        )
    
        g.commit("-am '{{ provider_name }} initialized via angreal'")
    except :
        pass
        
    pass
