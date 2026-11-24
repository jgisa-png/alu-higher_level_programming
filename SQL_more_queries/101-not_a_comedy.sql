-- Lists all shows without the genre Comedy in hbtn_0d_tvshows.
SELECT DISTINCT t.`title`
FROM `tv_shows` AS t
WHERE t.`title` NOT IN (
    SELECT t.`title`
    FROM `tv_shows` AS t
    INNER JOIN `tv_show_genres` AS s
    ON t.`id` = s.`show_id`
    INNER JOIN `tv_genres` AS g
    ON s.`genre_id` = g.`id`
    WHERE g.`name` = "Comedy"
)
ORDER BY t.`title` ASC;
