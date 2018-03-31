from graph import Graph
from bris import gen_bris
from meteo import gen_meteo

graph = Graph(source_qty=30, time_limits=(2016,2018))
gen_bris(graph)
gen_meteo(graph)
graph.generate_csv()
