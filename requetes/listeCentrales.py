"""
    Brief: Cette classe permet de faire les requêtes nécessaires
           pour afficher la page listeCentrales.html du siteweb.
"""
class ListeCentrales:
    """
        Brief: Le constructeur donne à l'instance courante la possibilité
               de faire des requêtes mysql grâce à une instance de la classe
               Requêtes passée en argument.
    """
    def __init__(self, req):
        self.execute = req.execute


    """
        Brief: Cette méthode retourne les informations relative à la liste des centrales.
        Return: Une liste de dictionnaires ayant pour clés
                "categorie"
                "eid"
                "puissance"
                "ville"
    """
    def get_data(self):
        req =  self.execute("SELECT Categorie, Eid, Puissance FROM Centrales;")   
        data = []
        for c in req:
            data.append({"categorie" : c[0],
                         "eid" : c[1],
                         "puissance" : c[2],
                         "ville" : self.__trouver_ville(c[1])[0][0]})
        return sorted(data, key=lambda centrale: centrale["puissance"], reverse=True)


    """
        Brief: Cette méthode permet de trouver la ville où une centrale se situe.
        Param[in]: L'identificateur de la centrale.
        Return: La ville où la centrale se situe.
    """
    def __trouver_ville(self, eid):
        return self.execute('SELECT Nom FROM Villes V WHERE MBRContains(V.Lieu,\
                            (SELECT Lieu FROM Postes WHERE Eid=\
                             (SELECT PosteSource FROM CENTRALES WHERE Eid = "{}")));'.format(eid))

