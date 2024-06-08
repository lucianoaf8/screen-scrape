CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    release_date DATE,
    genre VARCHAR(255),
    director VARCHAR(255)
);
