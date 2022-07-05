# A probability diffusion algorithm. A probability score is propagated through a network structure starting
# from an initial starting node (sn). In lines x–yy, probability is split preferentially between unvisited network neighbors
# of the starting node by edge weight and propagated recursively to secondary neighbors until the probability being diffused
# is less than a defined parameter, thresholdDiff (default set to 0.01). If the starting node, sn, has no unvisited
# neighbors, p1 is distributed uniformly amongst all unvisited nodes, regardless of proximity to sn

"""
:param p1: [float]–probability to be divided across network nodes
:param tresholdDiff: [float]–probability threshold at which diffusion truncates
:param sn: [string]–the node name of an initial starting node
:param G: [hash]–node names are KEYS, node probabilities are VALUES
:param vN: [vector]–visited nodes, a subset of node names (KEYS) in G
:param adj_mat: [matrix]–the weighted adjacency matrix of the network
"""

def DIFFUSE_PROBABILITY_ITERATIVE(p1, tresholdDiff, sn, G, vN, adj_mat):
    pass

def DIFFUSE_PROBABILITY_RECURSIVE(p1, tresholdDiff, sn, G, vN, adj_mat):
    pass