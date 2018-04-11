import pymysql

class ListeCentrales:
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
        req =  self.execute("SELECT Categorie, Eid, Puissance FROM Centrales;")   
        retour = []
        for c in req:
            retour.append({"categorie" : c[0],
                           "eid" : c[1],
                           "puissance" : c[2],
                           "ville" : self.__trouver_ville(c[1])[0][0]})
        return retour


    def __trouver_ville(self, eid):
        return self.execute('SELECT Nom FROM Villes V WHERE MBRContains(V.Lieu,\
                            (SELECT Lieu FROM Postes WHERE Eid=\
                             (SELECT PosteSource FROM CENTRALES WHERE Eid = "{}")));'.format(eid))


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

