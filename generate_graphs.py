import networkx as nx
import random
import os

def generate_random_graphs():
    ROOT_DIR = os.path.dirname(os.path.abspath("generate_graphs.py"))
    dest = f"{ROOT_DIR}/graphs"
    node_count = [10, 60, 500, 1500]
    for nc in node_count:
        probability = 0.25
        G = nx.gnp_random_graph(n=nc, p=probability, seed=42)
        for (u, v, w) in G.edges(data=True):
            w['weight'] = random.randint(0,100)
        df = nx.to_pandas_adjacency(G, dtype=int)
        df.to_csv(f"{dest}/gnp_graph_{nc}_nodeS_{probability}_prob.csv", index=None)

    for nc in node_count:
        probability = 0.4
        G = nx.gnp_random_graph(n=nc, p=probability, seed=42)
        for (u, v, w) in G.edges(data=True):
            w['weight'] = random.randint(0,100)
        df = nx.to_pandas_adjacency(G, dtype=int)
        df.to_csv(f"{dest}/gnp_graph_{nc}_nodes_{probability}_prob.csv", index=None)


    for nc in node_count:
        radius = 0.5
        G = nx.random_geometric_graph(n=nc, radius=radius, seed=42)
        for (u, v, w) in G.edges(data=True):
            w['weight'] = random.randint(0, 100)
        df = nx.to_pandas_adjacency(G, dtype=int)
        df.to_csv(f"{dest}/random_geometric_graph_{nc}_nodes_{radius}_prob.csv", index=None)

    for nc in node_count:
        radius = 0.8
        G = nx.random_geometric_graph(n=nc, radius=radius, seed=42)
        for (u, v, w) in G.edges(data=True):
            w['weight'] = random.randint(0, 100)
        df = nx.to_pandas_adjacency(G, dtype=int)
        df.to_csv(f"{dest}/random_geometric_graph_{nc}_nodes_{radius}_prob.csv", index=None)

    for nc in node_count:
        degree = 2
        G = nx.random_regular_graph(d=degree, n=nc, seed=42)
        for (u, v, w) in G.edges(data=True):
            w['weight'] = random.randint(0, 100)
        df = nx.to_pandas_adjacency(G, dtype=int)
        df.to_csv(f"{dest}/random_regular_graph_{nc}_nodes_{degree}_degree.csv", index=None)

    for nc in node_count:
        degree = 5
        G = nx.random_regular_graph(d=degree, n=nc, seed=42)
        for (u, v, w) in G.edges(data=True):
            w['weight'] = random.randint(0, 100)
        df = nx.to_pandas_adjacency(G, dtype=int)
        df.to_csv(f"{dest}/random_regular_graph_{nc}_nodes_{degree}_degree.csv", index=None)

if __name__ == "__main__":
    generate_random_graphs()
