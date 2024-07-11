from app.utils.dependency import get_config
from app.utils.init_db import SessionLocal
from app.components.data_ingestion import DataIngestionHandler
from app.components.data_transformation import DataTransformationHandler
from app.components.data_persistence import DataPersistence
from app.components.db import EventRepository
from app.utils.logging_helper import logger


config = get_config()
db = SessionLocal()

def scrap_web_ctrl():
    """
    Control function to handle the web scraping, data transformation, and data persistence workflow.
    
    This function orchestrates the process of scraping web data, transforming it into JSON format, and 
    saving it to the database.
    """
    logger.info("Starting web scraping control function.")
    
    # Data ingestion from the web
    data_ingestion = DataIngestionHandler(base_url=config.app.base_url)
    events = data_ingestion.get_all_events()
    events_info = [data_ingestion.get_event_info(event) for event in events if event is not None]
    logger.info("Data ingestion completed.")

    # Data transformation
    data_transformation = DataTransformationHandler()
    json_dict = [data_transformation.transform_to_json(html_content=html_content) for html_content in events_info if html_content is not None]
    logger.info("Data transformation completed.")

    # Data persistence to the database
    event_repository = EventRepository(db=db)

    for data in json_dict:
        if data is not None:
            data_persistence = DataPersistence(data=data, repository=event_repository)
            data_persistence.save_to_db()
            logger.info(f"Data saved to database: {data}")
            print(f"\ndata: {data} \nsaved in database successfully\n")
    
    logger.info("Web scraping control function completed.")

