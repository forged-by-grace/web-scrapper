import os
import sys
import logging

# Define the logging format
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Set the logging path
log_dir = "log"
log_filepath = os.path.join(log_dir, "audit.log")
os.makedirs(log_dir, exist_ok=True)

# Configure the logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level to DEBUG to capture all levels of log messages
    format=logging_str,   # Set the logging format
    handlers=[
        logging.FileHandler(log_filepath), # Log mesages to the audit.log
        logging.StreamHandler(sys.stdout)   # Also log messages to the console (stdout)
    ]
)

# Create a logger instance for the "accounts-api" component
logger = logging.getLogger("Web scrapper")
