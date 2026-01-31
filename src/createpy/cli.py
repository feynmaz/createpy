# src/createpy/cli.py (Typer: Modern 2026+ CLI - efficient annotations drive validation/completions/help; superior to Click: Native Python hints (not click.types), auto-Pydantic integration for complex models, less decorators/boilerplate, fastest dev UX with IDEs/typecheckers)
import typer
from typing import Optional
from typer import Option
from tools import validate_name
from errors import ErrorReason

app = typer.Typer()


@app.callback()
def callback():
    pass


@app.command()
def create(
    name: Optional[str] = Option(
        None, "-n", "--name", help="Name of a project to create"
    ),
    repo: Optional[str] = Option(None, "-r", "--repo", help="Project repo url"),
    git_user: Optional[str] = Option(None, "-u", "--user", help="Git user name"),
    git_email: Optional[str] = Option(None, "-e", "--email", help="Git user email"),
):
    if not name and not repo:
        raise typer.BadParameter(ErrorReason.NO_VALUES_PROVIDED.value)

    if name:
        validate_name(name)


if __name__ == "__main__":
    app()
