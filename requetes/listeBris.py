from hashlib import sha256

"""
    Brief: Cette classe permet de faire les requêtes nécessaires
           pour afficher les pages listeBris.html et detailsBris.html
"""
class ListeBris:
    """
        Brief: Le constructeur donne à l'instance courante la possibilité
               de faire des requêtes mysql grâce à une instance de la classe
               Requêtes passée en argument.
    """
    def __init__(self, req):
        self.execute = req.execute
        self.commit = req.con.commit


    """
        Brief: Cette méthode retourne la liste des bris non résolus.
        Param[in]: La clé d'ordonnancement de la liste
                   "date" OU "nb_abonnes" OU "estimation_conso"
        Return: Une liste de dictionnaires ayant pour clés
                "eid"               Le id de l'équipement brisé
                "date"              La date de début du bris
                "nom"               Le nom de l'équipement
                "ville"             La ville où l'équipement se situe
                "nb_abonnes"        Le nombre d'abonnés affectés
                "aids"              Une liste des id des abonnées affectés
                "raccordements"     Une liste des points de raccordements de ces abonnés
                "estimation_conso"  Une estimation des consommations rendues impossibles
                                    pour le mois prochain basée sur la moyenne des trois
                                    derniers mois des utilisateurs affectés.
    """
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
            nom = self.__get_equipement_nom(eid)
            ville = self.__trouver_ville(eid)[0][0]
            if priorite != "date":
                self.__trouver_raccordements(eid, raccordements)
                if priorite == "estimation_conso":
                    #aids = self.__trouver_abonnes_racc(raccordements)
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


    """
        Brief: Cette méthode fait les requêtes nécessaires afin d'afficher la
               page detailsBris.html
        Param[in]: Un dictionnaire contenant les informations relatives à un bris.
                   Ce dictionnaire pourra être généré avec get_data
        Return: Un dictionnaire ayant pour clés
                "eid"               Le id de l'équipement brisé
                "nom"               Le nom de l'équipement
                "ville"             La ville où l'équipement se situe
                "date"              La date de début du bris
                "nb_abonnes"        Le nombre d'abonnés affectés
                "estimation_conso"  Une estimation des consommations rendues impossibles
                                    pour le mois prochain basée sur la moyenne des trois
                                    derniers mois des utilisateurs affectés.
                "meteo"             Un dictionnaire ayant pour clés
                                    "Temperature"           Int en celcius
                                    "Humidite"              Real en pourcents
                                    "Pression"              Real
                                    "Pluie"                 Int milimètres de pluie
                                    "Neige"                 Int centimètres de neige
                                    "Couverture neige"      Int centimètres de neige déjà au sol
    """
    def get_liste_details(self, bris):
        if bris['raccordements'] == []:
            self.__trouver_raccordements(bris['eid'], bris['raccordements'])
        if bris['aids'] == []:
            bris['aids'] = self.__trouver_abonnes_racc(bris['raccordements'])
        if bris['estimation_conso'] == 0:
            bris['estimation_conso'] = self.__estimation_conso(bris['aids'], bris['date'])
        return {"eid" : bris['eid'], "nom" : bris['nom'], "ville" : bris['ville'], "date" : bris['date'],
                "nb_abonnes": len(bris['raccordements']), "aids" : bris['aids'],
                "estimation_conso": bris['estimation_conso'], "meteo" : self.__trouver_meteo(bris['ville'], bris['date'])}


    """
        Brief: Cette méthode vérifie si le mot de passe donné correspond bien
               au mot de passe haché dans la base de données.
        Param[in]: Le mot de passe à tester sous forme de string.
        Return: 0 ou 1, tout dépendant du résultat de la vérification.
    """
    def check_password(self, password):
        password = sha256(password.encode()).hexdigest()
        return self.execute('SELECT COUNT(*) FROM AdminPassword\
                             WHERE Password="{}" LIMIT 1;'.format(password))[0][0]

    """
        Brief: Cette méthode est appelée par la page detailsBris.html et permet
               de résourdre un bris.
        Params[in]: La clé primaire du bris, soit le eid et la date de début du bris.
    """
    def resoudre_bris(self, eid, debut):
        self.execute("UPDATE Bris SET Fin=NOW() WHERE Eid='{0}' AND Debut=STR_TO_DATE('{1}', '%Y-%m-%d %H:%i:%s');".format(eid, debut))
        self.commit()


    """
        Brief: Cette méthode privée permet de retourner une description
               intelligible d'un équipement donné.
        Param[in]: L'identificateur de l'équipement
        Return: Un string décrivant l'équipement
               
    """
    def __get_equipement_nom(self, eid):
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
        

    """
        Brief: Cette méthode implémente un algorithme récursif permettant   
               de trouver les feuilles d'un arbre n-aire constituant le réseau
               électrique pour un noeud donné.
        Param[in] eid: L'identificateur d'un équipement quelconque du réseau.
                       Étant donné que les équipements de type poste représentent
                       les noeuds du graphe, la méthode doit convertir l'identificateur
                       fourni en celui du poste associé à l'équipement fourni.
        Param[in] raccordements: Une liste initialement vide qui sera progressivement
                                 peuplée de toutes les feuilles du graphe trouvées.
                                 Dans le contexte actuel, les feuilles sont des points
                                 de raccordement qui sont logiquement liés à des abonnés du réseau.
    """
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


    """
        Brief: Cette méthode permet de trouver tous les abonnés qui sont liés
               à des points de raccordement données.
        Param[in]: Une liste d'identificateur de point des raccordements sous
                   forme de strings.
    """
    def __trouver_abonnes_racc(self, raccordements):
        abonnes = []
        for r in raccordements:
            abonnes.append(self.execute('SELECT Abonne FROM Abonnes WHERE PointDeRaccordement="{}";'.format(r))[0][0])
        return abonnes

    """
        Brief: Cette méthode permet d'estimer la consommation qui aurait eut lieu le mois suivant
               l'apparition d'un bris si celui-ci ne s'était pas produit. Pour ce faire, elle 
               calcule la somme des moyennes des consommations sur les trois mois précédant
               le bris pour tous les abonnés affectés.
        Param[in] aids: Une liste des identificateurs des abonnés affectés.
        Param[in] debut: Le moment où le bris s'est produit sous forme de string
        Return: L'énergie estimée sous forme de float.
    """
    def __estimation_conso(self, aids, debut):
        estimation = 0
        for aid in aids: 
            req = 'SELECT AVG(Puissance)\
                   FROM ConsommationsMensuelles\
                   WHERE Aid={0} AND (DATEDIFF("{1}", Mois) < 93) AND Mois < "{1}";'.format(aid, debut)
            estimation += self.execute(req)[0][0]
        return round(float(estimation),2)


    """
        Brief: Cette méthode permet localier un équipement étant donné son identificateur.
        Param[in]: L'identificateur d'un équipement sous forme de string. 
        Return: Le nom de la ville où l'équipement se situe.
    """
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


    """
        Brief: Cette méthode permet de trouver conditions météorologiques
               pour une ville et un moment donné.
        Param[in] ville: Le nom de la ville sous forme de string.
        Param[in] heure: L'heure sous forme de string.
        Return Un dictionnaire listant les conditions météorologiques trouvées.
    """
    def __trouver_meteo(self, ville, heure):
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

