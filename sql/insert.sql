INSERT INTO public.genre (name_genre) VALUES
            ('Поп-музыка'),
            ('Джаз'),
            ('Блюз'),
            ('Шансон'),
            ('Рок'),
            ('Рэп'),
            ('Электронная музыка'),
            ('Хип-хоп');

INSERT INTO public.albums (name_album,release_year) VALUES
            ('Billie jean', 1982),
            ('Hello Dolly', 1963),
            ('The Best of the Early Years', 2007),
            ('Я Открою Свое Сердце', 2012),
            ('Чёрный пёс Петербург', 1993),
            ('Баста 40', 2020),
            ('Самолет', 2018),
            ('С самых низов', 2016);

INSERT INTO public.singers (name_singers,nickname) VALUES
            ('Michael Jackson','Майк'),
            ('Луи Дэниел Армстронг','Армстронг'),
            ('Би Би Кинг', 'Кинг'),
            ('Михайлов Стас','Хохляндия'),
            ('ДДТ','Шевчук'),
            ('Баста','Бородатый'),
            ('Чугунный Скороход','Самолет'),
            ('Леван Горозия','L’One');

INSERT INTO public.singers_albums (id_singer,id_album) VALUES
            (1,1),
            (2,2),
            (3,3),
            (4,4),
            (5,5),
            (6,6),
            (7,7),
            (8,8);

INSERT INTO public.singers_genres (id_genre,id_singer) VALUES
            (1,1),
            (2,2),
            (3,3),
            (4,4),
            (5,5),
            (6,6),
            (7,7),
            (8,8),
            (8,6),
            (6,8);

INSERT INTO public.singles (id_album,name_single,duration) VALUES
            (1,'Billie Jean',290),
            (1,'Cant Get Outta the Rain',240),
            (1,'Billie Jean(Длинная версия)',380),
            (1,'Billie Jean(Инструментальная версия)',380),
            (1,'Its the Falling in Love',226),
            (1,'Billie Jean (Extended Re-Mix)',380);

INSERT INTO public.singles (id_album,name_single,duration) VALUES
            (2,'Hello, Dolly!',147),
            (2,'Its Been a Long, Long',142),
            (2,'A Lot of Livin to Do',156),
            (2,'A Kiss to Build a Dream On',271),
            (2,'Someday',221),
            (2,'Hey, Look Me Over',158),
            (2,'I Still Get Jealous',133),
            (2,'Moon River',179);
            
INSERT INTO public.singles (id_album,name_single,duration) VALUES
            (3,'BB Boogie',237),
            (3,'Shes Dynamite',215),
            (3,'A Lot of Livin to Do',156),
            (3,'A Kiss to Build a Dream On',271),
            (3,'Someday',221),
            (3,'Hey, Look Me Over',158),
            (3,'I Still Get Jealous',133),
            (3,'Moon River',179),
            (3,'Please Love Me',234),
            (3,'Woke Up This Morning',433),
            (3,'You Upset Me Baby',345),
            (3,'Dont Look Now, But Ive Got The Blues',341);

INSERT INTO public.singles (id_album,name_single,duration) VALUES
            (4,'Intro (Live)',270),
            (4,'Я вижу пустоту (Live)',440),
            (4,'Я к вечности шагаю (Live)',500),
            (4,'Жене (Live)',225),
            (4,'За воротами времени (Live)',226),
            (4,'Живу и таю (Live)',400),
            (4,'Почти устал (Live)',414);

INSERT INTO public.singles (id_album,name_single,duration) VALUES
            (5,'Пролог',225),
            (5,'Новые блокадники',328),
            (5,'Styx',269),
            (5,'Храм',257),
            (5,'Беда',510),
            (5,'Ты не один',308),
            (5,'Я остановил время',308),
            (5,'В это',286),
            (5,'Post интеллигент (бонус CD-издания)',287),
            (5,'Террорист (бонус CD-издания)',504);
    
INSERT INTO public.singles (id_album,name_single,duration) VALUES
            (6,'Интро',145),
            (6,'С самых низов',339),
            (6,'Верил всегда',344),
            (6,'Время догонит нас',306),
            (6,'+100500',348),
            (6,'Дочь огня',249),
            (6,'Я вижу',370),
            (6,'Не дотянуться до звёзд',249),
            (6,'ГотеMMосква',271),
            (6,'Молодость',350);

INSERT INTO public.singles (id_album,name_single,duration) VALUES
            (7,'Амстердам супер расколбас',182),
            (7,'Тревога!',285),
            (7,'Самолёт',527),
            (7,'мой cамолет (Всю ночь под Феном)',352),
            (7,'Сначала по одной потом по половинке всё что нужно для хорошей вечеринки В',313),
            (7,'Всё,что нужно для хорошей вечеринки',248),
            (7,'Половинка (Polovinka Re-Work) (Radio Cut)',339),
            (7,'North-West GSM original mix',342);

INSERT INTO public.singles (id_album,name_single,duration) VALUES
            (8,'С самых низов',213),
            (8,'Эльдорадо',247),
            (8,'Рутина',315);

INSERT INTO public.collections (name_collection,release_year) VALUES
            ('Cборник 1',2015), 
            ('Cборник 2',2016), 
            ('Cборник 3',2017), 
            ('Cборник 4',2018), 
            ('Cборник 5',2019), 
            ('Cборник 6',2020), 
            ('Cборник 7',2021), 
            ('Cборник 8',2022);

INSERT INTO public.collections_singles (id_collection,id_single) VALUES
            (1,1),
            (1,2),
            (8,3),
            (1,4),
            (1,5),
            (1,6),
            (1,7),
            (8,8),
            (2,9),
            (2,10),
            (5,11),
            (2,12),
            (2,13),
            (6,14),
            (2,15),
            (2,16),
            (7,17),
            (3,18),
            (3,19),
            (3,20),
            (3,21),
            (3,22),
            (4,23),
            (3,24),
            (4,25),
            (3,26),
            (1,27),
            (1,28),
            (3,29),
            (4,30),
            (1,31),
            (4,32),
            (4,33),
            (5,34),
            (4,35),
            (4,36),
            (5,37),
            (5,38),
            (5,39),
            (5,40),
            (5,41),
            (6,42),
            (6,43),
            (6,44),
            (6,45),
            (7,46),
            (7,47),
            (7,48),
            (7,49),
            (7,50),
            (7,51),
            (8,52),
            (8,53),
            (8,54),
            (8,55);