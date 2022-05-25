__version__ = '0.1.0'
import typer
import sys
from py_utils.__create__ import __create__

app = typer.Typer()

@app.command()
def create(name: str):
    __create__(sys.executable, name)

@app.command()
def run(script: str):
    script

def main():
    app()
