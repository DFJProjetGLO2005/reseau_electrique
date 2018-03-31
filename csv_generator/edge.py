import random
from choices import Choices 
import util

"""
    Arg init_node [string]: This is the id of the Node that creates the current edge
    Brief: An edge is an object used by Graph to link its nodes. In the contexte of
           the database "reseau_electrique" it represents a "Ligne". Every "Ligne"
           has to be associated by supports so this class creates them.
"""
class Edge:
    """
        Arg graph [Graph]: This is the Graph that creates the current Edge
        Arg init_node [string]: This is the id of the initial Node of this Edge
        Brief: It creates the data associated with the Edge and stores it in within
               the associated Graph
    """
    def __init__(self, graph, init_node):
        self.graph = graph
        self.add_tuple(init_node)

    """
        Arg init_node [string]: This is the id of the initial Node of this Edge
        Brief: This method creates the tuple that represents the Edge and saves it
               within the associated Graph. Since an Edge has to lead to another
               Node, this method has to ask the Graph to create this new Node.
    """
    def add_tuple(self, init_node):
        dest_node = self.graph.add_node(init_node)
        l_id = Choices.e_id_gen("LIGNES", len(self.graph.tuples["LIGNES"]))
        self.create_supports(l_id)
        self.graph.tuples["EQUIPEMENTS"].append([l_id])
        self.graph.tuples["LIGNES"].append([l_id,
                                            random.randint(500, 10000),
                                            random.randint(500, 10000),
                                            random.choice(Choices.lignes),
                                            init_node,
                                            dest_node])
    

    """
        Arg l_id [string]: This is the id of the line associated with the supports that will be created
        Brief: This method creates the supports that will hold the current "Ligne"
               Their location is chosen arbitrarily in the graph's area
    """
    def create_supports(self, l_id):
        for i in range(random.randint(1, 10)):
            s_id = Choices.e_id_gen("SUPPORTS", len(self.graph.tuples["SUPPORTS"]))
            lieu = util.create_location(self.graph.boundaries)
            self.graph.tuples["EQUIPEMENTS"].append([s_id])
            self.graph.tuples["SUPPORTS"].append([s_id,
                                                  l_id,
                                                  util.create_location(self.graph.boundaries)])
            
            

            
