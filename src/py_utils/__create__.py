import json
from subprocess import run as run_shell
import os

def __create__(exe: str, name: str, app_type: str, framework: str):
    run_shell('"'+exe+'" -m pip virtualenv', shell=True)
    os.mkdir(name)
    os.mkdir(os.path.join(name, ".app"))

    with open(os.path.join(name, ".app", "metadata.json"), "w") as f:
        f.write(json.dumps({
            "type":app_type,
            "framework":framework,
        }))
    
    with open(os.path.join(name, ".app", "scripts.json"), "w") as f:
        f.write(json.dumps({
            "dev": "",
            "prod": ""
        }))
