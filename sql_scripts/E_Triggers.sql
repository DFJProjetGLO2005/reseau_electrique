delimiter //



# CategoriesDeSupports (foreign key ENUM: enlever cette table et ces spécifications?)
# TRIGGER: vérifier que chaque ID inséré dans une table correspond au code établi
# TRIGGER: cardinalités max par type de poste
#

#CREATE TRIGGER LignesPostesDistincts
#BEFORE INSERT ON Lignes
#FOR EACH ROW
#BEGIN
#    IF (NEW.Poste1 = NEW.Poste2)
#    THEN SET NEW.Eid = NULL;
#    END IF;
#END;//

#CREATE TRIGGER PrevenirSuperpositionVilles
#BEFORE INSERT ON Villes
#FOR EACH ROW
#BEGIN
#    IF ((SELECT COUNT(*)
#         FROM Villes V
#         WHERE (MBROverlaps(NEW.Lieu, V.Lieu))) > 0)
#    THEN SET NEW.nom = NULL;
#    END IF;
#END;//
#
# Tous les lieux doivent être dans une ville



delimiter ;
