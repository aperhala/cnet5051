"""
Null graph models
"""

import networkx as nx
import random


def configuration_model(deg_seq: list[int]) -> nx.MultiGraph:
    """
        Takes a list of integers as a degree sequence and returns a graph where each
        vertex has the assigned degree

        Parameters
        ----------
        deg_seq : list[int]
            a degree sequence for creating a graph
        
        Returns
        -------
        nx.MultiGraph
    """

    if sum(deg_seq) % 2 != 0:
        return None

    size = len(deg_seq)

    G = nx.empty_graph(size, create_using=nx.MultiGraph)

    needs_edges = list(range(size))

    while needs_edges:

        u = needs_edges[random.randint(0, len(needs_edges) - 1)]
        v = needs_edges[random.randint(0, len(needs_edges) - 1)]

        if u == v and G.degree(u) > deg_seq[u] - 2:
            continue

        G.add_edge(u, v)

        if G.degree(u) == deg_seq[u]:
            needs_edges.remove(u)
            if u == v:
                continue

        if G.degree(v) == deg_seq[v]:
            needs_edges.remove(v)

    return G


def chung_lu_model(deg_seq: list[int]) -> nx.Graph:

    """
        Parameters
        ----------
        deg_seq : list[int]

        Returns
        -------
        nx.Graph
    """

    size = len(deg_seq)
    edges = sum(deg_seq) / 2

    G = nx.empty_graph(size)

    edge_probablity = np.zeros((size, size))

    for i in list(range(size)):
        for j in list(range(size)):
            edge_probablity[i][j] = (deg_seq[i] * deg_seq[j]) / (2 * edges)

    nodes = [node for node in G.nodes]

    while edges:

        u, v = random.sample(nodes, 2)

        # no multi edges
        if G.has_edge(u, v):
            continue
        
        # check if we're going to make an edge
        if random.random() > edge_probablity[u][v]:
            continue    
            
        G.add_edge(u, v)

        edges -= 1

    return G
