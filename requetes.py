import pymysql

class Requetes:
    def __init__(self, user, password):
        self.con = pymysql.connect( host='localhost',
                            user=user,
                            password=password,
                            db='reseau_electrique')
        self.cur = self.con.cursor()

    def __del__(self):
        self.cur.close()
        self.con.close()

    #####################################################################

    def get_bris(self):
        liste_bris = []
        bris = self.execute("SELECT Eid, Debut FROM Bris WHERE Fin IS NOT NULL;")
        for b in bris:
            liste_bris.append({"eid" : b[0],
                               "nom" : self.get_equipement_nom(b[0]),
                               "ville" : self.__trouver_ville(b[0]),
                               "date" : b[1]})
        return liste_bris


    def get_equipement_nom(self,eid):
        if eid[0:4] == "SUPP":
            return "Support: " + self.execute('SELECT Categorie FROM Supports WHERE Eid="{}";'.format(eid)) 
        elif eid[0:4] == "SOUR":
            return "Poste source"
        elif eid[0:4] == "CENT":
            return self.execute('SELECT Categorie FROM Centrales WHERE Eid="{}";'.format(eid))
        elif eid[0:4] == "LIGN":
            return "Ligne: " + self.execute('SELECT Categorie FROM Lignes WHERE Eid="{}";'.format(eid))
        elif eid[0:4] == "RACC":
            return "Point de raccordement"
        elif eid[0:4] == "SATE":
            return "Poste satellite"
        elif eid[0:4] == "STRA":
            return "Poste strategique"
        elif eid[0:4] == "TRAN":
            return "Transformateur sur poteau de bois"
        



    def details_bris(self, eid, debut, ville):
        raccordements = []
        self.__trouver_raccordements(eid, raccordements)
        aids = self.__trouver_abonnes_racc(raccordements)
        return {"nb_abonnes" : len(raccordements),
                "aids" : aids,
                "estimation_conso" : self.__consommations_futures_estimees(aids, debut),
                "meteo" : self.trouver_meteo(ville, debut)}

    def trouver_meteo(self, ville, heure):
        # warning
        meteo = self.execute("SELECT * FROM ConditionsMeteorologiques WHERE Ville='{0}' AND\
                              (TIME_TO_SEC(TIMEDIFF(Heure, '{1}')) < 3600) LIMIT 1;".format(ville, heure))
        print(meteo)

        
    def __trouver_raccordements(self, eid, raccordements):
        if eid[0:4] == "SUPP":
            eid = self.execute('SELECT Poste2 FROM Lignes WHERE Eid=(SELECT Ligne FROM Supports WHERE Eid="{}");'.format(eid))
        elif eid[0:4] == "LIGN":
            eid = self.execute('SELECT Poste2 FROM Lignes WHERE Eid="{}";'.format(eid))
        elif eid[0:4] == "CENT":
            eid = self.execute('SELECT PosteSource FROM Centrales WHERE Eid={};'.format(eid))
        new_eids = self.execute('SELECT Poste2 FROM Lignes WHERE Poste1="{}";'.format(eid))
        if len(new_eids) == 0:
            raccordements.append(eid) 
        for e in new_eids:
            self.__trouver_raccordements(e, raccordements)

    def __trouver_abonnes_racc(self, raccordements):
        abonnes = []
        for r in raccordements:
            abonnes.append(self.execute('SELECT Aid FROM Abonnes WHERE PointDeRaccordement="{}";'.format(r)))
        return abonnes

    def __consommations_futures_estimees(self, aids, debut):
        estimation = 0
        for aid in aids:
            req = 'SELECT AVG(Puissance)\
                   FROM ConsommationsMensuelles\
                   WHERE Aid={0} AND (DATEDIFF("{1}", Mois) < 93) AND Mois < "{1}";'.format(aid, debut)
            estimation += self.execute(req)
        estimation /= len(aids)
        return float(estimation)


    def __trouver_ville(self, eid):
        if eid[0:4] == "SUPP":
            ville = self.execute('SELECT Nom FROM Villes V WHERE MBRContains(V.Lieu,\
                                  (SELECT Lieu FROM Supports WHERE Eid="{}"));'.format(eid))
        elif eid[0:4] == "CENT":
            ville = self.execute('SELECT Nom FROM Villes V WHERE MBRContains(V.Lieu,\
                                  (SELECT Lieu FROM Postes\
                                   WHERE Eid=(SELECT Eid FROM Sources WHERE Centrale="{}")));'.format(eid))
        elif eid[0:4] == "LIGN":
            ville = self.execute('SELECT Nom FROM Villes V WHERE MBRContains(V.Lieu,\
                                  (SELECT Lieu FROM Postes\
                                   WHERE Eid=(SELECT Poste1 FROM Lignes WHERE Eid="{}")));'.format(eid))
        else:
            ville = self.execute('SELECT Nom FROM Villes V WHERE MBRContains(V.Lieu,\
                                  (SELECT Lieu FROM Postes WHERE Eid="{}"));'.format(eid))
        return ville




    #########################################################################
    def execute(self, cmd):
        self.cur.execute(cmd)
        return self.fetch_cursor()
    
    def fetch_cursor(self):
        result = []
        for tup in self.cur:
            line = []
            for attr in tup:
                line.append(attr)
            if len(line) == 1: line = line[0]
            result.append(line)
        if len(result) == 1: result = result[0]
        return result

