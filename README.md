# Media Data Project

## Overview
This project retrieves data for movies from TMDB and stores it in a database.

## Setup
1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root and add your configuration:
    ```
    TMDB_API_KEY=your_tmdb_api_key
    DATABASE_URL=postgresql://user:password@localhost/mydatabase
    ```

5. Create the database and tables:
    ```bash
    psql -U yourusername -d yourdatabase -a -f create_tables.sql
    ```

## Running the Project
1. Retrieve and import data:
    ```bash
    python main.py
    ```

## Contributing
Feel free to submit issues or pull requests.
