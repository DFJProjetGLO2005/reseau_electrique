Utilisation
------------
Pour tester l'application sur votre système, veuillez exécuter le script python **installation.py**.</br>
Celui-ci vous permettra de:</br>
    .générer les données via ./csv\_generator/main.py</br>
    .générer la base de données via ./sql\_scripts/main.sql</br>
    .démarrer le serveur web via ./siteweb/serveur\_applicatif.py</br>
En tout temps, il est possible d'executer manuellement l'un des trois scripts cités ci-haut pour
par exemple démarrer le serveur web sans avoir à regénérer de réseau électrique.


# Modèle entité-relation
![alt text](https://i.imgur.com/jvoIsEs.jpg)

# Modèle relationel
**Abonnés** (__Aid : int__, Nom : char(20), Téléphone : char(8), Point de raccordement : char(9))<br>
**Consommations mensuelles** ('Aid : int', 'Mois : int', Puissance (kW/h) : real)<br>

**Équipements** (__Eid : char(9)__)<br>
**Centrales** (__Eid : char(9)__, Poste source : char(9), Categorie : enum, Puissance (MW) : real)<br> 
**Lignes** (__Eid : char(9)__, Tension : int, Courant : int, Categorie : enum, Longueur : int, Poste 1 : char(9), Poste 2 : char(9))<br>

**Supports** (__Eid : char(9)__, Ligne : char(9), Lieu : Geometry, Categorie : enum)<br>
**Categories de supports** (__Categorie : enum__, Portée : int, Poids : int, Hauteur : int)<br>

**Postes** (__Eid : char(9)__, Lieu : Geometry)<br>
**Sources** (__Eid : char(9)__, Centrale : char(9))<br>
**Satellites** (__Eid : char(9)__)<br>
**Stratégiques** (__Eid : char(9)__)<br>
**Transformateurs sur poteau de bois** (__Eid : char(9)__)<br>
**Points de raccordement** (__Eid : char(9)__, Abonne : int)<br>

**Bris** (__Eid : char(9)__, __Début : DateTime__, Fin : DateTime)<br>


**Villes** (__Nom : char(20)__, Lieu : Geometry)<br>
**Conditions météorologiques** (__Ville : char(20)__, __Heure : DateTime__, Température : int, Taux d’humidité : real, Pression atmosphérique : real, Chute de pluie : int, Chute de neige : int, Couverture de neige : int)<br>



# Schéma du site web
![alt text](https://i.imgur.com/qH5ukFj.jpg)

