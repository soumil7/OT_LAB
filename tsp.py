from sys import maxsize
from itertools import permutations 
v = 4
def tsp(graph, s):
    vertex = []
    for i in range(v):
        if i != s: 
            vertex.append(i)
    min_path = maxsize
    perm = permutations(vertex) 
    for i in perm:
        curr = 0
        k = s
        for j in i:
            curr += graph[k][j] 
            k = j 
        curr += graph[k][s] 
        min_path = min(min_path, curr) 
    return min_path




graph = [[0, 10, 15, 20], [10, 0, 35, 25], 
            [15, 35, 0, 30], [20, 25, 30, 0]]
s = 0
print(tsp(graph, s))