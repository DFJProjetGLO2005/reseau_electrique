
class ListeCentrales:
    def __init__(self, req):
        self.execute = req.execute

    def get_data(self):
        req =  self.execute("SELECT Categorie, Eid, Puissance FROM Centrales;")   
        data = []
        for c in req:
            data.append({"categorie" : c[0],
                         "eid" : c[1],
                         "puissance" : c[2],
                         "ville" : self.__trouver_ville(c[1])[0][0]})
        return sorted(data, key=lambda centrale: centrale["puissance"], reverse=True)


    def __trouver_ville(self, eid):
        return self.execute('SELECT Nom FROM Villes V WHERE MBRContains(V.Lieu,\
                            (SELECT Lieu FROM Postes WHERE Eid=\
                             (SELECT PosteSource FROM CENTRALES WHERE Eid = "{}")));'.format(eid))

