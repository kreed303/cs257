--
-- PostgreSQL database dump
--

-- Dumped from database version 17.4
-- Dumped by pg_dump version 17.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: albums; Type: TABLE; Schema: public; Owner: sam
--

CREATE TABLE public.albums (
    albumid integer NOT NULL,
    albumname text,
    albumyear integer
);


ALTER TABLE public.albums OWNER TO sam;

--
-- Name: albumssongs; Type: TABLE; Schema: public; Owner: sam
--

CREATE TABLE public.albumssongs (
    albumid integer NOT NULL,
    songid integer NOT NULL
);


ALTER TABLE public.albumssongs OWNER TO sam;

--
-- Name: artists; Type: TABLE; Schema: public; Owner: sam
--

CREATE TABLE public.artists (
    artistid integer NOT NULL,
    artistname text
);


ALTER TABLE public.artists OWNER TO sam;

--
-- Name: artistsalbums; Type: TABLE; Schema: public; Owner: sam
--

CREATE TABLE public.artistsalbums (
    artistid integer NOT NULL,
    albumid integer NOT NULL
);


ALTER TABLE public.artistsalbums OWNER TO sam;

--
-- Name: artistssongs; Type: TABLE; Schema: public; Owner: sam
--

CREATE TABLE public.artistssongs (
    artistid integer NOT NULL,
    songid integer NOT NULL
);


ALTER TABLE public.artistssongs OWNER TO sam;

--
-- Name: songs; Type: TABLE; Schema: public; Owner: sam
--

CREATE TABLE public.songs (
    songid integer NOT NULL,
    songname text,
    tracknumber integer,
    songlength integer,
    songbpm integer
);


ALTER TABLE public.songs OWNER TO sam;

--
-- Data for Name: albums; Type: TABLE DATA; Schema: public; Owner: sam
--

COPY public.albums (albumid, albumname, albumyear) FROM stdin;
0	Gold - Greatest Hits	1993
1	The Definitive Collection Disc 1	2001
2	The Definitive Collection Disc 2	2001
3	Cordial	2001
4	En Spectacle	2006
5	So Beautiful or So What	2011
6	Graceland	1986
7	There Goes Rhymin' Simon [Bonus Tracks]	2004
\.


--
-- Data for Name: albumssongs; Type: TABLE DATA; Schema: public; Owner: sam
--

COPY public.albumssongs (albumid, songid) FROM stdin;
1	1
1	2
1	3
1	4
1	5
1	6
1	7
1	8
1	9
1	10
1	11
1	12
1	13
1	14
1	15
1	16
1	17
1	18
1	19
2	20
2	21
2	22
2	23
2	24
2	25
2	26
2	27
2	28
2	29
2	30
2	31
2	32
2	33
2	34
2	35
2	36
2	37
2	38
2	39
3	40
3	41
3	42
3	43
3	44
3	45
3	46
3	47
3	48
3	49
3	50
3	51
3	52
3	53
3	54
3	55
3	56
4	57
4	58
4	59
4	60
4	61
4	62
4	63
4	64
4	65
4	66
4	67
4	68
4	69
4	70
4	71
4	72
5	73
5	74
5	75
5	76
5	77
5	78
5	79
5	80
5	81
5	82
5	83
5	84
5	85
5	86
5	87
5	88
6	89
6	90
6	91
6	92
6	93
6	94
6	95
6	96
6	97
6	98
7	99
7	100
7	101
7	102
7	103
7	104
7	105
7	106
7	107
7	108
7	109
7	110
7	111
7	112
7	113
8	114
8	115
8	116
8	117
8	118
8	119
8	120
8	121
8	122
8	123
8	124
8	125
8	126
8	127
\.


--
-- Data for Name: artists; Type: TABLE DATA; Schema: public; Owner: sam
--

COPY public.artists (artistid, artistname) FROM stdin;
0	ABBA
1	La Bottine Souriante
2	Paul Simon
\.


--
-- Data for Name: artistsalbums; Type: TABLE DATA; Schema: public; Owner: sam
--

