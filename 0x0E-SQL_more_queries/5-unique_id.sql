-- script that creates the table unique_id on your MySQL server
-- conect with mysql -u root -p
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE, name VARCHAR(256));
