SELECT "Assignation des cles etrangeres" as "";

ALTER TABLE Abonnes
ADD FOREIGN KEY (PointDeRaccordement) REFERENCES PointsDeRaccordement (Eid);

ALTER TABLE ConsommationsMensuelles
ADD FOREIGN KEY (Aid) REFERENCES Abonnes(Aid);



ALTER TABLE Centrales
ADD FOREIGN KEY (Eid) REFERENCES Equipements(Eid),
ADD FOREIGN KEY (PosteSource) REFERENCES Sources(Eid);

ALTER TABLE Lignes
ADD FOREIGN KEY (Eid) REFERENCES Equipements(Eid),
ADD FOREIGN KEY (Poste1) REFERENCES Postes(Eid),
ADD FOREIGN KEY (Poste2) REFERENCES Postes(Eid);

ALTER TABLE Supports
ADD FOREIGN KEY (Eid) REFERENCES Equipements(Eid),
ADD FOREIGN KEY (Ligne) REFERENCES Lignes(Eid),
ADD FOREIGN KEY (Categorie) REFERENCES CategoriesDeSupports(Categorie);

ALTER TABLE Sources
ADD FOREIGN KEY (Eid) REFERENCES Postes(Eid),
ADD FOREIGN KEY (Centrale) REFERENCES Centrales (Eid);

ALTER TABLE Postes
ADD FOREIGN KEY (Eid) REFERENCES Equipements(Eid);

ALTER TABLE PointsDeRaccordement
ADD FOREIGN KEY (Eid) REFERENCES Postes(Eid),
ADD FOREIGN KEY (Abonne) REFERENCES Abonnes(Aid);

ALTER TABLE Satellites
ADD FOREIGN KEY (Eid) REFERENCES Postes(Eid);

ALTER TABLE TransformateursSurPoteauDeBois
ADD FOREIGN KEY (Eid) REFERENCES Postes(Eid);

ALTER TABLE Bris
ADD FOREIGN KEY (Eid) REFERENCES Equipements(Eid);

ALTER TABLE ConditionsMeteorologiques
ADD FOREIGN KEY (Ville) REFERENCES Villes(Nom);
