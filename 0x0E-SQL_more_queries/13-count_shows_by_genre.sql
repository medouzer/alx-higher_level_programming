-- script that lists all genres from hbtn_0d_tvshows
SELECT s.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres s JOIN tv_show_genres sg ON s.id = sg.genre_id
GROUP BY genre ORDER BY number_of_shows DESC;
