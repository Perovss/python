-- INSERT INTO public.genre (name_genre) VALUES
--             ('Поп-музыка'),
--             ('Джаз'),
--             ('Блюз'),
--             ('Шансон'),
--             ('Рок'),
--             ('Рэп'),
--             ('Электронная музыка'),
--             ('Хип-хоп');

-- INSERT INTO public.albums (name_album,release_year) VALUES
--             ('Billie jean', 1982),
--             ('Hello Dolly', 1963),
--             ('The Best of the Early Years', 2007),
--             ('Я Открою Свое Сердце', 2012),
--             ('Чёрный пёс Петербург', 1993),
--             ('Мой альбом', 2021),
--             ('Самолет', 2018),
--             ('С самых низов', 2016)

-- INSERT INTO public.singers (name_singers,nickname) VALUES
--             ('Michael Jackson','Майк'),
--             ('Луи Дэниел Армстронг','Армстронг'),
--             ('Би Би Кинг', 'Кинг'),
--             ('Михайлов Стас','Хохляндия'),
--             ('ДДТ','Шевчук'),
--             ('Баста','Бородатый'),
--             ('Чугунный Скороход','Самолет'),
--             ('Леван Горозия','L’One')

-- INSERT INTO public.singers_albums (id_singer,id_album) VALUES
--             (1,1),
--             (2,2),
--             (3,3),
--             (4,4),
--             (5,5),
--             (6,6),
--             (7,7),
--             (8,8)
-- INSERT INTO public.singers_genres (id_genre,id_singer) VALUES
--             (1,1),
--             (2,2),
--             (3,3),
--             (4,4),
--             (5,5),
--             (6,6),
--             (7,7),
--             (8,8),
--             (8,6),
--             (6,8)
INSERT INTO public.singles (id_album,name_single,duration) VALUES
            (1,'Billie Jean',290),
            (2,'Cant Get Outta the Rain',240),
            (3,'Billie Jean(Длинная версия)',380),
            (4,'Billie Jean(Инструментальная версия)',380),
            (5,'Its the Falling in Love',226),
            (6,'Billie Jean (Extended Re-Mix)',380)

