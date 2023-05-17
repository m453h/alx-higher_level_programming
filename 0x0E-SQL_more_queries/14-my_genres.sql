-- This script uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT tg.`name`
FROM `tv_shows` AS ts
INNER JOIN `tv_show_genres` AS tsg
ON ts.`id` = tsg.`show_id`
INNER JOIN `tv_genres` AS tg
ON tg.`id` = tsg.`genre_id`
WHERE ts.`title` = "Dexter"
ORDER BY tg.`name`;
