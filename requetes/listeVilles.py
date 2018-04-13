from functools import reduce

"""
    Brief: Cette classe permet de faire les requêtes nécessaires
           pour afficher la page listeVilles.html du siteweb.
"""
class ListeVilles:
    """
        Brief: Le constructeur donne à l'instance courante la possibilité
               de faire des requêtes mysql grâce à une instance de la classe
               Requêtes passée en argument.
    """
    def __init__(self, req):
        self.execute = req.execute

    """
        Brief: Cette méthode permet de lister toutes les villes du réseau
               et de calculer pour chacunes d'elles la consommation mensuelle
               moyenne de la somme de ses habitants en MW.
        Return: Une liste de tuples
                (Nom de ville, (Consommation, [aids]))
    """
    def get_data(self):
        villes = {}
        for v in self.execute('SELECT Nom FROM Villes;'):
            villes[v[0]] = [], []
        for ev in self.execute('SELECT Eid, Nom FROM Postes P, Villes V WHERE P.Eid LIKE "RACC%" AND MBRContains(V.Lieu, P.Lieu);'):
            eid = ev[0]
            ville = ev[1]
            aid = self.execute('SELECT Aid FROM Abonnes WHERE PointDeRaccordement="{}";'.format(eid))[0][0]
            conso_moyenne = float(self.execute('SELECT AVG(Puissance) FROM ConsommationsMensuelles WHERE Aid={}'.format(aid))[0][0])
            villes[ev[1]][0].append(conso_moyenne)
            villes[ev[1]][1].append(aid)
        for ville, data in villes.items():
            villes[ville] = round(reduce(lambda x, y: x + y, data[0]) / 100,2), data[1]
        return [(v, villes[v]) for v in sorted(villes, key=villes.get, reverse=True)]

