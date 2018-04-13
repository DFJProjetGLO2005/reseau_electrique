SELECT "Creation des index..." as "";

CREATE INDEX LignesP1
USING HASH
ON Lignes(Poste1);


CREATE INDEX LignesP2
USING HASH
ON Lignes(Poste2);

CREATE INDEX AbbRac
USING HASH
ON Abonnes(PointDeRaccordement);


CREATE INDEX villeMeteo
USING HASH
ON ConditionsMeteorologiques(Ville);


CREATE INDEX EidPostes
USING HASH
ON Postes (Eid);

CREATE INDEX EidLignes
USING HASH
ON Lignes (Eid);


# Liste Villes
CREATE INDEX NomVilles
USING HASH
ON Villes (Nom);

CREATE INDEX RacAbonnes
USING HASH
ON Abonnes (PointDeRaccordement);

CREATE INDEX AidConso
USING HASH
ON ConsommationsMensuelles (Aid);

CREATE INDEX EidPostes
USING BTREE
ON Postes (Eid);
