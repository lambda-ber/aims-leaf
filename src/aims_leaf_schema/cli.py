"""Command-line interface for aims-leaf."""

import typer


app = typer.Typer(
    name="aims-leaf",
    help="CLI for aims-leaf: multimodal structural biology data",
    no_args_is_help=True,
)


@app.command()
def version() -> None:
    """Show version information."""
    try:
        from importlib.metadata import version as get_version

        current_version = get_version("aims-leaf")
    except Exception:
        current_version = "unknown"

    typer.echo(f"aims-leaf {current_version}")


def main() -> None:
    """Entry point for the CLI."""
    app()


if __name__ == "__main__":
    main()
