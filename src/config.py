import os
from dotenv import load_dotenv
from pathlib import Path  # python3 only

# load enviorment variables
env_path = 'src/config/.env'
load_dotenv(dotenv_path=env_path)


class Config:
    """
    Set SigmaConverter configuration vars from .env file
    """

    # Load in environment variables
    # These fields are associated with logger
    LOG_FILE = os.getenv('LOG_FILE')
    LOG_FORMAT = os.getenv('LOG_FORMAT')  
    OUTPUT = os.getenv('OUTPUT')
    FILE_DIRECTORY = os.getenv('FILE_DIRECTORY')
    FILE_FORMAT = os.getenv('FILE_FORMAT')