import os
import util
from choices import Choices
from source import Source
from edge import Edge
from node import Node
from city import CityGenerator


"""
    Brief: This class creates a directed acyclic graph representing an electricity network.
           All its data is kept as tuples that are compatible with the associated database "reseau_electrique"
           Every node is a "Poste"
           Every edge is a "Ligne" and is associated with a variable number of "Supports"
           Every node that is more specifically a "Source" is a root node and is associated with a "Centrale"
           Every node that is more specifically a "Point de raccordement" is a leaf node and is associated with a "Abonne" 
"""
class Graph:
    """
        Arg roots_qty [int]: In this context, it will be the number of Centrales
        Brief: This constructor generates the graph.
    """
    def __init__(self, source_qty, time_limits):
        self.create_csv_dir()
        self.boundaries = CityGenerator().get_general_boundaries()
        self.time_limits = time_limits
        self.init_tuples()
        for i in range(source_qty):
            util.display_loading("Création du graphe", i/source_qty)
            Source(self)


    """
        Brief: This method is called by the constructor and initializes the tuples container
    """
    def init_tuples(self):
        self.tuples = {}
        for t in Choices.equipements + Choices.postes + Choices.misc:
            self.tuples[t] = []

    """
        Arg init_node [string]: The id of the initial node of the edge
        Brief: Creates an edges for the graph which involves creating the next node.
    """
    def add_edge(self, init_node):
        Edge(self, init_node)

    """
        Arg prev_node [string]: The id of the node that leads to the one that will be created
        Brief: Creates a node which involdes creating a variable number of leaving edges 
    """
    def add_node(self, prev_node):
        return Node(self, prev_node).get_id()


    """
        Brief: This getter lets the user access the tuples
    """
    def generate_csv(self):
        n = len(self.tuples.keys())
        i = 0
        for category in self.tuples.keys():
            i += 1
            util.display_loading("Création des fichiers CSV", i/n)
            f = open("../csv_files/" + category + ".csv" , "w", encoding="utf-8")
            for row in self.tuples[category]:
                for value in row:
                    f.write(str(value) + ",")
                f.write("\n")
            f.close()

    """
        Brief: This method creates the directory where the csv files will be stored
    """
    @staticmethod
    def create_csv_dir():
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)
        if not os.path.isdir("../csv_files"): os.mkdir("../csv_files")
                
