Pour tester l'application sur votre système, veuillez exécuter le script python "installation.py".</br>
Celui-ci vous permettra de:</br>
&nbsp;&nbsp;&nbsp;&nbsp;.générer les données ./csv\_generator/main.py</br>
&nbsp;&nbsp;&nbsp;&nbsp;.générer la base de données ./sql\_scripts/main.sql</br>
&nbsp;&nbsp;&nbsp;&nbsp;.démarrer le serveur web ./siteweb/serveur\_applicatif.py</br>



# Modèle entité-relation
![alt text](https://i.imgur.com/jvoIsEs.jpg)

# Modèle relationel
**Abonnés** ('Aid : int', Nom : char(20), Téléphone : char(8), Point de raccordement : char(9))<br>
**Consommations mensuelles** ('Aid : int', 'Mois : int', Puissance (kW/h) : real)<br>

**Équipements** ('Eid : char(9)')<br>
**Centrales** ('Eid : char(9)', Poste source : char(9), Categorie : enum, Puissance (MW) : real)<br> 
**Lignes** ('Eid : char(9)', Tension : int, Courant : int, Categorie : enum, Longueur : int, Poste 1 : char(9), Poste 2 : char(9))<br>

**Supports** ('Eid : char(9)', Ligne : char(9), Lieu : Geometry, Categorie : enum)<br>
**Categories de supports** ('Categorie : enum', Portée : int, Poids : int, Hauteur : int)<br>

**Postes** ('Eid : char(9)', Lieu : Geometry)<br>
**Sources** ('Eid : char(9)', Centrale : char(9))<br>
**Satellites** ('Eid : char(9)')<br>
**Stratégiques** ('Eid : char(9)')<br>
**Transformateurs sur poteau de bois** ('Eid : char(9)')<br>
**Points de raccordement** ('Eid : char(9)', Abonne : int)<br>

**Bris** ('Eid : char(9)', 'Début : DateTime', Fin : DateTime)<br>


**Villes** ('Nom : char(20)', Lieu : Geometry)<br>
**Conditions météorologiques** ('Ville : char(20)', 'Heure : DateTime', Température : int, Taux d’humidité : real, Pression atmosphérique : real, Chute de pluie : int, Chute de neige : int, Couverture de neige : int)<br>


