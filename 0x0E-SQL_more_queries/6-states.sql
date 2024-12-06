-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the newly created database
USE hbtn_0d_usa;

-- Create the table `states` if it does not exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique, auto-incremented, non-null, primary key
    name VARCHAR(256) NOT NULL          -- Name column, cannot be null
);
