import pandas as pd
import random
from ctd_pda import *
import os


def test():
    ROOT_DIR = os.path.dirname(os.path.abspath("tests.py"))
    dest = f"{ROOT_DIR}/graphs"
    df = pd.read_csv(f"{dest}/gnp_graph_10_nodes_0.4_prob.csv")

    #print(df)
    #print(df.shape)
    #print(df.columns)

    size = len(df.columns)
    #sN = 0
    sN = random.randint(0, size)
    G = { n : 0 for n in range(0,len(df.columns))}
    vN = set()
    vN.add(sN)

    DIFFUSE_PROBABILITY_RECURSIVE(sN, G, vN, df)
    print(G)  #HOW TO TEST IF THIS IS ANY GOOD?!?!?!?!?!?! TODO


if __name__ == "__main__":
    test()