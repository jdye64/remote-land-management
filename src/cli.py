import click


@click.command()
@click.option("--client_host", default="localhost", help="DNS name or URL for the endpoint.")
@click.option("--client_port", default=6397, type=int, help="Port for the client endpoint.")
@click.option("--client_kwargs", help="Additional arguments to pass to the client.", default="{}")
@click.option("--dry_run", is_flag=True, help="Perform a dry run without executing actions.")
@click.option(
    "--log_level",
    type=click.Choice([level.value for level in LogLevel], case_sensitive=False),
    default="INFO",
    show_default=True,
    help="Log level.",
)
@click.option("--version", is_flag=True, help="Show version.")
@click.pass_context
def main(
    ctx,
    client_host: str,
    client_kwargs: str,
    client_port: int,
    dry_run: bool,
    log_level: str,
    version: [bool], # type: ignore
):
    if version:
        click.echo(f"nv-ingest     : {NV_INGEST_VERSION}")
        click.echo(f"nv-ingest-cli : {NV_INGEST_CLIENT_VERSION}")
        return

    try:
        configure_logging(logger, log_level)
        logging.debug(f"nv-ingest-cli:params:\n{json.dumps(ctx.params, indent=2, default=repr)}")

    except Exception as err:
        logging.error(f"Error: {err}")
        raise


if __name__ == "__main__":
    main()
