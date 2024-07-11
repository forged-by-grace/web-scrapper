from app.utils.logging_helper import logger
from app.models.events import Event
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import List

class EventRepository:
    """
    A class to handle operations related to the Event database.
    
    Attributes:
        db (Session): The database session used for database operations.
    """

    def __init__(self, db: Session):
        """
        Initialize the EventRepository with a database session.
        
        Parameters:
            db (Session): The database session used for database operations.
        """
        self.db = db
        logger.info("EventRepository initialized with a database session.")

    def close(self):
        """
        Close the database session.
        
        This method logs the disconnection from the database and closes the session if it is open.
        """
        logger.info('Disconnecting from SQLite')
        if self.db:
            self.db.close()
            logger.info("Database session closed.")

    def save_to_db(self, data: dict) -> None:
        """
        Save the provided data to the database.
        
        This method converts the data dictionary to an Event object and attempts to add it to the database.
        
        Parameters:
            data (dict): The data to be saved to the database.
        """
        try:
            db_event = Event(**data)
            self.db.add(db_event)
            self.db.commit()
            self.db.refresh(db_event)
            logger.info("Data successfully persisted to the database.")
        except Exception as e:
            logger.error(f'Failed to persist data to Database due to error: {e}')
        finally:
            self.close()
