import pandas as pd
import random
from ctd_pda import *
from plotting import *
import os


def test():
    ROOT_DIR = os.path.dirname(os.path.abspath("tests.py"))
    dest = f"{ROOT_DIR}/graphs"
    for filename in os.listdir(dest):
        print(f"Graph: {filename}")
        df = pd.read_csv(f"{dest}/{filename}")
        df.columns = df.columns.astype(int)

        size = len(df.columns)
        sN = 0
        startingProbability = 0.5
        #sN = random.randint(0, size)

        Giter = { n : 0 for n in range(0,len(df.columns))}
        Grec = {n: 0 for n in range(0, len(df.columns))}

        Giter[sN] = startingProbability
        Grec[sN] = startingProbability

        vNiter = set()
        vNiter.add(sN)

        vNrec = set()
        vNrec.add(sN)
        DIFFUSE_PROBABILITY_RECURSIVE(sN, Grec, vNrec, df, p1=startingProbability)
        DIFFUSE_PROBABILITY_ITERATIVE(sN, Giter, vNiter, df, p1=startingProbability)
        print(f"G iterative: {Giter}")
        print(f"G recursive: {Grec}")

        # if "10" in filename:
        #     plotGraph(df, Giter, sN, startingProbability, f"Iterative: {filename}", filename)
        #     plotGraph(df, Grec, sN, startingProbability, f"Recursive {filename}", filename)

if __name__ == "__main__":
    test()