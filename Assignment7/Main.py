import imp
from SearchFunctions import *

G = {"P":["Q","R"], "Q":["P","R"], "R":["P","Q"]}

# Task 4
G2 = {"A":["C", "B"], "B":["A", "D", "E"], "C":["A", "F"], "D":["B"], "E": ["B", "F"], "F": ["C", "E"]}

discoveredNodes = BFS(G2, "D")
print(discoveredNodes)