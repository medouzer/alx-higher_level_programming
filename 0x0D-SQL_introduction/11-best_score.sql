-- script that lists all records with a score >= 10 in the table second_table
-- conect with mysql -uroot -p
SELECT score, name from second_table WHERE score >= 10 ORDER BY score DESC;
