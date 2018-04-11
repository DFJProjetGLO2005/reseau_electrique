.La classe Requetes permet d'intéragir avec la base de données.
.Les autres classes sont associés à une page du site et nécessitent
 une instance de Requetes afin d'être fonctionnelles.
 Dans les exemples suivants on imagine que "req" est une instance
 de Requetes.


listeBris.html
--------------
    fichier: listeBris.py
    méthode: ListeBris(req).get_data(param)
    param: "date" OU "nb_abonnes" OU "estimation_conso"
    retour: Une liste de dictionnaires ayant pour clés
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
    Toutes ces données sont nécessaires afin d'afficher listeBris.html
    Cependant, certaines de celles-ci n'y seront pas directement affichées.
    Nous les gardons tout de même puisque les pages connexes les utiliseront.

    
detailsBris.html
----------------
    fichier: listeBris.py
    méthode: ListeBris(req).get_liste_Details(eid, debut, nom, ville, nb_abonnes, aids, raccordements, estimation_conso)
    params: Ils proviennent de la requête faite pour listeBris.html
    bouton résoudre bris: ListeBris(req).resoudre_bris(eid, date)
    retour: Un dictionnaire ayant pour clés
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
        


listeCentrales.html
-------------------
    fichier: listeCentrales.py
    méthode: ListeCentrales(req).get_data()
    retour: Une liste de dictionnaires ayant pour clés
            "categorie"
            "eid"
            "puissance"
            "ville"


listeAbonnes.html
-----------------
    fichier: listeAbonnes.py
    param: aids est une liste d'id d'abonnés
           Cette liste sera recueillie les pages précédentes à celle-ci
    méthode: ListeAbonnes(req).get_data(aids)
    retour: Une liste de listes
            [Aid, "Nom", "Numéro de téléphone"]


listeConsommationsMensuelles.html
---------------------------------
    fichier: listeConsommationsMensuelles.py
    méthode: ListeConsommationsMensuelles(req).get_data(aid)
    param: L'id d'un abonné
    retour: Une liste de listes
            ["Mois", Consommation en kw/h]


listeEquipements.html
---------------------
    fichier: listeEquipements.py
    méthode: ListeEquipements(req).get_data(ville)
    param: Le nom de la ville
    retour: (Nom de ville, Liste de listes [Type d'équipement, nombre de cet équipement])


listeVilles.html
----------------
    fichier: listeVilles.html
    méthode: ListeVilles(req).get_data()
    retour: Une liste de tuples
            (Nom de ville, (Consommation, [aids]))


