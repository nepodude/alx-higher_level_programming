-- create the database hbtn_0d_2 if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- create the user user_0d_2 with specified password.
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';

-- grant SELECT privilege on the database hbtn_0d_2 to the user user_0d_2.
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
