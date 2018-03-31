import random
from choices import Choices
from abonnes import gen_abonnnes
import util


"""
    Brief: This class represents a node that can be created by Graph
           Node can be any kind of "Poste", except a "Source"
           Therefore, Nodes are never a root and can be a leaf
"""
class Node:
    """
        Arg graph[GRAPH]: This is the associated Graph that asks the creation of a Node  
        Arg prev_node[string]: This is the id of this node's predecessor
        Brief: This constructor, creates a node with with its corresponding tuples and
               ends with creating its possible leaving edges.
    """
    def __init__(self, graph, prev_node):
        self.graph = graph
        self.prev_node = prev_node
        self.p_id = ""
        self.add_tuples()
        self.create_edges()

    """
        Brief: This method creates the nodes tuples and saves them within the associated Graph
    """
    def add_tuples(self):
        self.categorie = self.random_categorie()
        self.p_id = Choices.e_id_gen(self.categorie, len(self.graph.tuples[self.categorie]))
        lieu = util.create_location(self.graph.boundaries)
        self.graph.tuples["EQUIPEMENTS"].append([self.p_id])
        self.graph.tuples["POSTES"].append([self.p_id, lieu])
        self.graph.tuples[self.categorie].append([self.p_id])
        if self.categorie == "POINTSRACCORDEMENT":
            a_id = gen_abonnnes(self.p_id, self.graph)
            self.graph.tuples[self.categorie][-1] += [a_id]


    """
        Brief: This method determines the type of the current node depending on the type of the previous node.
               For every kind of previous node, a differently weighted random function will decide what will
               be the type of the current node. The goal of the weighted random functions is to make sure
               the resulting graph meets the pre-established databases rules and to make sure the graph
               can't be too big.
    """
    def random_categorie(self):
        return { "SOUR" : random.choice(["STRATEGIQUES", "SATELLITES"]),
                 "STRA" : random.choice(["STRATEGIQUES"] + ["SATELLITES"] + ["TRANSFORMATEURS"] * 5),
                 "SATE" : random.choice(["STRATEGIQUES"] + ["SATELLITES"] * 2 + ["TRANSFORMATEURS"] * 10),
                 "TRAN" : random.choice(["TRANSFORMATEURS"] + ["POINTSRACCORDEMENT"] * 3)
                 }[self.prev_node[0:4]] 

    """
        Brief: This method creates a random number of edges. The number will vary according
               to the current node's type. Here are the possibilities:
               Point de raccordement: 0
               Transformateur: 1 - 6
               Others: 1 - 4
    """
    def create_edges(self):
        max_output_edges = Choices.max_output_edges[self.categorie]
        if max_output_edges > 0:
            edge_qty = random.randint(1, max_output_edges)
            for e in range(edge_qty):
                self.graph.add_edge(self.p_id)
    
    """
        Brief: This getter lets the uses, which will in this case be the Graph, get this node's id in
               order to create the next node accordingly.
    """
    def get_id(self):
        return self.p_id
    
    
