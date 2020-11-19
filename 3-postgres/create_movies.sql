
DROP TABLE movies;

CREATE TABLE IF NOT EXISTS movies (
  id serial PRIMARY KEY,
  title VARCHAR(255) NOT NULL UNIQUE,
  genre VARCHAR(255),
  budget BIGINT,
  runtime DECIMAL,
  year INTEGER,
  month INTEGER,
  revenue BIGINT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
