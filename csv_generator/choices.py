

"""
    Brief: This class is a container for data and rules
           regarding the database "reseau_electrique".
           It is used by Graph and its associated classes.
"""
class Choices:
    """
        Brief: This list represents all the subsets of "Equipements"
    """
    equipements = [
        'LIGNES',
        'CENTRALES',
        'SUPPORTS',
        'POSTES'
    ]

    """
        Brief: This list represents all the subsets of "Postes" which is itself
               a subset of "Equipements"
    """
    postes = [
        'SOURCES',
        'STRATEGIQUES',
        'SATELLITES',
        'TRANSFORMATEURS',
        'POINTSRACCORDEMENT'
    ]

    misc = [
        'EQUIPEMENTS',
        'ABONNES',
        'CONSOMMATIONSMENSUELLES',
        'CATEGORIESDESUPPORTS',
        'CONDITIONSMETEOROLOGIQUES',
        'BRIS'
    ]
    
    """
        Brief: This list represents all the possible "Categories" of "Centrales" 
    """
    centrales =  [
        'PARC EOLIEN',
        'CENTRALE THERMIQUE',
        'CENTRALE HYDROELECTRIQUE',
        'CENTRALE SOLAIRE PHOTOVOLTAIQUE'
    ]
    
    """
        Brief: This list represents all the possible "Categories" of "Lignes" 
    """
    lignes =  [
        'CABLE CONDUCTEUR',
        'CABLE DE GARDE',
        'HAUBAN'
    ]

    supports = [
        ['SOUS-TERRAIN', 100, 0, 0],
        ['PYLONE MAE WEST', 120, 100, 100],
        ['PYLONE CLASSIQUE', 110, 120, 200],
        ['PYLONE HAUBANE EN V', 100, 100, 100],
        ['PYLONE TUBULAIRE', 200, 150, 100],
        ['PYLONE HAUBANE A CHAINETTE',220, 100, 90],
        ['PYLONE DE TRAVERSEE', 120, 110, 100],
        ['PYLONE A TREILLIS', 100, 100, 90],
        ['POTEAU DE BOIS', 20, 60, 5]
    ]
   
    """
        Brief: This dictionary keeps the maximum number of leaving edges
               for every type of Node.
    """
    max_output_edges = {
        'SOURCES' : 4,
        'STRATEGIQUES' : 4,
        'SATELLITES' : 4,
        'TRANSFORMATEURS' : 6,
        'POINTSRACCORDEMENT' : 0
    }

    """
        Brief: This dictionary keeps all the prefixes associated with
               the different types of "Equipements". Those types are
               used to generate ids.
    """
    prefix_categorie = {"SOURCES" : "SOUR",
                        "STRATEGIQUES" : "STRA",
                        "SATELLITES" : "SATE",
                        "TRANSFORMATEURS" : "TRAN",
                        "POINTSRACCORDEMENT" : "RACC",
                        "CENTRALES" : "CENT",
                        "LIGNES" : "LIGN",
                        "SUPPORTS" : "SUPP"}
    """
        Arg categorie [string]: The type of a given "Equipement" type
        Arg index [int]: A number that represents the current count for the specified "Categorie"
        Brief: This method creates ids for "Equipements". Every type of "Equipement" has
                its specific prefix and in order to keep every id unique, the prefix is
                concatenated with the current number of "Equipements" of the current "Categorie"
    """
    @staticmethod
    def e_id_gen(categorie, index):
        prefix = Choices.prefix_categorie[categorie]
        return "{0}{1:05d}".format(prefix, index)


