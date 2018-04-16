Le script main.sql se charge d'exécuter tous les autres scripts dans un ordre
logique. Nous documenterons chacun de ces scripts en suivant cet ordre.


A_init.sql
----------
    Ce script se charge d'initialiser la base de données à zéro.
    


B_CreateTables.sql
------------------
    Ce script se charge strictement de créer les tables en précisant
    leurs attribut typés.


C_PrimaryKeys.sql
-----------------
    Ce script assigne les clés primaires et les champs UNIQUE de chaque table.


D_ForeignKeys.sql
-----------------
    Ce script ajoute les contraintes de référence à la base de données.


E_Triggers.sql    
------------------
    Ce script se charge de préciser toutes les conditions additionnelles à la
    base de données. Chaque gachette appelle une procédure et chaque procédure
    est appelée par une gachette d'insertion et une autre de mise à jour.
    Voici une description de chacunes des procédures.
    
    .equipementValide:
     Vérifier que chaque équipement est bien d'un type dérivé de équipement.
    
    .posteValide:
     Vérifier que chaque poste est bien d'un type dérivé de postes.
    
    .prevenirSuperpositionVilles:
     Vérifier que deux villes ne sont pas géographiquement superposées.
     En plus d'être illogique, cela permettrait à un équipement d'être
     situé dans plusieurs villes simultannément.
    
    .verifierLigne:
     Cette procédure vérifie la validité des lignes qui est définie selon
     plusieurs critères.
     -Une ligne de doit pas relier deux fois le même poste.
     -Une ligne ne peut pas quitter un point de raccordement
     -Une ligne ne peut pas rejoindre un point source
     -Il ne peut exister plus de 6 lignes qui quittent un transformateur sur
      poteau de bois.
     -Il ne peut exister plus de 3 lignes qui quittent un poste source,
      un poste stratégique ou un poste satellite.
     -Le descendant d'un transformateur ne peut être qu'un autre
      transformateur sur poteau de bois ou un point de raccordement
     -Le descendant d'un poste stratégique, satellite ne peut pas être un
      point de raccordement.
    
    Toutes les autres gachettes se chargent de vérifier que chaque type
    hérité d'équipement a un identificateur qui correspond aux normes
    préétablies. Soit, d'être une chaîne de 9 caractères se terminant
    par 5 chiffres et commençant par 4 lettre déterminant le type.
    Centrale: "CENT"
    Lignes: "LIGN"
    PointsDeRaccordement: "RACC"
    Satellites: "SATE"
    Sources: "SOUR"
    Stratégiques: "STRA"
    Supports: "SUPP"
    TransformateursSurPoteauDeBois: "TRAN"
    
    Bien que la nature de ces identificateurs crée de la redondance
    dans la base de données, ils en simplifient grandement l'accès
    et l'identification des données.


F_InsertInto.sql
----------------
    Ce script charge le contenu de tous les fichiers CSV dans les 
    tables prévues à cet effet.


