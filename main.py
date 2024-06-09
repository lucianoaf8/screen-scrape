from omdb import fetch_multiple_movies as fetch_omdb_movies
from tmdb import fetch_multiple_tmdb_movies
from utils import save_to_database
import os
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env file in the same directory
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

def fetch_and_save_data(movie_titles):
    omdb_data = fetch_omdb_movies(movie_titles)
    tmdb_data = fetch_multiple_tmdb_movies(movie_titles)
    
    combined_data = pd.merge(omdb_data, tmdb_data, left_on='Title', right_on='title', suffixes=('_omdb', '_tmdb'))
    save_to_database(combined_data)

# Example usage
if __name__ == "__main__":
    movie_titles = ['Inception', 'The Matrix', 'Interstellar']
    fetch_and_save_data(movie_titles)
