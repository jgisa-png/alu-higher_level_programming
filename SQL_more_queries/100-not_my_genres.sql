-- Lists all genres not linked to the show Dexter in hbtn_0d_tvshows.
SELECT DISTINCT g.`name`
FROM `tv_genres` AS g
WHERE g.`name` NOT IN (
    SELECT g.`name`
    FROM `tv_genres` AS g
    INNER JOIN `tv_show_genres` AS s
    ON g.`id` = s.`genre_id`
    INNER JOIN `tv_shows` AS t
    ON s.`show_id` = t.`id`
    WHERE t.`title` = "Dexter"
)
ORDER BY g.`name` ASC;
