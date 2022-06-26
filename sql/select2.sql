-- 1. Количество исполнителей в каждом жанре
SELECT name_genre AS "Жанр",count(singers_genres.id_genre) AS "Количество исполнителей" FROM public.genre
JOIN public.singers_genres ON genre.id = singers_genres.id_genre
GROUP BY name_genre
ORDER BY 2;

-- 2. Количество треков вошедших в альбомы 2019-2020 гг.
SELECT count(id) AS "Количество треков" FROM singles s
WHERE id_album IN 
	(SELECT id FROM public.albums albums WHERE albums.releASe_year BETWEEN 2020 AND 2020);

-- 3. Средняя продолжительность треков по каждому альбому
SELECT a.name_album AS "Назване альбома", 
	to_char((coalesce(avg(s.duration), 0)|| ' second')::interval,'MI:SS') AS "Средняя длительность трека" 
	FROM public.singles s 
RIGHT OUTER JOIN public.albums a ON s.id_album = a.id
GROUP BY a.name_album 
ORDER BY 2;

-- 4. Все исполнители, которые не выпустили альбомы в 2020 году
SELECT s.name_singers  AS "Исполнитель" FROM public.singers s
WHERE s.id NOT IN (
	SELECT sa.id_singer  FROM public.singers_albums sa 
	JOIN public.albums b ON sa.id_album  = b.id 
	WHERE b.release_year = 2020)
ORDER BY 1;

-- 5. Названия сборников, в которых присутствует конкретный исполнитель
SELECT c.name_collection AS "Название сборника" FROM public.collections c 
JOIN public.collections_singles cs ON c.id = cs.id_collection 
JOIN public.singles s ON cs.id_single = s.id 
JOIN public.albums a2 ON s.id_album  = a2.id 
JOIN public.singers_albums sa ON a2.id = sa.id_album  
JOIN public.singers_albums sa2 ON sa.id_singer  = sa2.id_singer  
JOIN public.singers s2 ON sa2.id_singer  = s2.id 
WHERE s2.name_singers  ilike '%ДДТ%'
GROUP BY 1;

-- 6. Название альбомов, в которых присутствуют исполнители более 1 жанра
SELECT a.name_album AS "Название альбома", s.name_singers AS "Исполнитель", count(sg.id_genre)
	 AS "Кол-во жанров" FROM public.albums a 
JOIN public.singers_albums sa ON a.id = sa.id_album  
JOIN public.singers s ON sa.id_singer = s.id 
JOIN public.singers_genres sg ON s.id = sg.id_singer  
GROUP BY a.name_album , s.name_singers 
HAVING count(sg.id_singer) > 1
ORDER BY 1,2;

-- 7. Наименование треков, которые не входят в сборники
SELECT s.name_single  AS "Наименование трека" FROM public.singles s 
LEFT JOIN public.collections_singles cs ON s.id = cs.id_single  
WHERE cs.id_single  is null
ORDER BY 1;

-- 8. Исполнителя(-ей), написавшего самый короткий по продолжительности трек
SELECT s.name_singers  AS "Исполнитель", s3.name_single AS "Трек",
	to_char((coalesce((s3.duration), 0)|| ' second')::interval,'MI:SS') AS "Длительность трека" 
	FROM public.singers s 
JOIN public.singers_albums sa ON s.id = sa.id_singer  
JOIN public.albums s2 ON sa.id_album  = s2.id 
JOIN public.singles s3 ON s2.id = s3.id_album  
WHERE s3.duration IN (SELECT min(s4.duration) FROM public.singles s4)
ORDER BY 1, 2;

-- 9. Название альбомов, содержащих наименьшее количество треков
SELECT a.name_album  "Название альбома", count(s.id) AS "Кол-во треков" FROM public.albums a 
LEFT JOIN public.singles s ON a.id = s.id_album  
GROUP BY 1
HAVING count(s.id) =
	(SELECT min(cnt) FROM (SELECT s2.id_album AS id, count(s2.id) AS cnt FROM public.singles s2
		GROUP BY s2.id_album) c)
ORDER BY 1;