-- Lists all genres in hbtn_0d_tvshows_rate by their rating sum.
SELECT g.`name`, SUM(r.`rate`) AS `rating`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s
ON g.`id` = s.`genre_id`
INNER JOIN `tv_show_ratings` AS r
ON s.`show_id` = r.`show_id`
GROUP BY g.`name`
ORDER BY `rating` DESC;
