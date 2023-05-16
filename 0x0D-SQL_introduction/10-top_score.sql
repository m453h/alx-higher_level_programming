-- Write a script that lists all records of the table second_table 
-- of the database hbtn_0c_0 in a MySQL server.
--  i. Results display both the score and the name
--  ii. Records are ordered by score (top first)
--  iii. The database name will be passed as an argument of the mysql command
SELECT `score`, `name` FROM `second_table` ORDER BY `score` DESC;
