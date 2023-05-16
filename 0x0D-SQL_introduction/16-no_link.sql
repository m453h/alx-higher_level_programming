-- This script lists all records of the table second_table of 
-- the database hbtn_0c_0 in your MySQL server.
--  i) It doesn't list rows without a name value
-- ii) Results should display the score and the name
-- iii) Records should be listed by descending score
-- iv) The database name will be passed as an argument to the mysql command
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;