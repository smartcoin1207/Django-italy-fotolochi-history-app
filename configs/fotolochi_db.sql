--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.10
-- Dumped by pg_dump version 9.6.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(80) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO pmdbuser;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.auth_group_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO pmdbuser;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO pmdbuser;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO pmdbuser;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO pmdbuser;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.auth_permission_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO pmdbuser;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(30) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO pmdbuser;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO pmdbuser;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO pmdbuser;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.auth_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO pmdbuser;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO pmdbuser;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO pmdbuser;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: categories; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.categories (
    id integer NOT NULL,
    name character varying(128)
);


ALTER TABLE public.categories OWNER TO pmdbuser;

--
-- Name: categories_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categories_id_seq OWNER TO pmdbuser;

--
-- Name: categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.categories_id_seq OWNED BY public.categories.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO pmdbuser;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.django_admin_log_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO pmdbuser;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO pmdbuser;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.django_content_type_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO pmdbuser;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO pmdbuser;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO pmdbuser;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO pmdbuser;

--
-- Name: image_data; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.image_data (
    id integer NOT NULL,
    title character varying(128),
    short_description character varying(128),
    full_description character varying(128),
    date_updated timestamp with time zone NOT NULL,
    rating integer,
    creative boolean NOT NULL,
    is_publish boolean NOT NULL,
    img_file_id integer NOT NULL,
    api_id character varying(255),
    place_id integer
);


ALTER TABLE public.image_data OWNER TO pmdbuser;

