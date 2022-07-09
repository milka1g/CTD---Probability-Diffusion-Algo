import pandas as pd
import random
from ctd_pda import *
from plotting import *
from copy import deepcopy
import os
import dataframe_image as dfi
#performance
import timeit
import tracemalloc


ALPHA = 0.5
STARTING_PROBABILITY = 0.5
EXECUTIONS = 10
ERROR = 1e-5

class Performance:
    def __init__(self, filename="", memoryIter=0, memoryRec=0, timeIter=0, timeRec=0):
        self.filename = filename
        self.memoryIter = memoryIter
        self.memoryRec = memoryRec
        self.timeIter = timeIter
        self.timeRec = timeRec

    def to_dict(self):
        return {
            'filename': self.filename,
            'Mem Iterative [KiB]': self.memoryIter/1024,
            'Mem Recursive [KiB]': self.memoryRec/1024,
            'Verdict Memory': "Iterative" if self.memoryIter < self.memoryRec else "Recursive",
            'Time Iterative [s]': self.timeIter,
            'Time Recursive [s]': self.timeRec,
            'Verdict Time': "Iterative" if self.timeIter < self.timeRec else "Recursive",
        }


def exportResults(performanceData):
    ROOT_DIR = os.path.dirname(os.path.abspath("tests.py"))
    df = pd.DataFrame.from_records([s.to_dict() for s in performanceData])
    dfi.export(df, f"{ROOT_DIR}/performanceResults_A_{ALPHA}.png")

def compareResults(Giter, Grec):
    errors = [abs(x-y) for x,y in zip(Giter, Grec)]
    assert all(e < ERROR for e in errors)

def Gsum(G):
    sum = 0.0
    for node, prob in G.items():
        sum += prob
    print("G sum: ", sum)

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

            Giter = { n : 0 for n in range(0, len(df.columns))}
            Grec = { n : 0 for n in range(0, len(df.columns))}

            Giter[sN] = startingProbability
            Grec[sN] = startingProbability

            vNiter = set()
            vNiter.add(sN)

            vNrec = set()
            vNrec.add(sN)

            tracemalloc.start()
            DIFFUSE_PROBABILITY_RECURSIVE(sN, Grec, deepcopy(vNrec), df, p1=startingProbability, alpha=ALPHA)
            print(f"G recursive: {Grec}")
            Gsum(Grec)
            plotGraph(df, Grec, sN, startingProbability, f"Iterative: {filename}", filename)
            _, peak = tracemalloc.get_traced_memory()
            performance.memoryRec = peak
            tracemalloc.stop()

            tracemalloc.reset_peak()

            tracemalloc.start()
            DIFFUSE_PROBABILITY_ITERATIVE(sN, Giter, deepcopy(vNiter), df, p1=startingProbability, alpha=ALPHA)
            print(f"G iterative: {Giter}")
            Gsum(Giter)
            plotGraph(df, Giter, sN, startingProbability, f"Iterative: {filename}", filename)
            _, peak = tracemalloc.get_traced_memory()
            performance.memoryIter = peak
            tracemalloc.stop()

            compareResults(Giter, Grec)

            Grec = {n: 0 for n in range(0, len(df.columns))}
            Grec[sN] = startingProbability
            elapsedTime = timeit.timeit(
                    stmt=lambda: DIFFUSE_PROBABILITY_RECURSIVE(sN, deepcopy(Grec), deepcopy(vNrec), df, p1=startingProbability, alpha=ALPHA),
                    number=EXECUTIONS)
            performance.timeRec = elapsedTime / EXECUTIONS


            Giter = {n: 0 for n in range(0, len(df.columns))}
            Giter[sN] = startingProbability
            elapsedTime = timeit.timeit(
                stmt=lambda: DIFFUSE_PROBABILITY_ITERATIVE(sN, deepcopy(Giter), deepcopy(vNiter), df, p1=startingProbability, alpha=ALPHA),
                number=EXECUTIONS)
            performance.timeIter = elapsedTime / EXECUTIONS

            performanceData.append(performance)

    exportResults(performanceData)


if __name__ == "__main__":
    test()