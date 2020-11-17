CREATE TABLE IF NOT EXISTS orders (
  id serial PRIMARY KEY,
  user_id INT,
  FOREIGN KEY (user_id)
      REFERENCES users (user_id)
)
