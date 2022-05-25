import json
import typer
from subprocess import run as run_shell
import os

def __create__(exe, name, app_type, framework, git_init):
    run_shell('"'+exe+'" -m pip freeze', shell=True)
    os.mkdir(name)
    os.mkdir(os.path.join(name, ".app"))

    with open(os.path.join(name, ".app", "metadata.json"), "w") as f:
        f.write(json.dumps({
            "type":app_type,
            "framework":framework,
            "git_initialised":git_init
        }))