G_Indexes.sql
-------------
    Ce script crée les index de la base de données. Voici un description
    de tous ces index.
    
    .LignesP1:
     L'index de hachage sur Lignes(Poste1) est particulièrement
     utile pour l'algorithme récursif permettant de trouver toutes les 
     feuilles descendantes d'un noeud donné.
     (requetes/listeBris.py/ListeBris.__trouver_raccordements(self, eid, raccordements))
     Il commence ainsi:
     On trouve les lignes qui quittent le poste en question.  
     Lignes(Poste1) étant l'identificateur du poste de départ de la ligne,
     on n'a qu'à trouver les lignes ayant comme Poste1 l'identificateur de
     notre poste, ce qui se fait en temps constant grâce à l'index de hachage.
     Une fois les lignes trouvées, leur attribut Poste2, déjà accessible,
     représente le noeud d'arrivée. On vérifie donc si celui-ci est une
     feuille (de type point de raccordement). Si c'est le cas, on le
     conserve et sinon, on cherche les lignes qui le quittent. Pour ce
     faire, on cherche les lignes ayant comme Poste1 l'identificateur de
     notre nouveau poste. L'algorithme répète donc ces opérations jusqu'à
     ce que tous les postes trouvées soient des points de raccordement. On
     constate donc qu'il requiert une grande quantité de requêtes d'égalité
     sur Lignes(Poste1).

    .AbbRac:
     Cet index est utile pour la fonction
     requetes/listeBris.py/ListeBris.__trouver_abonnes_racc(self, raccordements)
     Au moment de l'appel de la fonction on a une liste d'identificateurs de
     points de raccordements. Elle retourne une liste des abonnés associés
     à chaque point de raccordement. Il sera donc nécessaire de faire une
     grande quantité de requêtes d'égalité sur Abonnes(PointDeRaccordement).
     La recherche inversée avec un index sur PointsDeRaccordement(Abonne)
     aurait été tout aussi valide, mais notre choix sera expliqué* plus
     précisément sous peu.

    .villeMeteo:
     Cet index de hachage sur ConsitionsMeteorologiques(Ville) permet
     de connaître rapidement les conditions météorologiques d'une ville. Voir
     requetes/listeBris.py/ListeBris.__trouver_meteo(self, ville, heure).
     Le requête complète dépend aussi de l'heure donnée, mais celle-ci
     étant passée dans la fonction DATEDIFF, il semble qu'aucun index
     n'aurait pu aider la partie de cette requête.

    .EidLignes:
     Cet index de hachage sur Lignes(Eid) est utilisé à plusieurs reprises.
     Notamment:
     -requetes/listeBris.py/ListeBris.__trouver_ville(self, eid) pour trouver
      la ville où une ligne se situe
     -requetes/listeBris.py/ListeBris.__get_equipement_nom(self, eid) pour trouver
      la catégorie d'une ligne
     -requetes/listeBris.py/ListeBris.__trouver_raccordement(self, eid, raccordements)
      Pour le cas où l'équipement donné est un support, on devrait donc trouver
      la ligne qu'il supporte.
      Pour le cas où l'équipement donné est une ligne, on devrait la localiser
      dans la table des lignes afin de trouver son poste de destination
     Tous ces cas de requêtes d'égalité sur Lignes(Eid) combinées nous ont paru
     suffisants pour ajouter cet index.

    .NomVilles:
     Cet index de hachage sur Villes(Nom) est utilisé pour afficher la page
     listeEquipements.html qui utilise la fonction
     requetes/listeEquipements.py/ListeEquipements.get_data(self, ville).
     Pour un nom de ville donné, la fonction doit trouver le polygone
     représentant ses frontières géographiques. Pour ce faire, une requête
     d'égalité sur Villes(Nom) est nécessaire et cela explique l'utilisation
     d'un index de hachage.

    .Les deux derniers index ont été créés afin d'accélérer les requêtes
     nécessaires pour afficher la page listeVilles.html. La fonction python
     qui les exécute est 
     requetes/listeVilles.py/ListeVilles.get_data(self) et permet de connaître
     la consommation totale de tous les abonnés de chaque ville. La fonction
     doit donc, pour chaque ville, trouver tous les postes de type point de
     raccordement qui s'y trouvent, trouver les abonnés associés à ces points de
     raccordement, et faire une moyenne de l'utilisation mensuelle de l'abonné
     et sommer toutes les moyennes trouvées pour une ville. La fonction
     retourne ensuite la liste des villes en ordre de consommation globale.
     Cette grande requête se décompose comme suit:
     Elle commence par un balayage des villes ce qui ne nécéessite aucun index.
     Ensuite elle effectue une jointure entre Postes et Villes. Celle-ci,
     applique une requête de gamme sur Postes(Eid) et c'est pourquoi nous
     avons mis un index B+ sur cet attribut. La même jointure utilise aussi 
     une autre fonction spécifique au type GEOMETRY qui ne semble pas pouvoir
     bénéficier d'un index. Ensuite, pour chaque tuple trouvé, on applique une 
     requête d'égalité sur Abonnes(PointDeRaccordement). Heureusement, cet
     index existe déjà et l'existence de cett requête explique* le choix fait
     pour AbbRac. De plus, on doit faire une requête d'égalité sur 
     ConsommationsMensuelles(Aid), ce qui justifie l'index AidConso.
     Malgré tout, cette requête demeure lente et nous pensons qu'une architecture
     différente des tables de la base de données aurait pu améliorer la rapidité
     de l'accès à cette information. Par exemple, de calculer cette information
     pour chaque ville périodiquement à chaque mois serait une solution
     amplement correcte.