--
-- Name: image_data_categories; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.image_data_categories (
    id integer NOT NULL,
    imagedata_id integer NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.image_data_categories OWNER TO pmdbuser;

--
-- Name: image_data_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.image_data_categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.image_data_categories_id_seq OWNER TO pmdbuser;

--
-- Name: image_data_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.image_data_categories_id_seq OWNED BY public.image_data_categories.id;


--
-- Name: image_data_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.image_data_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.image_data_id_seq OWNER TO pmdbuser;

--
-- Name: image_data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.image_data_id_seq OWNED BY public.image_data.id;


--
-- Name: image_data_tags; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.image_data_tags (
    id integer NOT NULL,
    imagedata_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.image_data_tags OWNER TO pmdbuser;

--
-- Name: image_data_tags_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.image_data_tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.image_data_tags_id_seq OWNER TO pmdbuser;

--
-- Name: image_data_tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.image_data_tags_id_seq OWNED BY public.image_data_tags.id;


--
-- Name: image_file; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.image_file (
    id integer NOT NULL,
    file_name character varying(128),
    original_name character varying(128),
    thumb_name character varying(128),
    preview_name character varying(128),
    added_date timestamp with time zone NOT NULL,
    is_color boolean NOT NULL,
    orientation character varying(128),
    is_new boolean NOT NULL
);


ALTER TABLE public.image_file OWNER TO pmdbuser;

--
-- Name: image_file_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.image_file_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.image_file_id_seq OWNER TO pmdbuser;

--
-- Name: image_file_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.image_file_id_seq OWNED BY public.image_file.id;


--
-- Name: places; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.places (
    id integer NOT NULL,
    name character varying(128)
);


ALTER TABLE public.places OWNER TO pmdbuser;

--
-- Name: places_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.places_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.places_id_seq OWNER TO pmdbuser;

--
-- Name: places_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.places_id_seq OWNED BY public.places.id;


--
-- Name: tags; Type: TABLE; Schema: public; Owner: pmdbuser
--

CREATE TABLE public.tags (
    id integer NOT NULL,
    name character varying(128),
    weight integer NOT NULL
);


ALTER TABLE public.tags OWNER TO pmdbuser;

--
-- Name: tags_id_seq; Type: SEQUENCE; Schema: public; Owner: pmdbuser
--

CREATE SEQUENCE public.tags_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tags_id_seq OWNER TO pmdbuser;

--
-- Name: tags_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pmdbuser
--

ALTER SEQUENCE public.tags_id_seq OWNED BY public.tags.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: categories id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.categories ALTER COLUMN id SET DEFAULT nextval('public.categories_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: image_data id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data ALTER COLUMN id SET DEFAULT nextval('public.image_data_id_seq'::regclass);


--
-- Name: image_data_categories id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data_categories ALTER COLUMN id SET DEFAULT nextval('public.image_data_categories_id_seq'::regclass);


--
-- Name: image_data_tags id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data_tags ALTER COLUMN id SET DEFAULT nextval('public.image_data_tags_id_seq'::regclass);


--
-- Name: image_file id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_file ALTER COLUMN id SET DEFAULT nextval('public.image_file_id_seq'::regclass);


--
-- Name: places id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.places ALTER COLUMN id SET DEFAULT nextval('public.places_id_seq'::regclass);


--
-- Name: tags id; Type: DEFAULT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.tags ALTER COLUMN id SET DEFAULT nextval('public.tags_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can add user	2	add_user
5	Can change user	2	change_user
6	Can delete user	2	delete_user
7	Can add permission	3	add_permission
8	Can change permission	3	change_permission
9	Can delete permission	3	delete_permission
10	Can add group	4	add_group
11	Can change group	4	change_group
12	Can delete group	4	delete_group
13	Can add content type	5	add_contenttype
14	Can change content type	5	change_contenttype
15	Can delete content type	5	delete_contenttype
16	Can add session	6	add_session
17	Can change session	6	change_session
18	Can delete session	6	delete_session
19	Can add place	7	add_place
20	Can change place	7	change_place
21	Can delete place	7	delete_place
22	Can add tag	8	add_tag
23	Can change tag	8	change_tag
24	Can delete tag	8	delete_tag
25	Can add image data	9	add_imagedata
26	Can change image data	9	change_imagedata
27	Can delete image data	9	delete_imagedata
28	Can add image to tag	10	add_imagetotag
29	Can change image to tag	10	change_imagetotag
30	Can delete image to tag	10	delete_imagetotag
31	Can add image files	11	add_imagefiles
32	Can change image files	11	change_imagefiles
33	Can delete image files	11	delete_imagefiles
34	Can add image to place	12	add_imagetoplace
35	Can change image to place	12	change_imagetoplace
36	Can delete image to place	12	delete_imagetoplace
37	Can add category	13	add_category
38	Can change category	13	change_category
39	Can delete category	13	delete_category
40	Can add image to category	14	add_imagetocategory
41	Can change image to category	14	change_imagetocategory
42	Can delete image to category	14	delete_imagetocategory
43	Can view log entry	1	view_logentry
44	Can view permission	3	view_permission
45	Can view group	4	view_group
46	Can view user	2	view_user
47	Can view content type	5	view_contenttype
48	Can view session	6	view_session
49	Can view category	13	view_category
50	Can view image data	9	view_imagedata
51	Can add image file	15	add_imagefile
52	Can change image file	15	change_imagefile
53	Can delete image file	15	delete_imagefile
54	Can view image file	15	view_imagefile
55	Can view image to category	14	view_imagetocategory
56	Can view image to place	12	view_imagetoplace
57	Can view image to tag	10	view_imagetotag
58	Can view place	7	view_place
59	Can view tag	8	view_tag
\.


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 59, true);


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$120000$K9gAUu8QqPb6$4K88ZSkSQ9jdRnaZxpqgvNLMOO3y/n1Z+19kL9lFp2E=	2018-08-17 15:41:33.838039+02	t	admin			test1.avv@gmail.com	t	t	2018-04-25 14:54:32.855681+02
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.categories (id, name) FROM stdin;
\.


--
-- Name: categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.categories_id_seq', 1, false);


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
\.


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 1, false);


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	user
3	auth	permission
4	auth	group
5	contenttypes	contenttype
6	sessions	session
7	administration	place
8	administration	tag
9	administration	imagedata
10	administration	imagetotag
11	administration	imagefiles
12	administration	imagetoplace
13	administration	category
14	administration	imagetocategory
15	administration	imagefile
\.


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 15, true);


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2018-04-25 14:48:24.266132+02
2	auth	0001_initial	2018-04-25 14:48:24.345342+02
3	admin	0001_initial	2018-04-25 14:48:24.377842+02
4	admin	0002_logentry_remove_auto_add	2018-04-25 14:48:24.393499+02
5	contenttypes	0002_remove_content_type_name	2018-04-25 14:48:24.442505+02
6	auth	0002_alter_permission_name_max_length	2018-04-25 14:48:24.450727+02
7	auth	0003_alter_user_email_max_length	2018-04-25 14:48:24.466532+02
8	auth	0004_alter_user_username_opts	2018-04-25 14:48:24.482085+02
9	auth	0005_alter_user_last_login_null	2018-04-25 14:48:24.498557+02
10	auth	0006_require_contenttypes_0002	2018-04-25 14:48:24.501482+02
11	auth	0007_alter_validators_add_error_messages	2018-04-25 14:48:24.514013+02
12	auth	0008_alter_user_username_max_length	2018-04-25 14:48:24.539525+02
13	auth	0009_alter_user_last_name_max_length	2018-04-25 14:48:24.554891+02
14	sessions	0001_initial	2018-04-25 14:48:24.568325+02
15	administration	0001_initial	2018-04-25 16:21:25.573513+02
16	administration	0002_auto_20180820_1258	2018-08-20 14:58:31.563462+02
17	admin	0003_logentry_add_action_flag_choices	2018-08-20 16:01:17.272915+02
18	administration	0003_auto_20180820_1345	2018-08-20 16:02:04.965322+02
\.


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 18, true);


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
nud2qozfhvvmc7v5pe2acqhktwywg05w	MzEzYjI1MDY4ZjNiNTJjOTVkNTA3ODFjZjFiYTgzYTMzMTY4NTBlNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDNiOGRkNWI0ZDYzYzE5MDBiMmJiMWY1ZTU2MzY1MGI3NmQ4NzY4NSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2018-05-09 17:20:12.284666+02
u1volc5rl2o1x6tc8rlkzbm7st33ezvj	MTMxNzk5NzRkOWZiYWQzNTA0ZTM0MmNhZDRmNzZkMTA4OGRkNzk2Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIwM2I4ZGQ1YjRkNjNjMTkwMGIyYmIxZjVlNTYzNjUwYjc2ZDg3Njg1In0=	2018-05-09 17:42:04.482041+02
e214f1dvm5n69tiv7bbqfqm3g02ld8x1	MzEzYjI1MDY4ZjNiNTJjOTVkNTA3ODFjZjFiYTgzYTMzMTY4NTBlNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDNiOGRkNWI0ZDYzYzE5MDBiMmJiMWY1ZTU2MzY1MGI3NmQ4NzY4NSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2018-05-09 19:12:58.932012+02
v04jg5vwy9luzs6pmfwhmfwqzftl0dub	MzEzYjI1MDY4ZjNiNTJjOTVkNTA3ODFjZjFiYTgzYTMzMTY4NTBlNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDNiOGRkNWI0ZDYzYzE5MDBiMmJiMWY1ZTU2MzY1MGI3NmQ4NzY4NSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2018-05-09 20:48:00.7186+02
iiqa845eaqs4nwxweprf3g3hczxa1l7j	MzEzYjI1MDY4ZjNiNTJjOTVkNTA3ODFjZjFiYTgzYTMzMTY4NTBlNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDNiOGRkNWI0ZDYzYzE5MDBiMmJiMWY1ZTU2MzY1MGI3NmQ4NzY4NSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2018-05-10 09:07:12.130466+02
0x3xd6uumwv648u8jlm7vmsqgrmnkn1a	MzEzYjI1MDY4ZjNiNTJjOTVkNTA3ODFjZjFiYTgzYTMzMTY4NTBlNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDNiOGRkNWI0ZDYzYzE5MDBiMmJiMWY1ZTU2MzY1MGI3NmQ4NzY4NSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2018-05-10 11:03:50.113522+02
fa4awrqh5awkpt65wgmdasma156h4hdc	MzEzYjI1MDY4ZjNiNTJjOTVkNTA3ODFjZjFiYTgzYTMzMTY4NTBlNjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiMDNiOGRkNWI0ZDYzYzE5MDBiMmJiMWY1ZTU2MzY1MGI3NmQ4NzY4NSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=	2018-05-10 11:30:47.33069+02
dtp8xjthopd71pjdn5kdig5fn9phnhue	NjRkMDQwOWY1MDQ0NDQ3MjVlMjYzOWIxNzBmOGFiZjM1NzlkNDFlNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjAzYjhkZDViNGQ2M2MxOTAwYjJiYjFmNWU1NjM2NTBiNzZkODc2ODUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2018-08-22 12:23:26.690263+02
yv1e248atlbt256ow7r99qd9zikjrcet	NjRkMDQwOWY1MDQ0NDQ3MjVlMjYzOWIxNzBmOGFiZjM1NzlkNDFlNzp7Il9hdXRoX3VzZXJfaGFzaCI6IjAzYjhkZDViNGQ2M2MxOTAwYjJiYjFmNWU1NjM2NTBiNzZkODc2ODUiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=	2018-08-22 12:33:44.211805+02
gysgt9ncfly680ps4k4vy6fm2lp2hm29	MWE3NzBlNzY0MzVkN2ZkODRkOGE0MzM1ZTFjZTAyYjdmNmFmZGI2Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI5MTM5ZDAyMDU5ZDIyOTExYzQ3OWJiMjU0MjkwMTc1Nzc0YmRhZmM1In0=	2018-09-01 10:21:47.604284+02
\.


