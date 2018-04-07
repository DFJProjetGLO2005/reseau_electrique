delimiter //

## ON UPDATE AUSSI: mettre le code dans une procedure qui sera appelée par les 2 triggers
# Prévenir lexistence dun équipement sans ses tables associées






#CREATE TRIGGER InsertionPoste
#BEFORE INSERT ON Postes
#FOR EACH ROW
#BEGIN
#    INSERT INTO Equipements (Eid) VALUES (NEW.Eid);
#    IF (NEW.Eid LIKE "TRAN%")
#    THEN INSERT INTO TransformateursSurPoteauDeBois (Eid) VALUES (NEW.Eid);
#    ELSEIF (NEW.Eid LIKE "SATE%")
#    THEN INSERT INTO Satellites (Eid) VALUES (NEW.Eid);
#    ELSEIF (NEW.Eid LIKE "SOUR%")
#    THEN INSERT INTO Sources (Eid, Centrale) VALUES (NEW.Eid, NEW.Centrale);
#    #ELSE IF (NEW.Eid LIKE "RACC%")
#    #THEN INSERT INTO PointsDeRaccordement (Eid) VALUES (NEW.Eid);
#    END IF;
#END//

#CREATE TRIGGER InsertionLigne

#CREATE TRIGGER InsertionCentrale

#CREATE TRIGGER InsertionSupports



CREATE PROCEDURE PrevenirSuperpositionVilles (INOUT Nom CHAR(35), IN Lieu GEOMETRY)
BEGIN
    IF ((SELECT COUNT(*)
         FROM Villes V
         WHERE (MBROverlaps(Lieu, V.Lieu))) > 0)
    THEN SET Nom = NULL;
    END IF;
END//

CREATE TRIGGER SuperpositionVillesInsert
BEFORE INSERT ON Villes
FOR EACH ROW
CALL PrevenirSuperpositionVilles(NEW.Nom, NEW.Lieu)//

CREATE TRIGGER SuperpositionVillesUpdate
BEFORE UPDATE ON Villes
FOR EACH ROW
CALL PrevenirSuperpositionVilles(NEW.Nom, NEW.Lieu)//





CREATE PROCEDURE verifier_ligne(INOUT EID CHAR(9), IN P1 CHAR(9), IN P2 CHAR(9))
BEGIN
    IF ((P1 LIKE "RACC%") OR 
        ((SELECT COUNT(*) FROM Lignes WHERE Poste2=P2) <> 0 ) OR 
        ((P1 LIKE "TRAN%") AND (SELECT COUNT(*) FROM Lignes WHERE Poste1=P1) >= 6 ) OR
        (((P1 LIKE "SOUR%") OR (P1 LIKE "SATE%") OR (P1 LIKE "STRA%")) AND (SELECT COUNT(*) FROM Lignes WHERE Poste1=P1) >= 3 ) OR
        (P1 = P2) OR
        (P1 LIKE "TRAN%" AND NOT (P2 LIKE "TRAN%" OR P2 LIKE "RACC%")) OR
        (((P1 LIKE "SATE%") OR (P1 LIKE "STRA%")) AND (P2 LIKE "RACC%")) OR
        (P2 LIKE "SOUR%"))
    THEN SET EID = NULL;
    END IF;
END//

DROP TRIGGER IF EXISTS LignesInsert//
CREATE TRIGGER LignesInsert
BEFORE INSERT ON Lignes    
FOR EACH ROW
CALL verifier_ligne(NEW.Eid, New.Poste1, New.Poste2)//

DROP TRIGGER IF EXISTS LignesUpdate//
CREATE TRIGGER LignesUpdate
BEFORE UPDATE ON Lignes    
FOR EACH ROW
CALL verifier_ligne(NEW.Eid, New.Poste1, New.Poste2)//








######################################################
## EID is correct depending on the Equipement category


CREATE TRIGGER EidCentralesCorrect
BEFORE INSERT ON Centrales
FOR EACH ROW
BEGIN
    IF (NEW.Eid NOT LIKE "CENT%")
    THEN SET NEW.Eid = NULL;
    END IF;
END;//

DROP TRIGGER IF EXISTS EidLignesCorrect;
CREATE TRIGGER EidLignesCorrect
BEFORE INSERT ON Lignes
FOR EACH ROW
BEGIN
    IF (NEW.Eid NOT LIKE "LIGN%")
    THEN SET NEW.Eid = NULL;
    END IF;
END;//

DROP TRIGGER IF EXISTS EidPointsDeRaccordementCorrect;
CREATE TRIGGER EidPointsDeRaccordementCorrect
BEFORE INSERT ON PointsDeRaccordement
FOR EACH ROW
BEGIN
    IF (NEW.Eid NOT LIKE "RACC%")
    THEN SET NEW.Eid = NULL;
    END IF;
END;//

DROP TRIGGER IF EXISTS EidSatellitesCorrect;
CREATE TRIGGER EidSatellitesCorrect
BEFORE INSERT ON Satellites
FOR EACH ROW
BEGIN
    IF (NEW.Eid NOT LIKE "SATE%")
    THEN SET NEW.Eid = NULL;
    END IF;
END;//

CREATE TRIGGER EidSourcesCorrect
BEFORE INSERT ON Sources
FOR EACH ROW
BEGIN
    IF (NEW.Eid NOT LIKE "SOUR%")
    THEN SET NEW.Eid = NULL;
    END IF;
END;//

CREATE TRIGGER EidStrategiqueCorrect
BEFORE INSERT ON Strategiques
FOR EACH ROW
BEGIN
    IF (NEW.Eid NOT LIKE "STRA%")
    THEN SET NEW.Eid = NULL;
    END IF;
END;//

CREATE TRIGGER EidSupportsCorrect
BEFORE INSERT ON Supports
FOR EACH ROW
BEGIN
    IF (NEW.Eid NOT LIKE "SUPP%")
    THEN SET NEW.Eid = NULL;
    END IF;
END;//

CREATE TRIGGER EidTransformateursCorrect
BEFORE INSERT ON TransformateursSurPoteauDeBois
FOR EACH ROW
BEGIN
    IF (NEW.Eid NOT LIKE "TRAN%")
    THEN SET NEW.Eid = NULL;
    END IF;
END;//





delimiter ;
