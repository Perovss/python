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
select a.name_album as "Назване альбома", 
	to_char((coalesce(avg(s.duration), 0)|| ' second')::interval,'MI:SS') as "Средняя длительность трека" 
	from public.singles s 
	right outer join public.albums a on s.id_album = a.id
	group by a.name_album 
	order by 2;

-- 4. Все исполнители, которые не выпустили альбомы в 2020 году
select s.name_singers  as "Исполнитель" from public.singers s
where s.id not in (
	select sa.id_singer  from public.singers_albums sa 
	join public.albums b on sa.id_album  = b.id 
	where b.release_year = 2020)
	order by 1;
