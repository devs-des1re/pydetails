"""Libraries"""
import typer
import requests

from .utils import error_message, get_info

app = typer.Typer(no_args_is_help=True)

@app.command()
def details(
    package: str,
    testpypi : bool = typer.Option(
        False,
        "--testpypi", "--test", "-t",
        help="Gets the info from test pypi"
    )
):
    """Gets the details of a python package

    Args:
        package (str): The name of the package you want to get the details of
        testpypi (bool, optional): If the package you want to get the details of is from TestPyPI. Defaults to typer.Option(False, "--testpypi", "--test", "-t", help="Gets the info from test pypi").
    """
    request = requests.get(
        f"https://{'test.pypi' if testpypi else 'pypi'}.org/pypi/{package}/json",
        timeout=10
    )

    if request.status_code != 200:
        error_message("The package you have provided is invalid.")
    else:
        data = request.json()
        print(get_info(data))

@app.command()
def json(
    package: str,
    testpypi : bool = typer.Option(
        False,
        "--testpypi", "--test", "-t",
        help="Gets the info from test pypi"
    )
):
    """Gets the json of a python package

    Args:
        package (str): The name of the package you want to get the json of
        testpypi (bool, optional): If the package you want to get the json of is from TestPyPI. Defaults to typer.Option(False, "--testpypi", "--test", "-t", help="Gets the info from test pypi").
    """
    request = requests.get(
        f"https://{'test.pypi' if testpypi else 'pypi'}.org/pypi/{package}/json",
        timeout=10
    )

    if request.status_code != 200:
        error_message("The package you have provided is invalid.")
    else:
        data = request.json()
        print(data)

if __name__ == "__main__":
    app()