COPY public.artistsalbums (artistid, albumid) FROM stdin;
1	1
1	2
1	3
1	4
1	5
1	6
1	7
1	8
1	9
1	10
1	11
1	12
1	13
1	14
1	15
1	16
1	17
1	18
1	19
1	20
1	21
1	22
1	23
1	24
1	25
1	26
1	27
1	28
1	29
1	30
1	31
1	32
1	33
1	34
1	35
1	36
1	37
1	38
1	39
1	40
1	41
1	42
1	43
1	44
1	45
1	46
1	47
1	48
1	49
1	50
1	51
1	52
1	53
1	54
1	55
1	56
2	57
2	58
2	59
2	60
2	61
2	62
2	63
2	64
2	65
2	66
2	67
2	68
2	69
2	70
2	71
2	72
2	73
2	74
2	75
2	76
2	77
2	78
2	79
2	80
2	81
2	82
2	83
2	84
2	85
2	86
2	87
2	88
3	89
3	90
3	91
3	92
3	93
3	94
3	95
3	96
3	97
3	98
3	99
3	100
3	101
3	102
3	103
3	104
3	105
3	106
3	107
3	108
3	109
3	110
3	111
3	112
3	113
3	114
3	115
3	116
3	117
3	118
3	119
3	120
3	121
3	122
3	123
3	124
3	125
3	126
3	127
0	0
0	0
0	1
0	2
1	3
1	4
2	5
2	6
2	7
0	0
0	0
0	1
0	2
1	3
1	4
2	5
2	6
2	7
\.


--
-- Data for Name: artistssongs; Type: TABLE DATA; Schema: public; Owner: sam
--

COPY public.artistssongs (artistid, songid) FROM stdin;
0	1
0	2
0	3
0	4
0	5
0	6
0	7
0	8
0	9
0	10
0	11
0	12
0	13
0	14
0	15
0	16
0	17
0	18
0	19
0	20
0	21
0	22
0	23
0	24
0	25
0	26
0	27
0	28
0	29
0	30
0	31
0	32
0	33
0	34
0	35
0	36
0	37
0	38
0	39
0	40
0	41
0	42
0	43
0	44
0	45
0	46
0	47
0	48
0	49
0	50
0	51
0	52
0	53
0	54
0	55
0	56
1	57
1	58
1	59
1	60
1	61
1	62
1	63
1	64
1	65
1	66
1	67
1	68
1	69
1	70
1	71
1	72
1	73
1	74
1	75
1	76
1	77
1	78
1	79
1	80
1	81
1	82
1	83
1	84
1	85
1	86
1	87
1	88
2	89
2	90
2	91
2	92
2	93
2	94
2	95
2	96
2	97
2	98
2	99
2	100
2	101
2	102
2	103
2	104
2	105
2	106
2	107
2	108
2	109
2	110
2	111
2	112
2	113
2	114
2	115
2	116
2	117
2	118
2	119
2	120
2	121
2	122
2	123
2	124
2	125
2	126
2	127
\.


--
-- Data for Name: songs; Type: TABLE DATA; Schema: public; Owner: sam
--