--
-- Data for Name: image_data; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.image_data (id, title, short_description, full_description, date_updated, rating, creative, is_publish, img_file_id, api_id, place_id) FROM stdin;
2	\N	\N	\N	2018-04-25 18:23:10.593603+02	\N	f	f	2	\N	\N
3	\N	\N	\N	2018-04-25 18:23:11.469407+02	\N	f	f	3	\N	\N
4	\N	\N	\N	2018-04-25 18:23:12.169249+02	\N	f	f	4	\N	\N
5	\N	\N	\N	2018-04-25 18:23:13.308312+02	\N	f	f	5	\N	\N
6	\N	\N	\N	2018-04-25 18:23:13.421362+02	\N	f	f	6	\N	\N
7	\N	\N	\N	2018-04-25 18:23:14.380775+02	\N	f	f	7	\N	\N
8	\N	\N	\N	2018-04-25 18:23:15.382163+02	\N	f	f	8	\N	\N
9	\N	\N	\N	2018-04-25 18:23:16.087697+02	\N	f	f	9	\N	\N
10	\N	\N	\N	2018-04-25 18:23:17.07417+02	\N	f	f	10	\N	\N
1	pixels photo	city skyline		2018-08-20 16:04:09.764333+02	\N	f	f	1	\N	\N
\.


