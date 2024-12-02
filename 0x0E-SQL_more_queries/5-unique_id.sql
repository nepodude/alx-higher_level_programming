-- create a table unique_id and won't fail if it does exits.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE 1,
    name VARCHAR(256)
);
