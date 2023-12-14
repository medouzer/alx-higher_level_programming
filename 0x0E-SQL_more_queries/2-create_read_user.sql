-- script that creates the database hbtn_0d_2 and the user user_0d_2
-- conect with mysql -u root -p
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'LOCALHOST' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'LOCALHOST';
