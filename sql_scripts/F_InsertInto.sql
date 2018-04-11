delimiter //

LOAD DATA LOCAL INFILE "../csv_files/ABONNES.csv"
INTO TABLE Abonnes
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Aid, Nom, Telephone, PointDeRaccordement)//

LOAD DATA LOCAL INFILE "../csv_files/CONSOMMATIONSMENSUELLES.csv"
INTO TABLE ConsommationsMensuelles
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Aid, @m, Puissance)
SET Mois = STR_TO_DATE(@m, '%Y-%m-%d %H:%i:%s')//

LOAD DATA LOCAL INFILE "../csv_files/EQUIPEMENTS.csv"
INTO TABLE Equipements
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid)//

LOAD DATA LOCAL INFILE "../csv_files/CENTRALES.csv"
INTO TABLE Centrales
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, PosteSource, Categorie, Puissance)//


LOAD DATA LOCAL INFILE "../csv_files/LIGNES.csv"
INTO TABLE Lignes
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, Tension, Courant, Longueur, Poste1, Poste2, Categorie)//


LOAD DATA LOCAL INFILE "../csv_files/SUPPORTS.csv"
INTO TABLE Supports
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, Ligne, @l, Categorie)
SET Lieu = POLYGONFromText(@l)//


LOAD DATA LOCAL INFILE "../csv_files/CATEGORIESDESUPPORTS.csv"
INTO TABLE CategoriesDeSupports
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Categorie, Portee, Poids, Hauteur)//


LOAD DATA LOCAL INFILE "../csv_files/POSTES.csv"
INTO TABLE Postes
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, @l)
SET Lieu = POLYGONFromText(@l)//


LOAD DATA LOCAL INFILE "../csv_files/SOURCES.csv"
INTO TABLE Sources
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, Centrale)//

LOAD DATA LOCAL INFILE "../csv_files/POINTSRACCORDEMENT.csv"
INTO TABLE PointsDeRaccordement
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, Abonne)//

LOAD DATA LOCAL INFILE "../csv_files/SATELLITES.csv"
INTO TABLE Satellites
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid)//

LOAD DATA LOCAL INFILE "../csv_files/STRATEGIQUES.csv"
INTO TABLE Strategiques
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid)//

LOAD DATA LOCAL INFILE "../csv_files/TRANSFORMATEURS.csv"
INTO TABLE TransformateursSurPoteauDeBois
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid)//

LOAD DATA LOCAL INFILE "../csv_files/BRIS.csv"
INTO TABLE Bris
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Eid, @d, @f)
SET  Debut = STR_TO_DATE(@d, '%Y-%m-%d %H:%i:%s'),
     Fin = STR_TO_DATE(@f, '%Y-%m-%d %H:%i:%s')//



LOAD DATA LOCAL INFILE "../csv_files/VILLES.csv"
INTO TABLE Villes
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Nom, @l)
SET Lieu = POLYGONFromText(@l)//


LOAD DATA LOCAL INFILE "../csv_files/CONDITIONSMETEOROLOGIQUES.csv"
INTO TABLE ConditionsMeteorologiques
FIELDS TERMINATED BY ','
OPTIONALLY ENCLOSED BY '"'
(Ville, @h, Temperature, Humidite, PressionAtmospherique, ChuteDePluie, ChuteDeNeige, CouvertureDeNeige)
SET Heure = STR_TO_DATE(@h, '%Y-%m-%d %H:%i:%s')//


delimiter ;