--
-- Data for Name: image_data_categories; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.image_data_categories (id, imagedata_id, category_id) FROM stdin;
\.


--
-- Name: image_data_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.image_data_categories_id_seq', 1, false);


--
-- Name: image_data_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.image_data_id_seq', 10, true);


--
-- Data for Name: image_data_tags; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.image_data_tags (id, imagedata_id, tag_id) FROM stdin;
\.


--
-- Name: image_data_tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.image_data_tags_id_seq', 1, false);


--
-- Data for Name: image_file; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.image_file (id, file_name, original_name, thumb_name, preview_name, added_date, is_color, orientation, is_new) FROM stdin;
1	pexels-photo-164357.jpeg	original/fonis26b06clm3l9kwob3141fhu3aw.jpeg	thumb/i9f4nev5uexr74jljx9qsjgsk161w5.jpeg	preview/0bvx1qiwc9ti7hmc29pyz1kjsuerhl.jpeg	2018-04-25 18:23:09.36614+02	f	landscape	t
2	pexels-photo-748626.jpeg	original/uaxefmwses46lt8jvef8drsz3y1rcm.jpeg	thumb/8iwj57zox54pzsxuuxmqs6aui3281a.jpeg	preview/mby7as5mz7rg20obbyylw3x6f4nsrt.jpeg	2018-04-25 18:23:10.59153+02	f	landscape	t
3	amazing-animal-beautiful-beautifull.jpg	original/kqgqdejnyep13mdzco70xpxmcam6i5.jpg	thumb/w6jecg53i4uromf57oyqm5e0e9gjuy.jpg	preview/dnil8ywke6wvbv0mnjufy3xkbbqy93.jpg	2018-04-25 18:23:11.46734+02	t	landscape	t
4	pexels-photo-266174.jpeg	original/0rqr2fzgrtb0tng750fgxaw12077h8.jpeg	thumb/6ui3om7uk7rvdtsj0w6oudw7epdv71.jpeg	preview/nxd8uci276ir1a0vsrof74n6g16nr1.jpeg	2018-04-25 18:23:12.167308+02	f	landscape	t
5	pexels-photo.jpg	original/n5fkuix0pnrh5qf402wbchd9ixjpp7.jpg	thumb/o0wyeopnarj7tdhi2hzgcosqn60wgw.jpg	preview/fhetcy20n1vwhc6jgf71coo8leas2l.jpg	2018-04-25 18:23:13.306422+02	t	landscape	t
6	pexels-photo-459225.jpeg	original/l4k1tknuyd3nepbcw8gb9znnx2kw9r.jpeg	thumb/c103fellep1lucgxrv9z59czlsi92k.jpeg	preview/c50y35yl175y0i18n6uderntkqg43d.jpeg	2018-04-25 18:23:13.419449+02	t	landscape	t
7	pexels-photo-133459.jpeg	original/meypq3dt0k90hcif7cn43rq5kr7824.jpeg	thumb/oa7depgxuzalf470kgccg81rk9v5u1.jpeg	preview/v9yl9yd48bdcn3oe215lg5dp3wzhxh.jpeg	2018-04-25 18:23:14.378465+02	t	landscape	t
8	pexels-photo-248347.jpeg	original/ok4n0uctdt8fin3jnum8iv8vi8do2z.jpeg	thumb/gr456qxmeejygg7iedxivanntld95l.jpeg	preview/j9xbf907w3p8axtiprwwpf2387ruuw.jpeg	2018-04-25 18:23:15.375926+02	f	landscape	t
9	pexels-photo-248797.jpeg	original/fth6odzbxpn82bmea9p8ez7xfqpg3z.jpeg	thumb/yymm4fg2n6wuqw1sp8i0clnfv95d37.jpeg	preview/gjc9uko4yn2yxsufa76ujm6gnn8sss.jpeg	2018-04-25 18:23:16.085845+02	t	landscape	t
10	pexels-photo-145939.jpeg	original/5xxca08coaykwp9yrbc9kq9j59bq24.jpeg	thumb/iqhwhfnlhs46bj6rh67hgkhsfebjfy.jpeg	preview/6yhfon7hgs2tjj65k5px7rx9i2izx7.jpeg	2018-04-25 18:23:17.072237+02	t	landscape	t
\.


