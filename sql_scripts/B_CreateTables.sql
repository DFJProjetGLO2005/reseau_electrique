CREATE TABLE Abonnes
(
    Aid INT,
    Nom CHAR(20),
    Age INT,
    Telephone CHAR(8),
    PointDeRaccordement INT
);

CREATE TABLE ConsommationsMensuelles
(
    Aid INT,
    Mois TIMESTAMP,
    Puissance INT
);




CREATE TABLE Equipements(Eid CHAR(9));

CREATE TABLE Centrales
(
    Eid CHAR(9),
    PosteSource CHAR(9),
    Puissance INT,
    Categorie ENUM('Parc éolien',
                   'Centrale thermique',
                   'Centrale hydroélectrique',
                   'Centrale solaire photovoltaïque')
);

CREATE TABLE Lignes
(
    Eid CHAR(9),
    Tension INT,
    Courant INT,
    Longueur INT,
    Poste1 CHAR(9),
    Poste2 CHAR(9),
    Categorie ENUM('Câble conducteur',
                   'Câble de garde',
                   'Hauban')
);

CREATE TABLE Supports
(
    Eid CHAR(9),
    Ligne CHAR(9),
    Courant INT,
    Lieu GEOMETRY,
    Categorie ENUM('Sous-terrain',
                   'Pylône Mae West',
                   'Pylône Classique',
                   'Pylône Haubané en V',
                   'Pylône Tubulaire',
                   'Pylône Haubané à chaînette',
                   'Pylône de traversée',
                   'Pylône à treillis',
                   'Poteau de bois')
);


CREATE TABLE CategoriesDeSupports
(
    Categorie ENUM('Sous-terrain',
                   'Pylône Mae West',
                   'Pylône Classique',
                   'Pylône Haubané en V',
                   'Pylône Tubulaire',
                   'Pylône Haubané à chaînette',
                   'Pylône de traversée',
                   'Pylône à treillis',
                   'Poteau de bois'),
    Portee INT,
    Poids INT,
    Hauteur INT
);


CREATE TABLE Postes (
    Eid CHAR(9),
    Lieu GEOMETRY
);

CREATE TABLE Sources(
    Eid CHAR(9),
    Centrale CHAR(9)
);

CREATE TABLE PointsDeRaccordement(
    Eid CHAR(9),
    Abonne INT
);

CREATE TABLE Satellites(
    Eid CHAR(9)
);

CREATE TABLE Strategiques(
    Eid CHAR(9)
);

CREATE TABLE TransformateursSurPoteauDeBois(
    Eid CHAR(9)
);

CREATE TABLE Bris (
    Eid CHAR(9),
    Debut TIMESTAMP,
    Fin TIMESTAMP
); 



CREATE TABLE Villes
(
    Nom CHAR(35),
    Lieu GEOMETRY
);

CREATE TABLE ConditionsMeteorologiques
( 
    Ville CHAR(35),
    Heure TIMESTAMP,
    Humidite REAL,
    PressionAtmospherique REAL,
    ChuteDePluie INT,
    ChuteDeNeige INT,
    CouvertureDeNeige INT
);
