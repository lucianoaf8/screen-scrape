import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env file in the same directory
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///movies.db')

def save_to_database(df):
    engine = create_engine(DATABASE_URL)
    df.to_sql('movies', engine, if_exists='replace', index=False)

def load_from_database():
    engine = create_engine(DATABASE_URL)
    return pd.read_sql('movies', engine)
