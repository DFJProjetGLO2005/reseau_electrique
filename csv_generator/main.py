from graph import Graph
from bris import gen_bris
from meteo import gen_meteo
from util import gen_categories_supports

graph = Graph(source_qty=30, time_limits=(2016,2018))
gen_bris(graph)
gen_meteo(graph)
gen_categories_supports(graph)
graph.generate_csv()
