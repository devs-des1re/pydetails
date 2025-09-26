"""Libraries"""
import click
from rich.console import Console

console = Console()

def error_message(message: str):
    """Creates a error message

    Args:
        message (str): The error message

    Raises:
        click.UsageError: Raises the error
    """
    raise click.UsageError(f"Error: {message}")

def get_info(data: dict):
    """Gets the info of a python package

    Args:
        data (dict): The json of the python package

    Returns:
        string: A formatted description of the python package
    """
    text = []
    info = data["info"]

    text.append(f"Package: {info['name']} ({info['version']})")
    text.append(f"Summary: {info['summary']}")
    text.append(f"PyPI URL: {info['package_url']}")
    text.append(f"License: {info.get('license_expression', 'N/A')}")
    text.append(f"Author(s): {info['author_email']}")
    text.append(f"Maintainer: {info.get('maintainer_email', 'N/A')}")
    text.append(f"Requires Python: {info['requires_python']}")
    text.append(f"Dependencies: {', '.join(info.get('requires_dist', [])) or 'None'}")

    text.append("\nClassifiers:")
    for classifier in info["classifiers"]:
        text.append(f"  - {classifier}")

    latest_version = info["version"]
    release_files = data["releases"].get(latest_version, [])
    text.append(f"\nFiles for version {latest_version}:")
    for f in release_files:
        text.append(f"  - {f['filename']} ({f['packagetype']}, {f['size']} bytes)")
        text.append(f"    URL: {f['url']}")

    return "\n".join(text)
