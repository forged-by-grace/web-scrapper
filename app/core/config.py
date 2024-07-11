from omegaconf import DictConfig, OmegaConf
from app.utils.logging_helper import logger
import sys
from hydra import compose, initialize
from pathlib import Path

class AppConfig:
    def __init__(self):
        """
        Initialize AppConfig with a path to configuration.
        
        Args:
        - cfg_path (DictConfig): Path to the environment configuration.
        """

    def load_config(self) -> DictConfig:
        """
        Load and merge environment-specific configuration.

        Returns:
        - DictConfig: Merged configuration object.
        """
        try:            
            # Initialize Hydra for configuration composition
            with initialize(version_base=None, config_path="../../config/", job_name='common'):
                # Load common configuration
                logger.info('Loading common config')
                common_cfg = OmegaConf.load('./config/config_common.yaml')
                logger.info('Common config loaded successfully')                
                
            return OmegaConf.create(common_cfg)
        
        except FileNotFoundError:
            logger.error(f"Error: Configuration file '{self.cfg_path}' not found.")
            sys.exit(1)
        
        except Exception as e:
            logger.error(f"Error loading configuration: {e}")
            sys.exit(1)
