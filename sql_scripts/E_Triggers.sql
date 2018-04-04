delimiter //

## ON UPDATE AUSSI: mettre le code dans une procedure qui sera appelée par les 2 triggers




CREATE TRIGGER PrevenirSuperpositionVilles
BEFORE INSERT ON Villes
FOR EACH ROW
BEGIN
    IF ((SELECT COUNT(*)
         FROM Villes V
         WHERE (MBROverlaps(NEW.Lieu, V.Lieu))) > 0)
    THEN SET NEW.nom = NULL;
    END IF;
END;//




######################################################
#CREATE PROCEDURE z(IN P1 CHAR(9), IN P2 CHAR(9))
#BEGIN
#    IF ((Poste1 LIKE "RACC%") OR
#        ((SELECT COUNT(*) FROM Lignes WHERE Poste2=NEW.Poste2) <> 0 ) OR
#        ((Poste1 LIKE "TRAN%") AND (SELECT COUNT(*) FROM Lignes WHERE Poste1=P1) >= 6 ) OR
#        (((Poste1 LIKE "SOUR%") OR (Poste1 LIKE "SATE%") OR (Poste1 LIKE "STRA%")) AND
#          (SELECT COUNT(*) FROM Lignes WHERE Poste1=Poste1) >= 3 ) OR
#        (Poste1 = Poste2))
#    THEN SET NEW.Eid = NULL;
#    END IF;
#END;//
#
#
#
#DROP TRIGGER IF EXISTS CardinalitesPostesCategories;
#CREATE TRIGGER CardinalitesPostesCategories
#BEFORE INSERT ON Lignes    
#FOR EACH ROW
#BEGIN
#    CALL z(NEW);
#END;//







######################################################
## EID is correct depending on the Equipement category
DROP TRIGGER IF EXISTS EidCentralesCorrect;
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
