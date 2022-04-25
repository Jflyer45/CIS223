import imp
from SearchFunctions import *

task_graph = {'A':['B','C'], 'B':['D','E'], 'C':['A','F'], 'D':['B'], 'E':['B','F'], 'F':['E','C']}
test = {'A':['B','E','F'], 'B':['A','C'], 'C':['B','D'], 'D':['C','G'], 'E':['A'], 'F':['A'], 'G':['D']}
test2 = {1:[2], 2:[1,3,4], 3:[2,4], 4:[2, 5], 5:[4]}
test3 = {3:[6,10], 6:[3,7,9], 7:[6,9], 9:[6,7,10], 10:[3,9]}
test4 = {1:[2], 2:[1,3,4], 3:[2], 4:[2]}
G = {"P":["Q","R"], "Q":["P","R"], "R":["P","Q"]}

# Task 4
G2 = {"A":["C", "B"], "B":["A", "D", "E"], "C":["A", "F"], "D":["B"], "E": ["B", "F"], "F": ["C", "E"]}
G3 = {"a":["b", "c"], "b":["a","e"], "c":["a",'d'], 'd':['c'], 'e': ['b','a']}
#discoveredNodes = BFS(G2, "D")
#print(discoveredNodes)

#print(DFS(test2,5))
print(cycle_detect(task_graph))
print(cycle_detect(test2))
print(cycle_detect(test4))
# print(cycle_detect(task_graph))

