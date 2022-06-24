SET client_encoding = 'UTF8';

CREATE TABLE public.albums (
    id serial4 NOT NULL,
    name_album text,
    release_year int4 null check (((release_year >= 1900) AND (release_year <= 9999)))
);

COMMENT ON TABLE public.albums IS 'Альбомы';
COMMENT ON COLUMN public.albums.id IS 'Идентификатор альбома';
COMMENT ON COLUMN public.albums.name_album IS 'Наименование альбома';
COMMENT ON COLUMN public.albums.reales_year IS 'Год выпуска';

CREATE TABLE public.collections (
    id serial4 NOT NULL,
    name_collection text,
    release_year int4 null check (((release_year >= 1900) AND (release_year <= 9999)))
);


COMMENT ON TABLE public.collections IS 'Сборники';
COMMENT ON COLUMN public.collections.id IS 'Идентификатор сборника';
COMMENT ON COLUMN public.collections.name_collection IS 'Наименование сборника';
COMMENT ON COLUMN public.collections.reales_year IS 'Год выпуска';

CREATE TABLE public.collections_singles (
    id_collection serial4 NOT NULL,
    id_single serial4 NOT NULL
);

COMMENT ON TABLE public.collections_singles IS 'Связка сборники- треки';
COMMENT ON COLUMN public.collections_singles.id_collection IS 'Идентификатор сборника';
COMMENT ON COLUMN public.collections_singles.id_single IS 'Идентификатор трека';

CREATE TABLE public.genre (
    id serial4 NOT NULL,
    name_genre text
);

COMMENT ON TABLE public.genre IS 'Жанры';
COMMENT ON COLUMN public.genre.id IS 'Идентификатор жанра';
COMMENT ON COLUMN public.genre.name_genre IS 'Наименование жанра';

CREATE TABLE public.singers (
    id serial4 NOT NULL,
    name_singers text,
    nickname text
);

COMMENT ON TABLE public.singers IS 'Исполнители';
COMMENT ON COLUMN public.singers.name_singers IS 'Имя испонителя';
COMMENT ON COLUMN public.singers.nickname IS 'Псевдоним';
COMMENT ON COLUMN public.singers.id IS 'Идентификатор исполнителя';


CREATE TABLE public.singers_albums (
    id_singer serial4 NOT NULL,
    id_album serial4 NOT NULL
);

COMMENT ON TABLE public.singers_albums IS 'Связка исполнитель-альбом';
COMMENT ON COLUMN public.singers_albums.id_singer IS 'Идентификатор исполнителя';
COMMENT ON COLUMN public.singers_albums.id_album IS 'Идентификатор альбома';

CREATE TABLE public.singers_genres (
    id_genre serial4 NOT NULL,
    id_singer serial4 NOT NULL
);

COMMENT ON TABLE public.singers_genres IS 'Связка исполнитель-жанр';
COMMENT ON COLUMN public.singers_genres.id_genre IS 'Идентификатор жанра';
COMMENT ON COLUMN public.singers_genres.id_singer IS 'Идентификатор исполнителя';

CREATE TABLE public.singles (
    id serial4 NOT NULL,
    id_album serial4 NOT NULL,
    name_single text,
    duration int4
);

COMMENT ON TABLE public.singles IS 'Треки';
COMMENT ON COLUMN public.singles.id IS 'Идентификатор трека';
COMMENT ON COLUMN public.singles.id_album IS 'Идентификатор альбом';
COMMENT ON COLUMN public.singles.name_single IS 'Наименование трека';
COMMENT ON COLUMN public.singles.duration IS 'Длительность';

ALTER TABLE ONLY public.albums
    ADD CONSTRAINT albums_pk PRIMARY KEY (id);

ALTER TABLE ONLY public.collections
    ADD CONSTRAINT collections_pk PRIMARY KEY (id);

ALTER TABLE ONLY public.genre
    ADD CONSTRAINT genre_pk PRIMARY KEY (id);

ALTER TABLE ONLY public.singers
    ADD CONSTRAINT singers_pk PRIMARY KEY (id);

ALTER TABLE ONLY public.singles
    ADD CONSTRAINT singles_pk PRIMARY KEY (id);

ALTER TABLE ONLY public.collections_singles
    ADD CONSTRAINT collections_singles_pk PRIMARY KEY (id_collection,id_single);   

ALTER TABLE ONLY public.singers_genres
    ADD CONSTRAINT singers_genres_pk PRIMARY KEY (id_genre,id_singer);

ALTER TABLE ONLY public.singers_albums
    ADD CONSTRAINT singers_albums_pk PRIMARY KEY (id_singer,id_album);



ALTER TABLE ONLY public.collections_singles
    ADD CONSTRAINT collections_singles_fk FOREIGN KEY (id_collection) REFERENCES public.collections(id);

ALTER TABLE ONLY public.collections_singles
    ADD CONSTRAINT collections_singles_fk2 FOREIGN KEY (id_single) REFERENCES public.singles(id);

ALTER TABLE ONLY public.singers_albums
    ADD CONSTRAINT singers_albums_fk FOREIGN KEY (id_singer) REFERENCES public.singers(id);

ALTER TABLE ONLY public.singers_albums
    ADD CONSTRAINT singers_albums_fk2 FOREIGN KEY (id_album) REFERENCES public.albums(id);

ALTER TABLE ONLY public.singers_genres
    ADD CONSTRAINT singers_genres_fk FOREIGN KEY (id_singer) REFERENCES public.singers(id);

ALTER TABLE ONLY public.singers_genres
    ADD CONSTRAINT singers_genres_fk2 FOREIGN KEY (id_genre) REFERENCES public.genre(id);

ALTER TABLE ONLY public.singles
    ADD CONSTRAINT singles_fk FOREIGN KEY (id_album) REFERENCES public.albums(id);
