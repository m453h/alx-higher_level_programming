-- This script lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command

SELECT ts.`title`, tsg.`genre_id` 
FROM `tv_shows` AS ts 
LEFT JOIN `tv_show_genres` AS tsg
ON ts.`id` = tsg.`show_id`
ORDER BY ts.`title`, tsg.`genre_id`;
