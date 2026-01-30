# src/createpy/cli.py (Typer: Modern 2026+ CLI - efficient annotations drive validation/completions/help; superior to Click: Native Python hints (not click.types), auto-Pydantic integration for complex models, less decorators/boilerplate, fastest dev UX with IDEs/typecheckers)
import typer
from typing import Optional
from typer import Option, Argument

app = typer.Typer()


@app.callback()
def callback():
    pass


@app.command()
def create(
    name: str = Argument(help="Name of a project to create OR project repo url"),
    repo: Optional[str] = Option(
        None, help="Project repo url (if not provided as name)"
    ),
    git_user: Optional[str] = Option(None, help="Git user name"),
    git_email: Optional[str] = Option(None, help="Git user email"),
):
    """Create project."""
    typer.echo(f"Creating project {name}...")
    if repo:
        typer.echo(f"with repo {repo}")


if __name__ == "__main__":
    app()
