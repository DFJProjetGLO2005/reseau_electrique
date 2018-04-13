"""
    Brief: Cette classe permet de faire les requêtes nécessaires
           pour afficher la page listeAbonnes.html du siteweb.
"""
class ListeAbonnes:
    def __init__(self, req):
        self.execute = req.execute

    """
        Brief: Cette fonction retourne les informations relative à une liste d'abonnées.
        Param[in]: (int list) Une liste d'identificateurs d'abonnés.
        Return: 
    """
    def get_data(self, aids):
        aids = "({})".format(", ".join(str(a) for a in aids))
        return self.execute("SELECT Aid, Nom, Telephone FROM Abonnes WHERE Aid in {};".format(aids))
