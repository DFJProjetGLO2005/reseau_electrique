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

#CREATE INDEX EidSources
#USING HASH
#ON Sources (Eid);
#
#CREATE INDEX EidPointsDeRaccordement
#USING HASH
#ON PointsDeRaccordement (Eid);
#
#CREATE INDEX EidSatellites
#USING HASH
#ON Satellites (Eid);
#
#CREATE INDEX EidStrategiques
#USING HASH
#ON Strategiques (Eid);
#
#CREATE INDEX EidTransformateursSurPoteauDeBois
#USING HASH
#ON TransformateursSurPoteauDeBois (Eid);
#
#CREATE INDEX EidCentrales
#USING HASH
#ON Centrales (Eid);
#
CREATE INDEX EidLignes
USING HASH
ON Lignes (Eid);
#
#CREATE INDEX EidSupports
#USING HASH
#ON Supports (Eid);
#
