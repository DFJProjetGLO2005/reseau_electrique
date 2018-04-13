import pymysql

"""
    Brief: Cette classe permet de simplifier et d'uniformiser l'opération
           de requête qui est utilisée à répétition par les autres scripts
           de ce dossier.
"""
class Requetes:
    """
    Brief: Le constructeur prend le nom d'utilisateur et le mot de passe
           de l'utilisateur du serveur mysql utilisé.
           La base de données reseau_electrique est utilisée par défaut.
    """
    def __init__(self, user, password):
        self.con = pymysql.connect( host='localhost',
                            user=user,
                            password=password,
                            db='reseau_electrique')
        self.cur = self.con.cursor()

    """
        Brief: Le destructeur de la classe permet de terminer
               la connection avec la base de donnée proprement.
    """
    def __del__(self):
        self.cur.close()
        self.con.close()

    """
        Brief: Cette méthode permet d'exécuter une requête.
               Toutes les autres classes du dossier courant
               conservent une copie de cette méthode localement.
        Param[in]: Un string respectant la syntaxe mysql
        Return: Le résultat de la requête sous forme de liste de lignes
                qui sont des listes de valeurs.
    """
    def execute(self, cmd):
        self.cur.execute(cmd)
        return self.fetch_cursor()


    """
        Brief: Cette méthode permet de récupérer les données
               contenues par le curseur.
        Return: Une liste de listes, soit une liste de lignes
                qui sont des listes de valeurs.
    """
    def fetch_cursor(self):
        result = []
        for tup in self.cur:
            line = []
            for attr in tup:
                line.append(attr)
            result.append(line)
        return result

