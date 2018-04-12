
class ListeBris:
    def __init__(self, req):
        self.execute = req.execute
        self.commit = req.con.commit


    def get_data(self, priorite):
        liste_bris = []
        bris = self.execute("SELECT Eid, CAST(Debut AS CHAR) FROM Bris WHERE Fin IS NULL;")
        if priorite == "date":
            rev_order = False
        else:
            rev_order = True
        for b in bris:
            eid = b[0]
            debut = b[1]
            raccordements = []
            aids = []
            estimation_conso = 0
            nom = self.get_equipement_nom(eid)
            ville = self.__trouver_ville(eid)[0][0]
            if priorite != "date":
                self.__trouver_raccordements(eid, raccordements)
                if priorite == "estimation_conso":
                    aids = self.__trouver_abonnes_racc(raccordements)
                    estimation_conso = self.__estimation_conso(aids, debut)
            liste_bris.append({"eid" : eid,
                               "date": debut,
                               "nom" : nom,
                               "ville" : ville,
                               "nb_abonnes": len(raccordements),
                               "aids" : aids,
                               "raccordements" : raccordements,
                               "estimation_conso": round(estimation_conso, 2)})
        return sorted(liste_bris, key=lambda bris: bris[priorite], reverse=rev_order)



    def get_liste_details(self, bris):
        if bris['raccordements'] == []:
            self.__trouver_raccordements(bris['eid'], bris['raccordements'])
        if bris['aids'] == []:
            bris['aids'] = self.__trouver_abonnes_racc(bris['raccordements'])
        if bris['estimation_conso'] == 0:
            bris['estimation_conso'] = self.__estimation_conso(bris['aids'], bris['date'])
        return {"eid" : bris['eid'], "nom" : bris['nom'], "ville" : bris['ville'], "date" : bris['date'],
                "nb_abonnes": len(bris['raccordements']), "aids" : bris['aids'],
                "estimation_conso": bris['estimation_conso'], "meteo" : self.trouver_meteo(bris['ville'], bris['date'])}

    def resoudre_bris(self, eid, debut):
        self.execute("UPDATE Bris SET Fin=NOW() WHERE Eid='{0}' AND Debut=STR_TO_DATE('{1}', '%Y-%m-%d %H:%i:%s');".format(eid, debut))
        self.commit()


    def get_equipement_nom(self, eid):
        if eid[0:4] == "SUPP":
            return "Support: " + self.execute('SELECT Categorie FROM Supports WHERE Eid="{}";'.format(eid))[0][0] 
        elif eid[0:4] == "SOUR":
            return "Poste source"
        elif eid[0:4] == "CENT":
            return self.execute('SELECT Categorie FROM Centrales WHERE Eid="{}";'.format(eid))[0][0]
        elif eid[0:4] == "LIGN":
            return "Ligne: " + self.execute('SELECT Categorie FROM Lignes WHERE Eid="{}";'.format(eid))[0][0]
        elif eid[0:4] == "RACC":
            return "Point de raccordement"
        elif eid[0:4] == "SATE":
            return "Poste satellite"
        elif eid[0:4] == "STRA":
            return "Poste strategique"
        elif eid[0:4] == "TRAN":
            return "Transformateur sur poteau de bois"
        


    def __trouver_raccordements(self, eid, raccordements):
        if eid[0:4] == "SUPP":
            eid = self.execute('SELECT Poste2 FROM Lignes WHERE Eid=(SELECT Ligne FROM Supports WHERE Eid="{}");'.format(eid))[0][0]
        elif eid[0:4] == "LIGN":
            eid = self.execute('SELECT Poste2 FROM Lignes WHERE Eid="{}";'.format(eid))[0][0]
        elif eid[0:4] == "CENT":
            eid = self.execute('SELECT PosteSource FROM Centrales WHERE Eid={};'.format(eid))[0][0]
        new_eids = self.execute('SELECT Poste2 FROM Lignes WHERE Poste1="{}";'.format(eid))
        if len(new_eids) == 0:
            raccordements.append(eid) 
        for e in new_eids:
            self.__trouver_raccordements(e[0], raccordements)


    def __trouver_abonnes_racc(self, raccordements):
        abonnes = []
        for r in raccordements:
            abonnes.append(self.execute('SELECT Aid FROM Abonnes WHERE PointDeRaccordement="{}";'.format(r))[0][0])
        return abonnes

    def __estimation_conso(self, aids, debut):
        estimation = 0
        for aid in aids: 
            req = 'SELECT AVG(Puissance)\
                   FROM ConsommationsMensuelles\
                   WHERE Aid={0} AND (DATEDIFF("{1}", Mois) < 93) AND Mois < "{1}";'.format(aid, debut)
            estimation += self.execute(req)[0][0]
        return round(float(estimation),2)


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


    def trouver_meteo(self, ville, heure):
        meteo = self.execute('SELECT *\
                             FROM ConditionsMeteorologiques\
                             WHERE Ville="{0}"\
                             AND DATEDIFF(Heure, "{1}")=0\
                             AND ABS(TIMEDIFF(Heure, "{1}"))<=5959;'.format(ville, heure))[0]
        return {"Temperature" : meteo[2],
                "Humidite" : meteo[3],
                "Pression" : meteo[4],
                "Pluie" : meteo[5],
                "Neige" : meteo[6],
                "Couverture neige" : meteo[7]}

