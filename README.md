Utilisation
------------
Pour tester l'application sur votre système, veuillez exécuter le script python **installation.py**.</br>
Celui-ci vous permettra de:</br>
    .générer les données via ./csv\_generator/main.py</br>
    .générer la base de données via ./sql\_scripts/main.sql</br>
    .démarrer le serveur web via ./siteweb/serveur\_applicatif.py</br>
En tout temps, il est possible d'executer manuellement l'un des trois scripts cités ci-haut pour
par exemple démarrer le serveur web sans avoir à répéter la génération de la base de données.

__Le mot de passe d'administration nécessaire pour marquer un bris comme résolu est "12345".__


Ce readme n'est que partiel et ses suites se trouvent dans les différents dossiers de ce dépôt.


csv_generator/
--------------
    Ce dossier contient tous les scripts qui créent des données logiques et conformes
    à notre base de données. Afin de répéter une génération de ces données, il suffit
    d'exécuter le script main.py.


requetes/
---------
    Ce dossier contient tous les scripts permettant de communiquer avec une instance
    peuplée de notre base de données. Ils servent de pont entre la base de données
    et le serveur applicatif.


siteweb/
--------
    Ce dossier contient tout ce qui a trait au siteweb et son serveur applicatif.


sql_scripts/
------------
    Ce dossier contient tous les scripts sql qui créent la base de données
    selon l'architecture choisie et importe les données créées par les scripts
    contenus dans csv_generator/.
