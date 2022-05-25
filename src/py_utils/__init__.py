__version__ = '0.1.0'
import typer
import sys
from py_utils.__create__ import __create__

app = typer.Typer()

@app.command()
def create(
    name: str = typer.Option(..., prompt="Enter the nae of the project"),
    app_type : str = typer.Option(..., prompt="Enter the app type (web, app, game)")
    ):
    __create__(sys.executable)

@app.command()
def run(script: str):
    script

def main():
    app()
