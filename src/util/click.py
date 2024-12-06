import logging
from enum import Enum

import os
import click

logger = logging.getLogger(__name__)


class LogLevel(str, Enum):
    """Logging level for the application"""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class RunMode(str, Enum):
    """Mode that the planning application should run in."""
    CREATE = "CREATE"
    DREAM = "DREAM"
    FIT = "FIT"


def validate_not_empty(_, param, value):
    """Validates a Click parameter to make sure it is present and not empty"""
    if not value:
        raise click.BadParameter(f'Parameter: {param} cannot be empty.')
    return value


def validate_asset_file_exists_expand_path(_ctx, param, file_path):
    """
    Validates that the provided 'assets_file' exists. If the file 
    does exist the provided path is updated to be the fully qualified path
    """
    if not file_path:
        raise click.BadParameter(f'Parameter: {param} cannot be empty.')

    # Check if the file exists
    if not os.path.exists(file_path):
        raise click.BadParameter(
            f"The specified 'assets_file' - '{file_path}' does not exist.")

    # Expand the relative path to a fully qualified path
    absolute_path = os.path.abspath(file_path)

    return absolute_path
