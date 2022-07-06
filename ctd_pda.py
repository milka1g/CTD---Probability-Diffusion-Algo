# A probability diffusion algorithm. A probability score is propagated through a network structure starting
# from an initial starting node (sn). In lines x–yy, probability is split preferentially between unvisited network neighbors
# of the starting node by edge weight and propagated recursively to secondary neighbors until the probability being diffused
# is less than a defined parameter, thresholdDiff (default set to 0.01). If the starting node, sn, has no unvisited
# neighbors, p1 is distributed uniformly amongst all unvisited nodes, regardless of proximity to sn

"""
:param p1: [float]–probability to be divided across network nodes
:param tresholdDiff: [float]–probability threshold at which diffusion truncates
:param sn: [string]–the node name of an initial starting node // index
:param G: [hash]–node names are KEYS, node probabilities are VALUES //{int-float}
:param vN: [vector]–visited nodes, a subset of node names (KEYS) in G //[list]
:param adj_mat: [matrix]–the weighted adjacency matrix of the network //pd
"""

def DIFFUSE_PROBABILITY_RECURSIVE(startingNode, G, visitedNodes, adj_mat, tresholdDiff=0.01, alpha=0.5, p1=0.5):
    # unvisited neighbors of sn
    unvisitedNodes = set(G.keys()).difference(visitedNodes)

    unvisitedNeighbors = [un for un in unvisitedNodes if adj_mat.iloc[startingNode, un] > 0]

    unvisitedNeighborsEdgeWeights = []
    for un in unvisitedNeighbors:
        unvisitedNeighborsEdgeWeights.append(adj_mat.iloc[startingNode, un])

    if len(unvisitedNeighbors):
        sum_weights = sum(unvisitedNeighborsEdgeWeights)
        for un in unvisitedNeighbors:
            inherited_prob = p1*(adj_mat.iloc[startingNode, un]/sum_weights)
            G[un] = G[un] + inherited_prob
            if inherited_prob * alpha > tresholdDiff:
                G[un] = G[un] - inherited_prob * alpha
                visitedNodes.add(un)
                DIFFUSE_PROBABILITY_RECURSIVE(un, G, visitedNodes, adj_mat, p1=inherited_prob*alpha)
    else:
        for un in unvisitedNodes:
            G[un] = G[un] + p1/len(unvisitedNodes)
        return


def DIFFUSE_PROBABILITY_ITERATIVE(sn, G, vN, adj_mat, tresholdDiff=0.01, alpha=0.5, p1=0.5):
    pass