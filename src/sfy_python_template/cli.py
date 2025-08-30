import typer

from sfy_python_template import package_a, package_b

cli = typer.Typer(no_args_is_help=True)

cli.add_typer(package_a.app, name="package-a")
cli.add_typer(package_b.app, name="package-b")


def main():
    cli()
