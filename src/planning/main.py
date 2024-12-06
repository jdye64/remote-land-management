import logging
import click

from planning.service.space.runner import Runner
from util.click import LogLevel, RunMode, validate_asset_file_exists_expand_path, validate_not_empty
from util.system import configure_logging

logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--run_mode",
    type=click.Choice(
        [mode.value for mode in RunMode],
        case_sensitive=False
    ),
    default="FIT",
    show_default=True,
    help="Run mode the for the planning application.\n \
        CREATE a space to fit all assets\n \
        DREAM a space up with extra room\n \
        FIT all assets into a fixed sized space"
)
@click.option(
    "--assets_file",
    required=False,
    type=click.Path(exists=False),
    help="Specify the local file that contains the asset \
        definitions that should be planned against",
    callback=validate_asset_file_exists_expand_path,
)
@click.option(
    "--log_level",
    type=click.Choice(
        [level.value for level in LogLevel],
        case_sensitive=False
    ),
    default="INFO",
    show_default=True,
    help="Log level.",
)
@click.pass_context
def main(
    ctx,
    run_mode: str,
    log_level: str,
    assets_file: str,
):
    """Entry point for the floor/space planning application"""
    try:
        configure_logging(logger, log_level)
        logger.info("Run Mode: %s", run_mode)
        logger.info("Assets File: %s", assets_file)
        planning_runner = Runner(run_mode, assets_file)
        results = planning_runner.invoke()
        logger.info("Results: %s", results)
    except Exception as err:
        logging.error("Error: %s", err)
        raise


if __name__ == "__main__":
    main()
