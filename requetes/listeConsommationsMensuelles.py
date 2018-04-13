"""
    Brief: Cette classe permet de faire les requêtes nécessaires
           pour afficher la page listeConsommationsMensuelles.html du siteweb.
"""
class ListeConsommationsMensuelles:
    """
        Brief: Le constructeur donne à l'instance courante la possibilité
               de faire des requêtes mysql grâce à une instance de la classe
               Requêtes passée en argument.
    """
    def __init__(self, req):
        self.execute = req.execute


    """
        Brief: Cette méthode permet de faire les requêtes à la base de données
               nécéessaires pour afficher la page listeConsommationsMensuelles.html du siteweb.
        Param[in]: L'identificateur de l'abonné ciblé sous forme de int
        Return: Une liste de listes
                ["Mois", Consommation en kw/h]
    """
    def get_data(self, aid):
        return self.execute("SELECT SUBSTR(CAST(Mois AS CHAR) FROM 1 FOR 7), Puissance FROM ConsommationsMensuelles WHERE Aid={}".format(aid))

