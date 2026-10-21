CREATE TABLE IF NOT EXISTS films (
  id SERIAL PRIMARY KEY,
  title TEXT,
  year INT
);

TRUNCATE table films;

INSERT INTO films (title, year) VALUES ('Interstellar', 2020);
INSERT INTO films (title, year) VALUES ('Blood Diamonds', 2010);
INSERT INTO films (title, year) VALUES ('Inglorious Bastards', 2021);