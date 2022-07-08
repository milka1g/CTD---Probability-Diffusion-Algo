# A probability diffusion algorithm. A probability score is propagated through a network structure starting
# from an initial starting node (sn). In lines x–yy, probability is split preferentially between unvisited network NEIGHBORS
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
from queue import LifoQueue


def DIFFUSE_PROBABILITY_RECURSIVE(startingNode, G, visitedNodes, adj_mat, tresholdDiff=0.01, alpha=0.5, p1=0.5):
    unvisitedNodes = set(G.keys()).difference(visitedNodes)

    unvisitedNeighbors = set(filter(lambda x: adj_mat.iloc[startingNode, x] > 0, unvisitedNodes))

    unvisitedNeighborsEdgeWeights = []
    for un in unvisitedNeighbors:
        unvisitedNeighborsEdgeWeights.append(adj_mat.iloc[startingNode, un])

    sum_weights = sum(unvisitedNeighborsEdgeWeights)
    if len(unvisitedNeighbors) > 0:
        for un in unvisitedNeighbors:
            inherited_prob = p1/sum_weights*adj_mat.iloc[startingNode, un]
            G[un] = G[un] + inherited_prob
            if inherited_prob * alpha > tresholdDiff:
                G[un] = G[un] - inherited_prob * alpha
                #visitedNodes.add(un) #BAD -> node A can be neighbor of B and C and if you visit it from
                # B it doesn't mean you can't visit it from C later when recursion unwinds
                #it should just prevent us from making cycles when distributing p
                DIFFUSE_PROBABILITY_RECURSIVE(un, G, visitedNodes.union({un}), adj_mat, p1=inherited_prob*alpha)
    else:
        for un in unvisitedNodes:
            G[un] = G[un] + p1/len(unvisitedNodes)
        return


def DIFFUSE_PROBABILITY_ITERATIVE(startingNode, G, visitedNodes, adj_mat, tresholdDiff=0.01, alpha=0.5, p1=0.5):
    stack = LifoQueue()
    stack.put([startingNode, visitedNodes, p1])

    while stack.qsize() > 0:
        startingNode, visitedNodes, p1 = stack.get()
        unvisitedNodes = set(G.keys()).difference(visitedNodes)
        unvisitedNeighbors = set(filter(lambda x: adj_mat.iloc[startingNode, x] > 0, unvisitedNodes))
        unvisitedNeighborsEdgeWeights = []
        for un in unvisitedNeighbors:
            unvisitedNeighborsEdgeWeights.append(adj_mat.iloc[startingNode, un])
        sum_weights = sum(unvisitedNeighborsEdgeWeights)

        if len(unvisitedNeighbors) > 0:
            for un in unvisitedNeighbors:
                inherited_prob = p1 / sum_weights * adj_mat.iloc[startingNode, un]
                G[un] = G[un] + inherited_prob
                if inherited_prob * alpha > tresholdDiff:
                    G[un] = G[un] - inherited_prob * alpha
                    stack.put([un, visitedNodes.union({un}), inherited_prob * alpha])
        else:
            for un in unvisitedNodes:
                G[un] = G[un] + p1 / len(unvisitedNodes)


if __name__ == "__main__":
    DIFFUSE_PROBABILITY_ITERATIVE()