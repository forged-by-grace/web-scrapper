
# Web Scrapper and Processor

## Overview
This application is designed to scrape event data from a specified web source, transform the data into a structured JSON format, and persist it into a SQLite database. It leverages several components including data ingestion, data transformation, and data persistence to achieve this goal.

## Features
- **Web Scraping:** Scrapes event details from a given URL.
- **Data Transformation:** Converts the scraped HTML content into a JSON object using OpenAI's API.
- **Data Persistence:** Saves the transformed data into a SQLite database.

## Components
- **Data Ingestion Handler:** Handles the scraping of event data from the web.
- **Data Transformation Handler:** Converts scraped HTML data to JSON format.
- **Data Persistence:** Saves the transformed JSON data to the database.
- **Event Repository:** Manages database operations related to events.
- **Controller:** Orchestrates the workflow of scraping, transforming, and persisting data.

## Installation

### Prerequisites
- Python 3.8+
- `poetry` (Python package installer)

### Clone the Repository
```sh
git clone https://github.com/forged-by-grace/web-scrapper.git
cd web-scrapper

### Create a Virtual Environment
```sh
poetry new web-scrapper
```

### Install Dependencies
```sh
poetry add [dependencies]
```

### Set Up Environment Variables
Create a `.env` file in the root directory and add the following variables:
```env
OPENAI_API_KEY=your_openai_api_key
```

## Usage

### Run the Scraper
Execute the main script to start the web scraping, data transformation, and data persistence process:
```sh
python main.py
```

## Detailed Description of Components

### `data_ingestion.py`
Handles the process of scraping event data from the specified URL.

### `data_transformation.py`
Uses OpenAI's API to transform scraped HTML content into a structured JSON format.

### `data_persistence.py`
Manages the process of saving transformed JSON data into the SQLite database.

### `db.py`
Defines the database connection and session creation.

### `controller.py`
Orchestrates the overall workflow of data scraping, transformation, and persistence.

### `events.py`
Defines the SQLAlchemy model for events.

### `dependency.py`
Loads application configuration from environment variables.

### `init_db.py`
Initializes the SQLite database and creates the necessary tables.

### `logging_helper.py`
Configures and provides a logging helper for the application.


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
If you would like to contribute to this project, please open an issue or submit a pull request.

## Contact
For any inquiries or issues, please contact nornubariconfidence@gmail.com.

```