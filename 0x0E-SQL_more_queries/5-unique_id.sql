-- create a table unique_id and won't fail if it does exits.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAUL 1 UNIQUE,
    name VARCHAR(256)
);
