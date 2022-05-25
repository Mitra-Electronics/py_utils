import json
import typer
from subprocess import run as run_shell
import os

def __create__(exe):
    run_shell('"'+exe+'" -m pip freeze', shell=True)
    name: str = typer.Option(prompt="Enter the name of the project")
    if os.path.exists(name):
        typer.echo(f"A folder with {name} already exists. Please")
        raise typer.Abort()
    else:
        os.mkdir(name)
        os.mkdir(os.path.join(name, ".app"))
    
    

    with open(os.path.join(name, ".app", "metadata.json"), "w") as f:
        f.write(json.dumps({
            "type":app_type,
            "framework":framework,
            "git_initialised":git_init
        }))
