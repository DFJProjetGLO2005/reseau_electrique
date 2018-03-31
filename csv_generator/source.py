import random
from choices import Choices
import util

"""
    Brief: This class creates the root nodes of the Graph
"""
class Source:
    """
        Arg graph [Graph]: This is the Graph that creates the current root node
        Brief: This constructor creates all the data related to this root node
               and then creates the leaving edges.
    """
    def __init__(self, graph):
        self.graph = graph
        self.p_id = ""
        self.add_tuples()
        self.create_edges()

    """
        Brief: This method creates the tuples associated with the current root node.
               The first tuple represents the "Centrale" associated with this root node
               The next tuple represents the node as a "Source"
               The next tuple represents the node in the more general type "Poste"
               The "Source" and "Poste" tuples share the same id
    """
    def add_tuples(self):
        c_id, s_id, p_id = self.create_ids()
        self.p_id = p_id
        c_categorie, c_puissance = self.create_centrale_specs()
        lieu = util.create_location(self.graph.boundaries)
        self.graph.tuples["CENTRALES"].append([c_id,
                                               s_id,
                                               c_categorie,
                                               c_puissance])
        self.graph.tuples["SOURCES"].append([s_id, c_id])
        self.graph.tuples["POSTES"].append([p_id, lieu])
        self.graph.tuples["EQUIPEMENTS"].append([p_id])

    """
        Brief: This method creates the ids needed to create the tuples
    """
    def create_ids(self):
        c_id = Choices.e_id_gen("CENTRALES", len(self.graph.tuples["CENTRALES"]))
        s_id = Choices.e_id_gen("SOURCES", len(self.graph.tuples["SOURCES"]))
        p_id = s_id
        return c_id, s_id, p_id

    """
        Brief: This method creates the specifications for the "Centrale"
    """
    def create_centrale_specs(self):
        c_categorie = random.choice(Choices.centrales), 
        c_puissance = round(random.uniform(4, 5000), 3)
        return c_categorie, c_puissance

    """
        Brief: This method creates the edges that are exiting this root node
    """
    def create_edges(self):
        edge_qty = random.randint(1, Choices.max_output_edges["SOURCES"])
        for e in range(edge_qty):
            self.graph.add_edge(self.p_id)
