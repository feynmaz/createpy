# src/createpy/cli.py (Typer: Modern 2026+ CLI - efficient annotations drive validation/completions/help; superior to Click: Native Python hints (not click.types), auto-Pydantic integration for complex models, less decorators/boilerplate, fastest dev UX with IDEs/typecheckers)
import typer
from typing import Optional
from typer import Option
import subprocess
from .errors import ErrorReason
from .validators import (
    validate_name,
    validate_repo,
    validate_git_user,
    validate_git_email,
)


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
    try:
        if not (name or repo):
            raise ValueError(ErrorReason.NO_VALUES_PROVIDED)

        validate_name(name)
        validate_repo(repo)
        validate_git_user(git_user)
        validate_git_email(git_email)

        if not name:
            name = repo.split("/")[-1].split(".")[0]

        # Create project
        typer.echo(f"Creating project {name}...")
        result = subprocess.run(
            ["uv", "init", name],
            check=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise RuntimeError(f"Failed to create project: {result.stderr}")
        subprocess.run(["git", "init"], check=True)

        #  Set git user/email
        if git_user:
            subprocess.run(["git", "config", "user.name", git_user], check=True)

        if git_email:
            subprocess.run(["git", "config", "user.email", git_email], check=True)

        # Add remote
        if repo:
            typer.echo("Adding remote...")
            subprocess.run(["git", "remote", "add", "origin", repo], check=True)

        # Add tools
        result = subprocess.run(["uv", "add", "--dev", "ruff", "pytest"], check=True)
        if result.returncode != 0:
            raise RuntimeError(f"Failed to add tools: {result.stderr}")

    except ValueError as e:
        raise typer.BadParameter(str(e)) from e


if __name__ == "__main__":
    app()

    # subprocess.run(["git", "add", "."], check=True)
    # subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
    # subprocess.run(["git", "push", "-u", "origin", "master"], check=True)
