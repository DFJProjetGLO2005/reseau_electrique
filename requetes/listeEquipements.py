
"""
    Brief: Cette classe permet de faire les requêtes nécessaires
           pour afficher la page listeEquipements.html du siteweb.
"""
class ListeEquipements:
    """
        Brief: Le constructeur donne à l'instance courante la possibilité
               de faire des requêtes mysql grâce à une instance de la classe
               Requêtes passée en argument.
    """
    def __init__(self, req):
        self.execute = req.execute

    """
        Brief: Cette méthode permet de trouver tous les équipements situés
               dans la ville précisée.
        Param[in]: Le nom de la ville ciblée
        Return: (Nom de ville, Liste de listes [Type d'équipement, nombre de cet équipement])
    """
    def get_data(self, ville):
       polygon = self.execute('SELECT ST_AsText(Lieu) FROM Villes WHERE Nom="{}"'.format(ville))[0][0]
       centrales = self.execute("SELECT Categorie, COUNT(*) FROM Centrales WHERE PosteSource IN\
                                 (SELECT Eid From Postes WHERE MBRContains(ST_POLYGONFromText('{}'), Lieu))\
                                 GROUP BY Categorie;".format(polygon))
       postes = self.execute('SELECT CONCAT("POSTE ", SUBSTRING(Eid FROM 1 FOR 4)), COUNT(*)\
                              FROM Postes WHERE MBRContains(ST_POLYGONFromText("{}"), Lieu)\
                              GROUP BY\
                              (CASE WHEN Eid LIKE "RACC%" THEN "RACC"\
                                    WHEN Eid LIKE "TRAN%" THEN "TRAN"\
                                    WHEN Eid LIKE "SATE%" THEN "SATE"\
                                    WHEN Eid LIKE "STRA%" THEN "STRA"\
                                    WHEN Eid LIKE "SOUR%" THEN "SOUR"\
                               END);'.format(polygon))
       lignes = self.execute('SELECT CONCAT("LIGNE ", Categorie), COUNT(*)\
                              FROM Lignes WHERE Poste1 IN\
                              (SELECT Eid From Postes WHERE MBRContains(ST_POLYGONFromText("{}"), Lieu))\
                              GROUP BY Categorie;'.format(polygon))
       supports = self.execute('SELECT Categorie, COUNT(*)\
                                FROM Supports WHERE MBRContains(ST_POLYGONFromText("{}"), Lieu)\
                                GROUP BY Categorie;'.format(polygon))
       return ville, postes + centrales + lignes + supports
