"""
Graph generators
"""

import networkx as nx
import numpy as np
import random

def preferential_generator(n: int, a: float) -> nx.Graph:
    """
    Generates a graph with n nodes using preferential attachment

    Parameters
    ----------
    n : int
        number of nodes
    a : float
        exponent to modify probability each new node connects to an existing node

    Returns
    -------
    nx.Graph

    """

    G = nx.Graph()
    G.add_node(0)

    if n == 1:
        return G

    G.add_edge(0, 1)

    for i in list(range(n))[2:]:
        
        p_i = []

        for node in G.nodes:

            # probability new node connects to existing node
            n = ((G.degree[node] ** a) + 1)
            d = sum([(G.degree[n] ** a) + 1 for n in G.nodes])

            p = n / d

            p_i.append(p)

        random_node = np.random.choice(list(G.nodes), size=1, p=p_i)[0]

        G.add_edge(i, random_node)

    return G

def random_walk_generator(n: int, p: float) -> nx.Graph:
    """
    Generate a graph with n nodes with each node connecting
    to a random node, and p probability of attaching to
    a random nodes neighbor; otherwise attach to a second
    random node.

    Parameters
    ----------
    n : int
        number of nodes
    p : float
        probability node connects to a neighbor of a random node

    Returns
    -------
    nx.Graph
    
    """
    
    # since we add two edges every time, it's just a complete graph for n <= 3
    if n <= 3:
        return nx.complete_graph(n)
    
    G = nx.complete_graph(3)

    for i in list(range(n))[3:]:

        existing_nodes = list(G.nodes)
        random_node = random.choice(existing_nodes)

        # if r < p, connect to random neighbor; else connect to random node
        if random.random() > p:
            neighbors = list(G.neighbors(random_node))
            random_node2 = random.choice(neighbors)
        else:
            # remove first random node from list
            existing_nodes.remove(random_node)

            # get second random node
            random_node2 = random.choice(existing_nodes)

        # add our node and edges
        G.add_node(i)
        G.add_edge(i, random_node)
        G.add_edge(i, random_node2)

    
    return G
