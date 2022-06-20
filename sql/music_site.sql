SET client_encoding = 'UTF8';

CREATE TABLE public.albums (
    id integer NOT NULL,
    name_album text,
    reales_year date
);

COMMENT ON TABLE public.albums IS 'Альбомы';
COMMENT ON COLUMN public.albums.id IS 'Идентификатор альбома';
COMMENT ON COLUMN public.albums.name_album IS 'Наименование альбома';
COMMENT ON COLUMN public.albums.reales_year IS 'Год выпуска';


CREATE SEQUENCE public.albums_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.albums_id_seq OWNED BY public.albums.id;

CREATE TABLE public.collections (
    id integer NOT NULL,
    name_collection text,
    reales_year date
);


COMMENT ON TABLE public.collections IS 'Сборники';
COMMENT ON COLUMN public.collections.id IS 'Идентификатор сборника';
COMMENT ON COLUMN public.collections.name_collection IS 'Наименование сборника';
COMMENT ON COLUMN public.collections.reales_year IS 'Год выпуска';

CREATE SEQUENCE public.collections_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.collections_id_seq OWNED BY public.collections.id;

CREATE TABLE public.collections_singles (
    id_collection integer NOT NULL,
    id_single integer NOT NULL
);

COMMENT ON TABLE public.collections_singles IS 'Связка сборники- треки';
COMMENT ON COLUMN public.collections_singles.id_collection IS 'Идентификатор сборника';
COMMENT ON COLUMN public.collections_singles.id_single IS 'Идентификатор трека';

CREATE SEQUENCE public.collections_singles_id_collection_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.collections_singles_id_collection_seq OWNED BY public.collections_singles.id_collection;

CREATE SEQUENCE public.collections_singles_id_single_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.collections_singles_id_single_seq OWNED BY public.collections_singles.id_single;

CREATE TABLE public.genre (
    id integer NOT NULL,
    name_genre text
);

COMMENT ON TABLE public.genre IS 'Жанры';
COMMENT ON COLUMN public.genre.id IS 'Идентификатор жанра';
COMMENT ON COLUMN public.genre.name_genre IS 'Наименование жанра';

CREATE SEQUENCE public.genre_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.genre_id_seq OWNED BY public.genre.id;

CREATE TABLE public.singers (
    name_singers text,
    nickname text,
    id integer NOT NULL
);

COMMENT ON TABLE public.singers IS 'Исполнители';
COMMENT ON COLUMN public.singers.name_singers IS 'Имя испонителя';
COMMENT ON COLUMN public.singers.nickname IS 'Псевдоним';
COMMENT ON COLUMN public.singers.id IS 'Идентификатор исполнителя';


CREATE TABLE public.singers_albums (
    id_singer integer NOT NULL,
    id_album integer NOT NULL
);

COMMENT ON TABLE public.singers_albums IS 'Связка исполнитель-альбом';
COMMENT ON COLUMN public.singers_albums.id_singer IS 'Идентификатор исполнителя';
COMMENT ON COLUMN public.singers_albums.id_album IS 'Идентификатор альбома';

CREATE SEQUENCE public.singers_albums_id_album_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.singers_albums_id_album_seq OWNED BY public.singers_albums.id_album;

CREATE SEQUENCE public.singers_albums_id_singer_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.singers_albums_id_singer_seq OWNED BY public.singers_albums.id_singer;

CREATE TABLE public.singers_genres (
    id_genre integer NOT NULL,
    id_singer integer NOT NULL
);

COMMENT ON TABLE public.singers_genres IS 'Связка исполнитель-жанр';
COMMENT ON COLUMN public.singers_genres.id_genre IS 'Идентификатор жанра';
COMMENT ON COLUMN public.singers_genres.id_singer IS 'Идентификатор исполнителя';

CREATE SEQUENCE public.singers_genres_id_genre_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.singers_genres_id_genre_seq OWNED BY public.singers_genres.id_genre;

CREATE SEQUENCE public.singers_genres_id_singer_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.singers_genres_id_singer_seq OWNED BY public.singers_genres.id_singer;

CREATE SEQUENCE public.singers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.singers_id_seq OWNED BY public.singers.id;

CREATE TABLE public.singles (
    id integer NOT NULL,
    id_album integer NOT NULL,
    name_single text,
    duration time without time zone
);

COMMENT ON TABLE public.singles IS 'Треки';
COMMENT ON COLUMN public.singles.id IS 'Идентификатор трека';
COMMENT ON COLUMN public.singles.id_album IS 'Идентификатор альбом';
COMMENT ON COLUMN public.singles.name_single IS 'Наименование трека';
COMMENT ON COLUMN public.singles.duration IS 'Длительность';


CREATE SEQUENCE public.singles_id_album_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.singles_id_album_seq OWNED BY public.singles.id_album;

CREATE SEQUENCE public.singles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER SEQUENCE public.singles_id_seq OWNED BY public.singles.id;

ALTER TABLE ONLY public.albums ALTER COLUMN id SET DEFAULT nextval('public.albums_id_seq'::regclass);
ALTER TABLE ONLY public.collections ALTER COLUMN id SET DEFAULT nextval('public.collections_id_seq'::regclass);
ALTER TABLE ONLY public.collections_singles ALTER COLUMN id_collection SET DEFAULT nextval('public.collections_singles_id_collection_seq'::regclass);
ALTER TABLE ONLY public.collections_singles ALTER COLUMN id_single SET DEFAULT nextval('public.collections_singles_id_single_seq'::regclass);
ALTER TABLE ONLY public.genre ALTER COLUMN id SET DEFAULT nextval('public.genre_id_seq'::regclass);
ALTER TABLE ONLY public.singers ALTER COLUMN id SET DEFAULT nextval('public.singers_id_seq'::regclass);
ALTER TABLE ONLY public.singers_albums ALTER COLUMN id_singer SET DEFAULT nextval('public.singers_albums_id_singer_seq'::regclass);
ALTER TABLE ONLY public.singers_albums ALTER COLUMN id_album SET DEFAULT nextval('public.singers_albums_id_album_seq'::regclass);
ALTER TABLE ONLY public.singers_genres ALTER COLUMN id_genre SET DEFAULT nextval('public.singers_genres_id_genre_seq'::regclass);
ALTER TABLE ONLY public.singers_genres ALTER COLUMN id_singer SET DEFAULT nextval('public.singers_genres_id_singer_seq'::regclass);
ALTER TABLE ONLY public.singles ALTER COLUMN id SET DEFAULT nextval('public.singles_id_seq'::regclass);
ALTER TABLE ONLY public.singles ALTER COLUMN id_album SET DEFAULT nextval('public.singles_id_album_seq'::regclass);

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
