__version__ = '0.1.0'
import typer
import sys
from py_utils.__create__ import __create__

app = typer.Typer()

@app.command()
def create(name: str):
    __create__(sys.executable, name)

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")

def main():
    app()

if __name__ == '__main__':
    main()
