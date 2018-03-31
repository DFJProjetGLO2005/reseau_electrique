LOAD DATA LOCAL INFILE "../csv_files/ABONNES.csv"
INTO TABLE Abonnes
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Aid, Nom, Age, Telephone, PointDeRaccordement);

LOAD DATA LOCAL INFILE "../csv_files/CONSOMMATIONSMENSUELLES.csv"
INTO TABLE ConsommationsMensuelles
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Aid, Mois, Puissance);

LOAD DATA LOCAL INFILE "../csv_files/EQUIPEMENTS.csv"
INTO TABLE Equipements
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid);

LOAD DATA LOCAL INFILE "../csv_files/CENTRALES.csv"
INTO TABLE Centrales
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, PosteSource, Puissance, Categorie);


LOAD DATA LOCAL INFILE "../csv_files/LIGNES.csv"
INTO TABLE Lignes
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, Tension, Courant, Longueur, Poste1, Poste2);

###################################################
###################################################
## DIVISER SUPPORTS ET CATEGORIES DE SUPPORTS #####
#LOAD DATA LOCAL INFILE "../csv_files/SUPPORTS.csv"
#INTO TABLE Supports
#FIELDS TERMINATED BY ','
#OPTIONALLY ENCLOSED BY '"'
#(Eid, Ligne, Courant, Lieu, Categorie);


DROP TABLE IF EXISTS TempPostes;
CREATE TABLE TempPostes (Eid CHAR(9), Lieu CHAR(255));
LOAD DATA LOCAL INFILE "../csv_files/POSTES.csv"
INTO TABLE TempPostes
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, Lieu);
INSERT INTO Postes (Eid, Lieu)
SELECT T.Eid, POLYGONFromText(T.Lieu) FROM TempPostes T;
DROP TABLE TempPostes;


LOAD DATA LOCAL INFILE "../csv_files/SOURCES.csv"
INTO TABLE Sources
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, Centrale);

LOAD DATA LOCAL INFILE "../csv_files/POINTSRACCORDEMENT.csv"
INTO TABLE PointsDeRaccordement
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, Abonne);

LOAD DATA LOCAL INFILE "../csv_files/SATELLITES.csv"
INTO TABLE Satellites
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid);

LOAD DATA LOCAL INFILE "../csv_files/STRATEGIQUES.csv"
INTO TABLE Strategiques
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid);

LOAD DATA LOCAL INFILE "../csv_files/TRANSFORMATEURS.csv"
INTO TABLE TransformateursSurPoteauDeBois
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid);

LOAD DATA LOCAL INFILE "../csv_files/BRIS.csv"
INTO TABLE Bris
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, Debut, Fin);

DROP TABLE IF EXISTS TempVilles;
CREATE TABLE TempVilles (Nom CHAR(35), Lieu CHAR(255));
LOAD DATA LOCAL INFILE "../csv_files/VILLES.csv"
INTO TABLE TempVilles
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Nom, Lieu);
INSERT INTO Villes (Nom, Lieu)
SELECT T.Nom, POLYGONFromText(T.Lieu) FROM TempVilles T;
DROP TABLE TempVilles;


LOAD DATA LOCAL INFILE "../csv_files/CONDITIONSMETEOROLOGIQUES.csv"
INTO TABLE ConditionsMeteorologiques
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Ville, Heure, Humidite, PressionAtmospherique, ChuteDePluie, ChuteDeNeige, CouvertureDeNeige);

