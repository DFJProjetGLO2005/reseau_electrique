from graph import Graph
from bris import gen_bris
from meteo import gen_meteo
from util import gen_categories_supports


"""
    Brief: Ce fichier est chargé de créer tous les fichiers CSV nécessaires pour
           la construction de la base de données. Il génère une instance de Graph
           qui accumulera progressivement l'ensemble des données nécessaires tout
           en s'assurant qu'elles sont logiquement liées et qu'elles respectent les
           critères de validité de la base de données.
        
"""
graph = Graph(source_qty=30, time_limits=(2016,2018))
gen_bris(graph)
gen_meteo(graph)
gen_categories_supports(graph)
graph.generate_csv()
