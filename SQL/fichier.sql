
CREATE TABLE elevesNSI (
  id INTEGER PRIMARY KEY,
  moisNais INTEGER,
  name TEXT NOT NULL,
  prenom TEXT NOT NULL,
  gender TEXT NOT NULL
);

CREATE TABLE mois (
    idMois INTEGER PRIMARY KEY,
    fr VARCHAR(10),
    en VARCHAR(10)
);

-- insert some values
INSERT INTO elevesNSI(moisNais, gender, name, id, prenom) VALUES (NULL, 'M', 'ALLI', 1, 'Zephir');
INSERT INTO elevesNSI VALUES (2, 3, 'BAR', 'Jules', 'M');
INSERT INTO elevesNSI VALUES (3, 11, 'BENARDE', 'Quentin', 'M');
insert into elevesNSI values (4, 2, 'BUKOV', 'Noa', 'M');
insert into elevesNSI values (5, 4, 'GABORIE', 'Cesar', 'M');
insert into elevesNSI values (6, 5, 'VIGNE', 'Noe', 'M');
insert into elevesNSI values (7, 7, 'VER', 'Salif', 'M');
insert into elevesNSI values (8, 4, 'SALOU', 'Clément', 'M');
insert into elevesNSI values (9, 10, 'LE GUYAD', 'Nattan', 'M');
insert into elevesNSI values (10, 6, 'RADOU', 'Youssef', 'M');
insert into elevesNSI values (11, 2, 'PROUTIE', 'Ethan', 'M');
insert into elevesNSI values (12, 9, 'MARTIN', 'Enzo', 'M');
insert into elevesNSI values (13, 6, 'MICET', 'Thibaut', 'M');
insert into elevesNSI values (14, 10, 'GUENGA', 'Noé', 'M');
insert into elevesNSI values (15, 5, 'GUIBAU', 'Ethan', 'M');
insert into elevesNSI values (16, 3, 'HAMA', 'Louis', 'M');

INSERT INTO mois VALUES (1, 'janvier', 'january');
INSERT INTO mois VALUES (2, 'février', 'february');
INSERT INTO mois VALUES (3, 'mars', 'march');
INSERT INTO mois VALUES (4, 'avril', 'april');
INSERT INTO mois VALUES (5, 'mai', 'may');
INSERT INTO mois VALUES (6, 'juin', 'june');
INSERT INTO mois VALUES (7, 'juillet', 'july');
INSERT INTO mois VALUES (8, 'août', 'august');
INSERT INTO mois VALUES (9, 'septembre', 'september');
INSERT INTO mois VALUES (10, 'octobre', 'october');
INSERT INTO mois VALUES (11, 'novembre', 'november');
INSERT INTO mois VALUES (12, 'décembre', 'december');



-- fetch some values
select * from mois natural join elevesNSI;
