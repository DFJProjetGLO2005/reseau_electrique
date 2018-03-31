ALTER TABLE Abonnes
ADD PRIMARY KEY (Aid);

ALTER TABLE ConsommationsMensuelles
ADD PRIMARY KEY (Aid, Mois);



ALTER TABLE Equipements
ADD PRIMARY KEY (Eid);

ALTER TABLE Centrales
ADD PRIMARY KEY (Eid);

ALTER TABLE Lignes
ADD PRIMARY KEY (Eid);

ALTER TABLE Supports
ADD PRIMARY KEY (Eid);

ALTER TABLE CategoriesDeSupports
ADD PRIMARY KEY (Categorie);

ALTER TABLE Postes
ADD PRIMARY KEY (Eid);

ALTER TABLE Sources
ADD PRIMARY KEY (Eid);

ALTER TABLE PointsDeRaccordement
ADD PRIMARY KEY (Eid);

ALTER TABLE Satellites
ADD PRIMARY KEY (Eid);

ALTER TABLE TransformateursSurPoteauDeBois
ADD PRIMARY KEY (Eid);

ALTER TABLE Bris
ADD PRIMARY KEY (Eid, Debut);


ALTER TABLE ConditionsMeteorologiques
ADD PRIMARY KEY (Ville, Heure);

ALTER TABLE Villes
ADD PRIMARY KEY (Nom);
