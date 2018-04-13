"""
    Brief: Cette classe permet de faire les requêtes nécessaires
           pour afficher la page listeAbonnes.html du siteweb.
"""
class ListeAbonnes:
    """
        Brief: Le constructeur donne à l'instance courante la possibilité
               de faire des requêtes mysql grâce à une instance de la classe
               Requêtes passée en argument.
    """
    def __init__(self, req):
        self.execute = req.execute

    """
        Brief: Cette méthode retourne les informations relative à une liste d'abonnées.
        Param[in]: (int list) Une liste d'identificateurs d'abonnés.
        Return: Une liste de listes [Aid, "Nom", "Numéro de téléphone"]
    """
    def get_data(self, aids):
        aids = "({})".format(", ".join(str(a) for a in aids))
        return self.execute("SELECT Aid, Nom, Telephone FROM Abonnes WHERE Aid in {};".format(aids))
