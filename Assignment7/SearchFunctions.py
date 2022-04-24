def BFS(graph, start):
    frontierQueue = []
    discovered = []
    frontierQueue.append(start)
    discovered.append(start)

    while(len(frontierQueue) != 0):
        current = frontierQueue.pop()
        print(f"We have visited {current}")
        for vertex in graph[current]:
            if(vertex not in discovered):
                frontierQueue.append(vertex)
                discovered.append(vertex)
    return discovered

def DFS():
    pass

def cycle_detect():
    pass