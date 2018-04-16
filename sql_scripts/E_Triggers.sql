SELECT "Creation des gachettes..." as "";
delimiter //



CREATE PROCEDURE equipementValide (INOUT Eid CHAR(9))
BEGIN
    IF ((Eid NOT IN (SELECT C.Eid FROM Centrales C)) AND
        (Eid NOT IN (SELECT P.Eid FROM Postes P)) AND
        (Eid NOT IN (SELECT L.Eid FROM Lignes L)) AND
        (Eid NOT IN (SELECT S.Eid FROM Supports S)))
    THEN SET Eid = NULL;
    END IF;
END//

CREATE TRIGGER equipementValideInsert
BEFORE INSERT ON Equipements
FOR EACH ROW
CALL equipementValide (NEW.Eid)//

CREATE TRIGGER equipementValideUpdate
BEFORE UPDATE ON Equipements
FOR EACH ROW
CALL equipementValide (NEW.Eid)//




CREATE PROCEDURE posteValide (INOUT Eid CHAR(9))
BEGIN
    IF ((Eid NOT IN (SELECT S.Eid FROM Sources S)) AND
        (Eid NOT IN (SELECT S.Eid FROM Strategiques S)) AND
        (Eid NOT IN (SELECT S.Eid FROM Satellites S)) AND
        (Eid NOT IN (SELECT P.Eid FROM PointsDeRaccordement P)) AND
        (Eid NOT IN (SELECT T.Eid FROM TransformateursSurPoteauDeBois T)))
    THEN SET Eid = NULL;
    END IF;
END//

CREATE TRIGGER posteValideInsert
BEFORE INSERT ON Postes
FOR EACH ROW
CALL posteValide (NEW.Eid)//

CREATE TRIGGER posteValideUpdate
BEFORE UPDATE ON Postes
FOR EACH ROW
CALL posteValide (NEW.Eid)//




CREATE PROCEDURE prevenirSuperpositionVilles (INOUT Nom CHAR(35), IN Lieu GEOMETRY)
BEGIN
    IF ((SELECT COUNT(*)
         FROM Villes V
         WHERE (MBROverlaps(Lieu, V.Lieu))) > 0)
    THEN SET Nom = NULL;
    END IF;
END//

CREATE TRIGGER prevenirSuperpositionVillesInsert
BEFORE INSERT ON Villes
FOR EACH ROW
CALL PrevenirSuperpositionVilles(NEW.Nom, NEW.Lieu)//

CREATE TRIGGER prevenirSuperpositionVillesUpdate
BEFORE UPDATE ON Villes
FOR EACH ROW
CALL prevenirSuperpositionVilles(NEW.Nom, NEW.Lieu)//





CREATE PROCEDURE verifierLigne(INOUT EID CHAR(9), IN P1 CHAR(9), IN P2 CHAR(9))
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

CREATE TRIGGER verifierLigneInsert
BEFORE INSERT ON Lignes    
FOR EACH ROW
CALL verifierLigne(NEW.Eid, New.Poste1, New.Poste2)//

CREATE TRIGGER verifierLigneUpdate
BEFORE UPDATE ON Lignes    
FOR EACH ROW
CALL verifierLigne(NEW.Eid, New.Poste1, New.Poste2)//








##############################################################
## Le format de EID est correct selon la catégorie déquipement
CREATE PROCEDURE EidCentralesCorrect(INOUT EID CHAR(9))
BEGIN
    IF (Eid NOT LIKE "CENT%")
    THEN SET Eid = NULL;
    END IF;
END//

CREATE TRIGGER EidCentralesCorrectInsert
BEFORE INSERT ON Centrales
FOR EACH ROW
CALL EidCentralesCorrect(NEW.Eid)//

CREATE TRIGGER EidCentralesCorrectUpdate
BEFORE UPDATE ON Centrales
FOR EACH ROW
CALL EidCentralesCorrect(NEW.Eid)//



CREATE PROCEDURE EidLignesCorrect(INOUT EID CHAR(9))
BEGIN
    IF (Eid NOT LIKE "LIGN%")
    THEN SET Eid = NULL;
    END IF;
END//

