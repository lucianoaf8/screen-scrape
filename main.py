import os
import time
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from api_wrappers import get_tmdb_all_movies

# Load environment variables from .env file
load_dotenv()

# Retrieve the environment variables
TMDB_API_KEY = os.getenv('TMDB_API_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')

def retrieve_all_movies():
    all_movies = []
    page = 1

    while True:
        data = get_tmdb_all_movies(TMDB_API_KEY, page)
        if 'results' in data:
            all_movies.extend(data['results'])
            if data['page'] >= data['total_pages']:
                break
            page += 1
            time.sleep(0.25)  # Handle API rate limiting
        else:
            break

    return all_movies

def import_data_to_db(movies_data):
    engine = create_engine(DATABASE_URL)
    conn = engine.connect()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id SERIAL PRIMARY KEY,
        title VARCHAR(255),
        release_date DATE,
        genre VARCHAR(255),
        director VARCHAR(255)
    )
    """)

    for movie in movies_data:
        conn.execute(f"""
        INSERT INTO movies (title, release_date, genre, director)
        VALUES ('{movie['title']}', '{movie['release_date']}', '{movie['genre']}', '{movie['director']}')
        """)

    conn.close()

if __name__ == "__main__":
    movies = retrieve_all_movies()
    print(f"Retrieved {len(movies)} movies")
    import_data_to_db(movies)
