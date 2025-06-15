-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT
    genre.name AS genre,
    COUNT(mapping.show_id) AS number_of_shows
FROM
    tv_genres AS genre
INNER JOIN
    tv_show_genres AS mapping
ON
    genre.id = mapping.genre_id
GROUP BY
    genre.name
ORDER BY
    number_of_shows DESC;