--
-- Name: image_file_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.image_file_id_seq', 10, true);


--
-- Data for Name: places; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.places (id, name) FROM stdin;
\.


--
-- Name: places_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.places_id_seq', 1, false);


--
-- Data for Name: tags; Type: TABLE DATA; Schema: public; Owner: pmdbuser
--

COPY public.tags (id, name, weight) FROM stdin;
\.


--
-- Name: tags_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pmdbuser
--

SELECT pg_catalog.setval('public.tags_id_seq', 1, false);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (id);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: image_data image_data_api_id_key; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data
    ADD CONSTRAINT image_data_api_id_key UNIQUE (api_id);


--
-- Name: image_data_categories image_data_categories_imagedata_id_category_id_2153e6cb_uniq; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data_categories
    ADD CONSTRAINT image_data_categories_imagedata_id_category_id_2153e6cb_uniq UNIQUE (imagedata_id, category_id);


--
-- Name: image_data_categories image_data_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data_categories
    ADD CONSTRAINT image_data_categories_pkey PRIMARY KEY (id);


--
-- Name: image_data image_data_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data
    ADD CONSTRAINT image_data_pkey PRIMARY KEY (id);


--
-- Name: image_data_tags image_data_tags_imagedata_id_tag_id_aac14744_uniq; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data_tags
    ADD CONSTRAINT image_data_tags_imagedata_id_tag_id_aac14744_uniq UNIQUE (imagedata_id, tag_id);


