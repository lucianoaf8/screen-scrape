import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file in the same directory
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

OMDB_API_KEY = os.getenv('OMDB_API_KEY')
OMDB_API_URL = 'http://www.omdbapi.com/'

def fetch_omdb_data(movie_title):
    params = {
        'apikey': OMDB_API_KEY,
        't': movie_title
    }
    response = requests.get(OMDB_API_URL, params=params)
    return response.json()

def fetch_multiple_movies(movie_titles):
    movies_data = []
    for title in movie_titles:
        data = fetch_omdb_data(title)
        if data['Response'] == 'True':
            movies_data.append(data)
    return pd.DataFrame(movies_data)
