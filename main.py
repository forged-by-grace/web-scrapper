from app.controllers.controller import scrap_web_ctrl
from app.models.events import Base
from app.utils.init_db import SessionLocal, engine
from dotenv import load_dotenv
from app.utils.logging_helper import logger


# Load environment variables
load_dotenv()
logger.info("Environment variables loaded.")

if __name__ == "__main__":
    """
    Main entry point of the script. This script will:
    1. Load environment variables.
    2. Create the events table if it does not exist.
    3. Invoke the web scraping control function.
    """
    logger.info("Starting the main script.")

    # Create event table if it does not exist
    Base.metadata.create_all(bind=engine)
    logger.info("Event table checked/created.")

    # Execute the web scraping control function
    scrap_web_ctrl()
    logger.info("Web scraping control function executed.")