--
-- Name: image_data_tags image_data_tags_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data_tags
    ADD CONSTRAINT image_data_tags_pkey PRIMARY KEY (id);


--
-- Name: image_file image_files_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_file
    ADD CONSTRAINT image_files_pkey PRIMARY KEY (id);


--
-- Name: places places_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.places
    ADD CONSTRAINT places_pkey PRIMARY KEY (id);


--
-- Name: tags tags_pkey; Type: CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: image_data_api_id_fde1fc74_like; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX image_data_api_id_fde1fc74_like ON public.image_data USING btree (api_id varchar_pattern_ops);


--
-- Name: image_data_categories_category_id_d3f000f4; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX image_data_categories_category_id_d3f000f4 ON public.image_data_categories USING btree (category_id);


--
-- Name: image_data_categories_imagedata_id_fd8e0b7d; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX image_data_categories_imagedata_id_fd8e0b7d ON public.image_data_categories USING btree (imagedata_id);


--
-- Name: image_data_img_file_id_9e7a37aa; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX image_data_img_file_id_9e7a37aa ON public.image_data USING btree (img_file_id);


--
-- Name: image_data_place_id_fced2c0d; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX image_data_place_id_fced2c0d ON public.image_data USING btree (place_id);


--
-- Name: image_data_tags_imagedata_id_4f69a288; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX image_data_tags_imagedata_id_4f69a288 ON public.image_data_tags USING btree (imagedata_id);


--
-- Name: image_data_tags_tag_id_61ae8589; Type: INDEX; Schema: public; Owner: pmdbuser
--

CREATE INDEX image_data_tags_tag_id_61ae8589 ON public.image_data_tags USING btree (tag_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: image_data_categories image_data_categories_category_id_d3f000f4_fk_categories_id; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data_categories
    ADD CONSTRAINT image_data_categories_category_id_d3f000f4_fk_categories_id FOREIGN KEY (category_id) REFERENCES public.categories(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: image_data_categories image_data_categories_imagedata_id_fd8e0b7d_fk_image_data_id; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data_categories
    ADD CONSTRAINT image_data_categories_imagedata_id_fd8e0b7d_fk_image_data_id FOREIGN KEY (imagedata_id) REFERENCES public.image_data(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: image_data image_data_img_file_id_9e7a37aa_fk_image_files_id; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data
    ADD CONSTRAINT image_data_img_file_id_9e7a37aa_fk_image_files_id FOREIGN KEY (img_file_id) REFERENCES public.image_file(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: image_data image_data_place_id_fced2c0d_fk_places_id; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data
    ADD CONSTRAINT image_data_place_id_fced2c0d_fk_places_id FOREIGN KEY (place_id) REFERENCES public.places(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: image_data_tags image_data_tags_imagedata_id_4f69a288_fk_image_data_id; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data_tags
    ADD CONSTRAINT image_data_tags_imagedata_id_4f69a288_fk_image_data_id FOREIGN KEY (imagedata_id) REFERENCES public.image_data(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: image_data_tags image_data_tags_tag_id_61ae8589_fk_tags_id; Type: FK CONSTRAINT; Schema: public; Owner: pmdbuser
--

ALTER TABLE ONLY public.image_data_tags
    ADD CONSTRAINT image_data_tags_tag_id_61ae8589_fk_tags_id FOREIGN KEY (tag_id) REFERENCES public.tags(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

