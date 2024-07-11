from typing import List
import requests
from bs4 import BeautifulSoup
import json
from app.utils.logging_helper import logger


class DataIngestionHandler:
    """
    A class to handle data ingestion from a given URL.
    
    Attributes:
        base_url (str): The base URL to fetch events from.
    """

    def __init__(self, base_url: str):
        """
        Initialize the DataIngestionHandler with a base URL.
        
        Parameters:
            base_url (str): The base URL to fetch events from.
        """
        self.base_url = base_url
        logger.info(f"DataIngestionHandler initialized with base URL: {base_url}")

    def get_all_events(self) -> List[dict] | None:
        """
        Fetch all events from the base URL.
        
        Returns:
            List[dict]: A list of dictionaries containing event details.
            None: If the request to the base URL fails.
        """
        logger.info(f"Fetching all events from {self.base_url}")
        response = requests.get(self.base_url)

        if response.status_code == 200:
            logger.info("Successfully fetched events page")
            soup = BeautifulSoup(response.content, 'html.parser')
            event_items = soup.find_all('div', class_='event-content')
            events = []
            for item in event_items:
                event = {}
                event_type = item.find('a', class_='event-type')
                event_datetime = item.find('span', class_='event-dates')
                h3_tag = item.find('h3', class_='editorial-card-title')
                event_title = h3_tag.find('a')
                event_description = item.find('p')
                event_details_url = event_title['href']

                if event_type and event_datetime and event_title and event_description and event_details_url:
                    event['type'] = event_type.text.strip()
                    event['name'] = event_title.text.strip()
                    event['datetime'] = event_datetime.text.strip()
                    event['url'] = f"{self.base_url}{event_details_url.split('/')[-1]}"
                    events.append(event)
                    logger.info(f"Event added: {event}")

            return events
        logger.error(f"Failed to fetch events page, status code: {response.status_code}")
        return None

    def get_event_info(self, event: dict) -> str | None:
        """
        Fetch detailed information for a specific event.
        
        Parameters:
            event (dict): A dictionary containing event details including the URL.
        
        Returns:
            str: The detailed information of the event.
            None: If the request to the event details URL fails.
        """
        details_url = event.get('url')
        logger.info(f"Fetching event details from {details_url}")
        response = requests.get(details_url)

        if response.status_code == 200:
            logger.info(f"Successfully fetched event details from {details_url}")
            soup = BeautifulSoup(response.content, 'html.parser')
            info = soup.find('div', class_=['large-8'])
            return info
        logger.error(f"Failed to fetch event details, status code: {response.status_code}")
        return None
