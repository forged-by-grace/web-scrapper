import json
from app.models.events import Event
from app.components.db import EventRepository
from app.utils.logging_helper import logger


class DataPersistence:
    """
    A class to handle data persistence operations.
    
    Attributes:
        data (list): The data to be persisted.
        repository (EventRepository): The repository to handle database operations.
    """

    def __init__(self, data: list, repository: EventRepository):
        """
        Initialize the DataPersistence with data and a repository.
        
        Parameters:
            data (list): The data to be persisted.
            repository (EventRepository): The repository to handle database operations.
        """
        self.data = data
        self.repository = repository
        logger.info("DataPersistence initialized with provided data and repository.")

    def save_to_db(self) -> None:
        """
        Save the provided data to the database.
        
        This method uses the repository's `save_to_db` method to persist the data.
        """
        logger.info("Saving data to the database.")
        try:
            self.repository.save_to_db(data=self.data)
            logger.info("Data successfully saved to the database.")
        except Exception as e:
            logger.error(f"Failed to save data to the database: {e}")
