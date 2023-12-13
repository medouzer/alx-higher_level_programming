-- script that lists all records of the table second_table
-- conect with mysql -uroot -p
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
