import argparse
from app.utils.logging_helper import logger
from app.core.config import AppConfig
import sys
from omegaconf import DictConfig


def get_config() -> DictConfig:
    """
    Load application configuration.

    Returns:
    - DictConfig: The loaded configuration object.
    """
    try:        
        # Load the configuration
        app_config = AppConfig()
        cfg = app_config.load_config()

        # Log successful configuration loading
        logger.info('Configuration loaded successfully')
        return cfg

    except Exception as e:
        # Log any errors encountered during configuration loading
        logger.error(f'Failed to load configuration due to error: {str(e)}')
        sys.exit(1)

