Cette section se charge de créer des données cohérentes pour
la base de données reseau_electrique.


main.py
-------

    C'est le fichier principal et il permet d'enclencher la génération.


graph.py
--------

    Ce fichier contient la classe Graph qui implémente un arbre n-aire
    d'équipements du réseau électrique interconnectés par les lignes électriques. 
    Le graphe est borné par des coordonnées géographiques ainsi que des
    limites temporelles.


edge.py
-------

    Ce fichier contient la classe Edge qui implémente les arcs du graphe
    ou plus concrètement, les lignes du réseau électrique.

node.py
-------

    Ce fichier contient la classe Node qui implémente les noeuds du graphe
    ou plus concrètement, tous les types de postes exceptés les postes sources.


source.py
---------

    Ce fichier contient la classe Source qui implémente les noeuds racines
    du graphe ou plus concrètement, les postes sources qui sont reliés
    logiquement à des centrales.


abonnes.py
----------
    
    Ce fichier contient la classe Abonnes qui implémente le concept d'abonné
     et qui génère les données nécessaires pour un abonné au réseau électrique.
    Les noms possibles des clients sont puisés à ./data/names.pkl

bris.py
-------

    Ce fichier permet de générer aléatoirement des bris pour les équipements
    du réseau électrique.


choices.py
----------

    Ce fichier contient les données caractérisant les valeurs possibles des
    différents types du réseau électrique. Les aglorithmes de génération
    aléatoires y puisent donc les choix possibles.


city.py
-------
    
    Ce fichier permet de créer la grande région du réseau électrique qui
    sera composée de plusieurs villes. Les noms de ville sont puisés à
    ./data/cities.pkl.


meteo.py
--------

    Ce fichier permet de créer des conditions météorologiques pour toutes
    les villes et toutes les heures du graphe.


util.py
-------

    Ce fichier contient les fonctions utilitaires à la création du graphe.
