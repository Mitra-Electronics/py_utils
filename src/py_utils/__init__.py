__version__ = '0.1.0'
import typer
import sys
from os import path
from py_utils.__create__ import __create__

app = typer.Typer()

@app.command()
def create():
    name = typer.prompt(text="Enter the name of the project")
    if path.exists(name):
        typer.echo(f"A folder named {name} already exists.")
        raise typer.Abort()
    
    app_type : str = typer.prompt(text="Enter the app type (web, app, game)")
    app_type = app_type.lower()
    if app_type != "web" and app_type != "app" and app_type != "game":
        typer.echo("Incorrect app type")
        raise typer.Abort()

    framework = typer.prompt(text="Enter the framework which you want to use")

    __create__(sys.executable, name, app_type, framework)

@app.command()
def run(script: str):
    script

def main():
    app()