COPY public.songs (songid, songname, tracknumber, songlength, songbpm) FROM stdin;
0	Take a Chance on Me	3	244466	0
1	I Have a Dream	7	284066	0
2	S.O.S.	10	201440	0
3	Knowing Me, Knowing You	2	242240	0
4	Super Trouper	6	254266	0
5	Mamma Mia	4	213493	0
6	The Name of the Game	17	240000	0
7	The Winner Takes It All	8	295533	0
8	Does Your Mother Know	15	195266	0
9	Dancing Queen	1	232200	0
10	Waterloo	19	162960	0
11	Gimme! Gimme! Gimme! (A Man After Midnight)	14	288800	0
12	Chiquitita	11	326266	0
13	Voulez-Vous	13	262466	0
14	One of Us	16	238040	0
15	Lay All Your Love on Me	5	274333	0
16	Money, Money, Money	9	188333	0
17	Fernando	12	253626	0
18	Thank You for the Music	18	231493	0
19	Does Your Mother Know	20	193480	0
20	Take a Chance on Me	16	245666	0
21	So Long	7	185693	0
22	S.O.S.	9	200493	0
23	Love Isn't Easy (But It Sure Is Hard Enough)	4	173933	0
24	Mamma Mia	10	212200	0
25	Knowing Me, Knowing You	14	241733	0
26	Dancing Queen	12	231666	0
27	Ring Ring	3	184693	0
28	Chiquitita	19	324573	0
29	Eagle	17	267333	0
30	People Need Love	1	165066	0
31	Fernando	11	254000	0
32	Waterloo	5	167000	0
33	Summer Night City	18	215893	0
34	Honey, Honey	6	175533	0
35	The Name of the Game	15	292240	0
36	Money, Money, Money	13	185800	0
37	He Is Your Brother	2	198440	0
38	I Do, I Do, I Do, I Do, I Do	8	196946	0
39	One of Us	9	236640	0
40	On and on and On	7	222506	0
41	The Visitors (Crackin' Up)	12	346626	0
42	Voulez-Vous	1	308373	0
43	Super Trouper	6	253360	0
44	Head Over Heels	11	227640	0
45	Lay All Your Love on Me	8	274626	0
46	I Have a Dream	4	282760	0
47	The Day Before You Came	13	351266	0
48	The Winner Takes It All	5	296373	0
49	Ring Ring [1974 Remix]	16	190400	0
50	Voulez-Vous [Extended Remix]	17	367880	0
51	When All Is Said and Done	10	197760	0
52	Under Attack	14	227866	0
53	Angeleyes	2	259933	0
54	Gimme! Gimme! Gimme! (A Man After Midnight)	3	290600	0
55	Thank You for the Music	15	231773	0
56	Ma Paillasse (My Straw Mat)	13	184666	0
57	En P'tit Boggie (Giddy Up)	5	163240	0
58	Suède Inn	8	190506	0
59	Lune de Miel (Honeymoon)	7	224400	0
60	Et Boucle La Bottine (And "Loop" La Bottine)	16	442426	0
61	Reel de Baie St-Paul (Baie St-Paul's Reel)	15	341066	0
62	Set à Ubert (Ubert's Set)	4	210960	0
63	Aimé	6	221626	0
64	Chant de La Luette (The Worbler's Song)	14	175293	0
65	Les Noces d'Or (Golden Wedding Reel)	11	137106	0
66	Le Démon Sort de l'Enfer (The Devil Comes out of Hell)	3	273706	0
67	Dans Paris Y'a T'Une Brune (The Brunette from Paris)	1	191026	0
68	La Grandeuse (The Grumbling Woman)	2	244133	0
69	A Bas Les Rideaux (Out with the Lies)	10	232493	0
70	Viens-Tu Prendre une Bière? (Come Have a Beer!)	12	154533	0
71	J'Ai Fait une Maîtresse (I Got Me a Mistress)	9	156800	0
72	Le Lanlire (La Poule à Colin)	11	301626	0
73	La Grand Côte	15	438800	0
74	Sur La Route (La Tapinie)	2	231200	0
75	À Travers La Vitre	12	236573	0
76	Suite de La Sauvagesse	3	303693	0
77	Le Voyage de Basile	5	264773	0
78	Le Rêve Musiçal (Le Rêve du Quéteux Tremblay)	8	187333	0
79	La Chanson de l'Ivrogne	13	255066	0
80	Ouverture	1	489600	0
81	Chapeau	6	329600	0
82	Galoppe et Quadrille	10	231000	0
83	Son P'tit Bidoulidou	16	95893	0
84	Virginie Adieu	7	113200	0
85	La Cuisinière	14	266160	0
86	Ch'pas Capable (La Montagne du Loup)	4	247400	0
87	Un Coup Madame	9	273866	0
88	Rewrite	4	229720	0
89	The Afterlife	2	220173	0
90	Amulet	7	96573	0
91	Getting Ready for Christmas Day	1	246720	0
92	Dazzling Blue	3	272320	0
93	Questions for the Angels	8	229906	0
94	Love Is Eternal Sacred Light	6	242160	0
95	So Beautiful or So What	10	248560	0
96	Love and Hard Times	5	249480	0
97	Love & Blessings	9	258160	0
98	All Around The World Or The Myths Of Fingerprints (Early Version)	14	198560	0
99	Diamonds On The Soles Of Her Shoes (Alternate Versioin)	13	281413	0
100	The Story Of "Graceland"	15	578960	0
101	Graceland	2	291200	0
102	Homeless	8	228413	0
103	Diamonds On The Soles Of Her Shoes	5	351346	0
104	Crazy Love, Vol. II	9	259360	0
105	Under African Skies	7	217160	0
106	You Can Call Me Al	6	280586	0
107	Homeless (Demo)	12	150546	0
108	All Around The World Or The Myth Of Fingerprints	11	198426	0
109	Gumboots	4	164826	0
110	I Know What I Know	3	193373	0
111	The Boy in the Bubble	1	239693	0
112	That Was Your Mother	10	172813	0
113	Was a Sunny Day	7	224320	0
114	Loves Me Like a Rock	10	220426	0
115	Tenderness	2	175506	0
116	One Man's Ceiling Is Another Man's Floor	5	228146	0
117	St. Judy's Comet	9	201640	0
118	Loves Me Like a Rock [Acoustic Demo][#][*]	14	204680	0
119	American Tune	6	227120	0
120	American Tune [Unfinished Demo][#][*]	13	243173	0
121	Take Me to the Mardi Gras [Acoustic Demo][#][*]	12	151106	0
122	Take Me to the Mardi Gras	3	210853	0
123	Learn How to Fall	8	167626	0
124	Something So Right	4	276826	0
125	Kodachrome	1	215400	0
126	Let Me Live in Your City [Work-In-Progress][#][*]	11	261973	0
\.


--
-- PostgreSQL database dump complete
--

