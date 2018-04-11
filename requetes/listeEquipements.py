class ListeEquipements:
    def __init__(self, req):
        self.execute = req.execute

    def get_data(self, ville):
       polygon = self.execute('SELECT ST_AsText(Lieu) FROM Villes WHERE Nom="{}"'.format(ville))[0][0]
       centrales = self.execute("SELECT Categorie, COUNT(*) FROM Centrales WHERE PosteSource IN\
                                 (SELECT Eid From Postes WHERE MBRContains(ST_POLYGONFromText('{}'), Lieu))\
                                 GROUP BY Categorie;".format(polygon))
       postes = self.execute('SELECT SUBSTRING(Eid FROM 1 FOR 4), COUNT(*)\
                              FROM Postes WHERE MBRContains(ST_POLYGONFromText("{}"), Lieu)\
                              GROUP BY\
                              (CASE WHEN Eid LIKE "RACC%" THEN "RACC"\
                                    WHEN Eid LIKE "TRAN%" THEN "TRAN"\
                                    WHEN Eid LIKE "SATE%" THEN "SATE"\
                                    WHEN Eid LIKE "STRA%" THEN "STRA"\
                                    WHEN Eid LIKE "SOUR%" THEN "SOUR"\
                               END);'.format(polygon))
       return ville, postes
