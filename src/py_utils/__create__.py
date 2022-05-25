import typer
from subprocess import run as run_shell
import os

def __create__(exe, name):
    run_shell('"'+exe+'" -m pip freeze', shell=True)
    if os.path.exists(name):
        typer.echo("Already exists")
        raise typer.Exit()
    else:
        os.mkdir(name)