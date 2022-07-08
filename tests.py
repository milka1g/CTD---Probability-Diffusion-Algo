import pandas as pd
import random
from ctd_pda import *
from plotting import *
import os


def test():
    ROOT_DIR = os.path.dirname(os.path.abspath("tests.py"))
    dest = f"{ROOT_DIR}/graphs"
    df = pd.read_csv(f"{dest}/gnp_graph_10_nodes_0.4_prob.csv")
    df.columns = df.columns.astype(int)

    #print(df)
    #print(df.shape)
    #print(df.columns)

    size = len(df.columns)
    sN = 0
    #sN = random.randint(0, size)
    G = { n : 0 for n in range(0,len(df.columns))}
    startingProbability = 0.5
    G[sN] = startingProbability;
    vN = set()
    vN.add(sN)
    print(df)
    #DIFFUSE_PROBABILITY_RECURSIVE(sN, G, vN, df, p1=startingProbability)
    DIFFUSE_PROBABILITY_ITERATIVE(sN, G, vN, df, p1=startingProbability)
    print(G)
    suma = 0
    for node,prob in G.items():
        suma += prob
    print("sum:", suma)
    #plotGraph(df, G, sN, startingProbability, "nameoffilemaybe")


if __name__ == "__main__":
    test()