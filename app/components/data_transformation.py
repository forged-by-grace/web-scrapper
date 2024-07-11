import json
from openai import OpenAI
from app.utils.dependency import get_config
from app.utils.logging_helper import logger


config = get_config()

class DataTransformationHandler:
    """
    A class to handle data transformation operations using OpenAI's API.
    
    Attributes:
        client (OpenAI): The OpenAI client for API requests.
        model (str): The model to be used for OpenAI API requests.
    """

    def __init__(self):
        """
        Initialize the DataTransformationHandler with OpenAI client and model.
        """
        self.client = OpenAI(api_key=config.openai.api_key)
        self.model = config.openai.model
        logger.info("DataTransformationHandler initialized with OpenAI client and model.")

    def transform_to_json(self, html_content: str) -> dict:
        """
        Transform HTML content to a JSON object using OpenAI's API.
        
        Parameters:
            html_content (str): The HTML content to be transformed.
        
        Returns:
            dict: A dictionary containing the transformed JSON data.
        """
        logger.info("Transforming HTML content to JSON.")
        
        prompt = (
            "Create a JSON with the following fields: event_title, event_type, event_date, event_time, "
            "event_location, event_address properly formatted, age_range of this event to be estimated if not listed, "
            "is_free_event, event_cost to be estimated as a string if event is not free, from the following HTML:\n\n"
            f"{html_content}\n\n. Note: Only return the JSON Object without markdown formatting, explanations, or introductory statements."
        )

        try:
            completion = self.client.chat.completions.create(
                temperature=0,
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that helps with HTML to JSON conversion!"},
                    {"role": "user", "content": prompt}
                ]
            )
            json_str = completion.choices[0].message.content
            json_dict = json.loads(json_str)
            json_dict['other'] = html_content
            logger.info("HTML content successfully transformed to JSON.")
            return json_dict
        except Exception as e:
            logger.error(f"Failed to transform HTML content to JSON: {e}")
            return {}
