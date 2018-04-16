SELECT "Creation des index..." as "";

CREATE INDEX LignesP1
USING HASH
ON Lignes(Poste1);

CREATE INDEX AbbRac
USING HASH
ON Abonnes(PointDeRaccordement);

CREATE INDEX villeMeteo
USING HASH
ON ConditionsMeteorologiques(Ville);

CREATE INDEX NomVilles
USING HASH
ON Villes (Nom);

CREATE INDEX EidLignes
USING HASH
ON Lignes (Eid);

CREATE INDEX EidPostes
USING BTREE
ON Postes (Eid);

CREATE INDEX AidConso
USING HASH
ON ConsommationsMensuelles (Aid);


