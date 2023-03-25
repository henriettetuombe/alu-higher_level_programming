-- 10-genre_id_by_show.sql
SELECT s.title, g.genre_id
FROM tv_shows s, tv_show_genres g
WHERE g.show_id = s.id
ORDER BY s.title ASC, g.genre_id ASC;
