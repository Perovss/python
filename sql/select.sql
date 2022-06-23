-- Альбомы релиза 2018 года
SELECT name_album as "Название альбома", release_year as "Дата релиза" FROM public.albums
where release_year = 2018;

-- Максимально длинный трек
SELECT name_single as "Наименование трека", duration as "Длительность" FROM public.singles
order by duration desc
limit 1;

-- Треки, длительность которых не менее 3,5 минут 
SELECT name_single as "Наименование трека", duration FROM public.singles
where duration >= 210
order by duration desc;

-- Сборники релиза 2018-2021 годов включительно
SELECT name_collection as "Название сборника", release_year as "Год релиза" FROM public.collections
where  release_year between 2018 and 2021
order by release_year desc;

-- Исполнители, чье имя состоит из одного слова
select name_singers as "Исполнитель", nickname as "Псевдоним" from public.singers
where name_singers not like '% %'
order by name_singers;

-- Название треков со словом "мой" / "my"
select name_single as "Название трека", duration as "Длительность" from public.singles
where name_single ilike '% мой' or name_single ilike  '% мой %' or name_single ilike  'мой %' or
      name_single ilike '% my' or name_single ilike  '% my %' or name_single ilike  'my %' 
order by name_single; 