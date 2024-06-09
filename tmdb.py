import requests
import pandas as pd
import os
from dotenv import load_dotenv
import json

# Load environment variables from .env file in the same directory
load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

TMDB_API_KEY = os.getenv('TMDB_API_KEY')
TMDB_API_URL = 'https://api.themoviedb.org/3'

def fetch_tmdb_data(movie_title):
    params = {
        'api_key': TMDB_API_KEY,
        'query': movie_title
    }
    search_url = f'{TMDB_API_URL}/search/movie'
    response = requests.get(search_url, params=params)
    results = response.json().get('results', [])
    if results:
        movie_id = results[0]['id']
        movie_url = f'{TMDB_API_URL}/movie/{movie_id}'
        movie_response = requests.get(movie_url, params={'api_key': TMDB_API_KEY})
        movie_data = movie_response.json()
        save_json(movie_data, movie_title)
        return movie_data
    return {}

def save_json(data, movie_title):
    file_path = f"{movie_title.replace(' ', '_').lower()}.json"
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {file_path}")

def fetch_multiple_tmdb_movies(movie_titles):
    movies_data = []
    for title in movie_titles:
        data = fetch_tmdb_data(title)
        if data:
            movies_data.append(data)
    return pd.DataFrame(movies_data)

# Example usage
if __name__ == "__main__":
    movie_titles = ['Inception', 'The Matrix', 'Interstellar']
    df_tmdb = fetch_multiple_tmdb_movies(movie_titles)
    print(df_tmdb.head())
