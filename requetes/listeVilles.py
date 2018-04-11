import pymysql
from functools import reduce

class ListeVilles:
    def __init__(self, user, password):
        self.con = pymysql.connect( host='localhost',
                                    user=user,
                                    password=password,
                                    db='reseau_electrique')
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()


    def requete(self):
        villes_conso = {}
        for v in self.execute('SELECT Nom FROM Villes;'):
            villes_conso[v[0]] = []
        for ev in self.execute('SELECT Eid, Nom FROM Postes P, Villes V\
                                WHERE P.Eid LIKE "RACC%" AND MBRContains(V.Lieu, P.Lieu);'):
            eid = ev[0]
            ville = ev[1]
            aid = self.execute('SELECT Aid FROM Abonnes WHERE PointDeRaccordement="{}";'.format(eid))[0][0]
            conso_moyenne = float(self.execute('SELECT AVG(Puissance) FROM ConsommationsMensuelles WHERE Aid={}'.format(aid))[0][0])
            villes_conso[ev[1]].append(conso_moyenne)

        for ville, conso in villes_conso.items():
            villes_conso[ville] = reduce(lambda x, y: x + y, conso) / len(conso) 
        
        return villes_conso


    def execute(self, cmd):
        self.cur.execute(cmd)
        return self.fetch_cursor()
    
    def fetch_cursor(self):
        result = []
        for tup in self.cur:
            line = []
            for attr in tup:
                line.append(attr)
            result.append(line)
        return result

