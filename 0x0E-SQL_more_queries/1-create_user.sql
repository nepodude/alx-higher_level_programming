-- Create MYSQL server user. If user exists nothing fails.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Grant all privileges to the user on the entire MYSQL server
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
-- Ensure privileges take effect immediately by flushing them.
FLUSH PRIVILEGES;
