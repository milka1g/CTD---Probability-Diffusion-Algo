import pandas as pd
import random
from ctd_pda import *
from plotting import *
import os
#performance
import timeit
import tracemalloc


ALPHA = 0.5
STARTING_PROBABILITY = 0.5
EXECUTIONS = 10

class Performance:
    def __init__(self, filename="", memoryIter=0, memoryRec=0, timeIter=0, timeRec=0):
        self.filename = filename
        self.memoryIter = memoryIter
        self.memoryRec = memoryRec
        self.timeIter = timeIter
        self.timeRec = timeRec

def test():
    performanceData = []
    ROOT_DIR = os.path.dirname(os.path.abspath("tests.py"))
    dest = f"{ROOT_DIR}/graphs"
    for filename in os.listdir(dest):
        if "10" in filename:
            performance = Performance()
            performance.filename = filename
            print(f"Graph: {filename}")
            df = pd.read_csv(f"{dest}/{filename}")
            df.columns = df.columns.astype(int)

            size = len(df.columns)
            sN = 0
            startingProbability = STARTING_PROBABILITY
            #sN = random.randint(0, size)

            Giter = { n : 0 for n in range(0,len(df.columns))}
            Grec = {n: 0 for n in range(0, len(df.columns))}

            Giter[sN] = startingProbability
            Grec[sN] = startingProbability

            vNiter = set()
            vNiter.add(sN)

            vNrec = set()
            vNrec.add(sN)

            tracemalloc.start()
            DIFFUSE_PROBABILITY_RECURSIVE(sN, Grec, vNrec, df, p1=startingProbability, alpha=ALPHA)
            _, peak = tracemalloc.get_traced_memory()
            performance.memoryRec = peak
            tracemalloc.stop()
            elapsedTime = timeit.timeit(
                    lambda: DIFFUSE_PROBABILITY_RECURSIVE(sN, Grec, vNrec, df, p1=startingProbability, alpha=ALPHA),
                    number=EXECUTIONS)
            performance.timeRec = elapsedTime / EXECUTIONS

            tracemalloc.reset_peak()

            tracemalloc.start()
            DIFFUSE_PROBABILITY_ITERATIVE(sN, Giter, vNiter, df, p1=startingProbability, alpha=ALPHA)
            _, peak = tracemalloc.get_traced_memory()
            performance.memoryIter = peak
            tracemalloc.stop()
            elapsedTime = timeit.timeit(
                lambda: DIFFUSE_PROBABILITY_ITERATIVE(sN, Grec, vNrec, df, p1=startingProbability, alpha=ALPHA),
                number=EXECUTIONS)
            performance.timeIter = elapsedTime / EXECUTIONS

            performanceData.append(performance)

            #print(f"G iterative: {Giter}")
            #print(f"G recursive: {Grec}")

            # if "10" in filename:
            #     plotGraph(df, Giter, sN, startingProbability, f"Iterative: {filename}", filename)
            #     plotGraph(df, Grec, sN, startingProbability, f"Recursive {filename}", filename)

if __name__ == "__main__":
    test()