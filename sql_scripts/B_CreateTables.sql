CREATE TABLE Abonnes
(
    Aid INT,
    Nom CHAR(20),
    Telephone CHAR(8),
    PointDeRaccordement CHAR(9)
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
    Categorie ENUM('PARC EOLIEN',
                   'CENTRALE THERMIQUE',
                   'CENTRALE HYDROELECTRIQUE',
                   'CENTRALE SOLAIRE PHOTOVOLTAIQUE'),
    Puissance INT
);

CREATE TABLE Lignes
(
    Eid CHAR(9),
    Tension INT,
    Courant INT,
    Longueur INT,
    Poste1 CHAR(9),
    Poste2 CHAR(9),
    Categorie ENUM('CABLE CONDUCTEUR',
                   'CABLE DE GARDE',
                   'HAUBAN')
);

CREATE TABLE Supports
(
    Eid CHAR(9),
    Ligne CHAR(9),
    Lieu GEOMETRY,
    Categorie ENUM('SOUS-TERRAIN',
                   'PYLONE MAE WEST',
                   'PYLONE CLASSIQUE',
                   'PYLONE HAUBANE EN V',
                   'PYLONE TUBULAIRE',
                   'PYLONE HAUBANE A CHAINETTE',
                   'PYLONE DE TRAVERSEE',
                   'PYLONE A TREILLIS',
                   'POTEAU DE BOIS')
);


CREATE TABLE CategoriesDeSupports
(
    Categorie ENUM('SOUS-TERRAIN',
                   'PYLONE MAE WEST',
                   'PYLONE CLASSIQUE',
                   'PYLONE HAUBANE EN V',
                   'PYLONE TUBULAIRE',
                   'PYLONE HAUBANE A CHAINETTE',
                   'PYLONE DE TRAVERSEE',
                   'PYLONE A TREILLIS',
                   'POTEAU DE BOIS'),
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
    Fin TIMESTAMP NULL
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