CREATE TRIGGER EidLignesCorrectInsert
BEFORE INSERT ON Lignes
FOR EACH ROW
CALL EidLignesCorrect(NEW.Eid)//

CREATE TRIGGER EidLignesCorrectUpdate
BEFORE UPDATE ON Lignes
FOR EACH ROW
CALL EidLignesCorrect(NEW.Eid)//



CREATE PROCEDURE EidPointsDeRaccordementCorrect(INOUT EID CHAR(9))
BEGIN
    IF (Eid NOT LIKE "RACC%")
    THEN SET Eid = NULL;
    END IF;
END//

CREATE TRIGGER EidPointsDeRaccordementCorrectInsert
BEFORE INSERT ON PointsDeRaccordement
FOR EACH ROW
CALL EidPointsDeRaccordementCorrect(NEW.Eid)//

CREATE TRIGGER EidPointsDeRaccordementCorrectUpdate
BEFORE UPDATE ON PointsDeRaccordement
FOR EACH ROW
CALL EidPointsDeRaccordementCorrect(NEW.Eid)//


CREATE PROCEDURE EidSatellitesCorrect(INOUT EID CHAR(9))
BEGIN
    IF (Eid NOT LIKE "SATE%")
    THEN SET Eid = NULL;
    END IF;
END//

CREATE TRIGGER EidSatellitesCorrectInsert
BEFORE INSERT ON Satellites
FOR EACH ROW
CALL EidSatellitesCorrect(NEW.Eid)//

CREATE TRIGGER EidSatellitesCorrectUpdate
BEFORE UPDATE ON Satellites
FOR EACH ROW
CALL EidSatellitesCorrect(NEW.Eid)//



CREATE PROCEDURE EidSourcesCorrect(INOUT EID CHAR(9))
BEGIN
    IF (Eid NOT LIKE "SOUR%")
    THEN SET Eid = NULL;
    END IF;
END//

CREATE TRIGGER EidSourcesCorrectInsert
BEFORE INSERT ON Sources
FOR EACH ROW
CALL EidSourcesCorrect(NEW.Eid)//

CREATE TRIGGER EidSourcesCorrectUpdate
BEFORE UPDATE ON Sources
FOR EACH ROW
CALL EidSourcesCorrect(NEW.Eid)//




CREATE PROCEDURE EidStrategiquesCorrect(INOUT EID CHAR(9))
BEGIN
    IF (Eid NOT LIKE "STRA%")
    THEN SET Eid = NULL;
    END IF;
END//

CREATE TRIGGER EidStrategiqueCorrectInsert
BEFORE INSERT ON Strategiques
FOR EACH ROW
CALL EidStrategiquesCorrect(NEW.Eid)//

CREATE TRIGGER EidStrategiqueCorrectUpdate
BEFORE UPDATE ON Strategiques
FOR EACH ROW
CALL EidStrategiquesCorrect(NEW.Eid)//




CREATE PROCEDURE EidSupportsCorrect(INOUT EID CHAR(9))
BEGIN
    IF (Eid NOT LIKE "SUPP%")
    THEN SET Eid = NULL;
    END IF;
END//

CREATE TRIGGER EidSupportsCorrectInsert
BEFORE INSERT ON Supports
FOR EACH ROW
CALL EidSupportsCorrect(NEW.Eid)//

CREATE TRIGGER EidSupportsCorrectUpdate
BEFORE UPDATE ON Supports
FOR EACH ROW
CALL EidSupportsCorrect(NEW.Eid)//



CREATE PROCEDURE EidTransformateursCorrect(INOUT EID CHAR(9))
BEGIN
    IF (Eid NOT LIKE "TRAN%")
    THEN SET Eid = NULL;
    END IF;
END//

CREATE TRIGGER EidTransformateursCorrectInsert
BEFORE INSERT ON TransformateursSurPoteauDeBois
FOR EACH ROW
CALL EidTransformateursCorrect(NEW.Eid)//

CREATE TRIGGER EidTransformateursCorrectUpdate
BEFORE UPDATE ON TransformateursSurPoteauDeBois
FOR EACH ROW
CALL EidTransformateursCorrect(NEW.Eid)//



delimiter ;
