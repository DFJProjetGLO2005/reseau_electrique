Utilisation
------------
Exécuter dans l'ordre:
.csv_generator/main.py avec l'exécutable python pour générer les données
.sql_scripts/main.sql avec l'exécutable mysql pour créer la base de données
.siteweb/serveur_applicatif.py avec l'exécutable python pour démarrer le serveur du siteweb 

__Le mot de passe d'administration nécessaire pour marquer un bris comme résolu est "12345".__


Ce readme n'est que partiel et ses suites se trouvent dans les différents dossiers de ce dépôt.


csv_generator/
--------------
    Ce dossier contient tous les scripts qui créent des données logiques et conformes
    à notre base de données. Bien que installation.py se charge de générer ces données
    il vous est possible de répéter la génération en exécutant csv_generator/main.py.


requetes/
---------
    Ce dossier contient tous les scripts permettant de communiquer avec une instance
    peuplée de notre base de données. Ils servent de pont entre la base de données
    et le serveur applicatif. 


siteweb/
--------
    Ce dossier contient tout ce qui a trait au siteweb et son serveur applicatif.
    Bien que installation.py se charge de démarrer le serveur applicatif, il vous
    est possible de le redémarrer en exécutant siteweb/serveur_applicatif.py

sql_scripts/
------------
    Ce dossier contient tous les scripts sql qui créent la base de données
    selon l'architecture choisie et importe les données créées par les scripts
    contenus dans csv_generator/. Bien que installation.py se charge de créer
    la base de données, il vous est possible de répéter l'opération en
    exécutant sql_scripts/main.sql, si csv_generator a déjà été exécuté
    et donc, que le dossier csv_files/ existe. 
