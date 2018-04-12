Pour tester l'application sur votre système, veuillez exécuter le script python "installation.py".</br>
Celui-ci vous permettra de:</br>
.&nbsp;&nbsp;&nbsp;&nbsp;générer les données ./csv\_generator/main.py</br>
.&nbsp;&nbsp;&nbsp;&nbsp;générer la base de données ./sql\_scripts/main.sql</br>
.&nbsp;&nbsp;&nbsp;&nbsp;démarrer le serveur web ./siteweb/serveur\_applicatif.py</br>



# Modèle entité-relation
![alt text](https://i.imgur.com/jvoIsEs.jpg)

# Modèle relationel
**Abonnés** (__Aid : int__, Nom : char(20), Téléphone : char(8), Point de raccordement : char(9))
**Consommations mensuelles** (__Aid : int__, __Mois : int__, Puissance (kW/h) : real)

**Équipements** (__Eid : char(9)__)
**Centrales** (__Eid : char(9)__, Poste source : char(9), Categorie : enum, Puissance (MW) : real) 
**Lignes** (__Eid : char(9)__, Tension : int, Courant : int, Categorie : enum, Longueur : int, Poste 1 : char(9), Poste 2 : char(9))

**Supports** (__Eid : char(9)__, Ligne : char(9), Lieu : Geometry, Categorie : enum)
**Categories de supports** (__Categorie : enum__, Portée : int, Poids : int, Hauteur : int)

**Postes** (__Eid : char(9)__, Lieu : Geometry)
**Sources** (__Eid : char(9)__, Centrale : char(9))
**Satellites** (__Eid : char(9)__)
**Stratégiques** (__Eid : char(9)__)
**Transformateurs sur poteau de bois** (__Eid : char(9)__)
**Points de raccordement** (__Eid : char(9)__, Abonne : int)

**Bris** (__Eid : char(9)__, __Début : DateTime__, Fin : DateTime)


**Villes** (__Nom : char(20)__, Lieu : Geometry)
**Conditions météorologiques** (__Ville : char(20)__, __Heure : DateTime__, Température : int, Taux d’humidité : real, Pression atmosphérique : real, Chute de pluie : int, Chute de neige : int, Couverture de neige : int)


