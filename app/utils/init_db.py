from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.utils.dependency import get_config
from app.utils.logging_helper import logger


# Load app configuration
config = get_config()
logger.info("App configuration loaded.")

# Initialize the SQLite database URL
SQLALCHEMY_DATABASE_URL = config.database.url
logger.info(f"Database URL initialized: {SQLALCHEMY_DATABASE_URL}")

# Create engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
logger.info("Database engine created.")

# Create a local session class instance
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
logger.info("SessionLocal class instance created.")

# Set the base class to be inherited by SQLAlchemy models
Base = declarative_base()
logger.info("Declarative base class set.")
