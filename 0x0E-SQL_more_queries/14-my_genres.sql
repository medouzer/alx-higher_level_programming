--  script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tg.name FROM tv_genres tg
JOIN tv_show_genres sg ON tg.id = sg.genre_id
JOIN tv_shows ON sg.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tg.name ASC;
