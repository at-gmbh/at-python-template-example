import logging

import typer

from example_project import __title__
from example_project import __version__
from example_project import util

logger = logging.getLogger('example_project')


app = typer.Typer(
    name='example_project',
    help="A small example project created with the at-python-template.")


def version_callback(version: bool):
    if version:
        typer.echo(f"{__title__} {__version__}")
        raise typer.Exit()


ConfigOption = typer.Option(
    ..., '-c', '--config', metavar='PATH', help="path to the program configuration")
VersionOption = typer.Option(
    None, '-v', '--version', callback=version_callback, is_eager=True,
    help="print the program version and exit")


@app.command()
def main(config_file: str = ConfigOption, version: bool = VersionOption):
    """
    This is the entry point of your command line application. The values of the CLI params that
    are passed to this application will show up als parameters to this function.

    This docstring is where you describe what your command line application does.
    Try running `python -m example_project --help` to see how this shows up in the command line.
    """
    config = util.load_config(config_file)
    util.logging_setup(config)
    logger.info("Looks like you're all set up. Let's get going!")
    # TODO your journey starts here


if __name__ == "__main__":
    app()
