

class TwoStack:
    
    # variables shared by all two stacks
    # none

    # variables in stacks
    def __init__(self, size1, size2):
        self.max1 = size1
        self.max2 = size2
        self.stacks = []  # creates a new list for each twostack
        self.pointer = 0  # pointer starts at 0

    # methods
    def Push1(self, key):
        # check to see if the list is full
        if (self.isFull1()):  # checking to see if the list is full before adding to it
            print(f"Push 1: Not Allowed {key}")
        else:
            self.stacks.insert(self.pointer, key)
            self.pointer += 1
            # because we are pushing to stack 1 we increse the pointer. by inserting, the list automatically pushes stack two

    def Push2(self, key):
        if (self.isFull2()):  # checking to see if the list is full before adding to it
            print(f"Push 2: Not Allowed {key}")
        else:
            self.stacks.insert(self.pointer, key)
            # we do not need to change the pointer because value was added to stack two

    def Pop1(self):
        valueToReturn = self.stacks.pop(
            self.pointer - 1)  # -1 becuase the pointer is currently pointing at stack two's first value:
        self.pointer -= 1  # decreasing pointer because we took from stack 1
        return valueToReturn  # returns the popped value;

    def Pop2(self):
        if (not self.isEmpty2()):
            valueToReturn = self.stacks.pop(self.pointer)  # pointer is already on the top item in the stack
            # don't need to mess with the pointer becuase it will still be on the top list of the stack
            return valueToReturn
        else: return "Stack is Empty"

    def Peek1(self):
        return self.stacks[
            self.pointer - 1]  # return the valyue that is one under pointer. pointer rests on first value stack 2

    def Peek2(self):
        return self.stacks[self.pointer]  # pointer is on value 2

    def isFull1(self):
        # list one is full if the pointer is  > maxsize
        if (self.pointer >= self.max1):
            return True
        else:
            return False

    def isFull2(self):
        if (len(self.stacks) - self.pointer >= self.max2):
            return True
        else:
            return False

    def isEmpty1(self):
        
        if (self.pointer == 0):
            return True
        else:
            False

    def isEmpty2(self):
        if (len(self.stacks) == self.pointer):
            return True
        else:
            False
            
def BFS(graph, start):
    # Gotta add the starting vertex to the set and queue
    frontierQueue = []
    discovered = []
    frontierQueue.append(start)
    discovered.append(start)

    while(len(frontierQueue) != 0):
        current = frontierQueue.pop()
        print(f"Current Node: {current}")
        for vertex in graph[current]:
            if(vertex not in discovered):
                frontierQueue.append(vertex)
                discovered.append(vertex)
    return discovered



def DFS(graph,startnode):
    vistedverticies = []
    stack = TwoStack(len(graph),100)
    stack.Push1(startnode)
    
    while (not stack.isEmpty1()):
        
        currentvertex = stack.Pop1()
        if (not currentvertex in vistedverticies):
            vistedverticies.append(currentvertex)
            for vertex in graph[currentvertex]:
                stack.Push1(vertex)
        
    return vistedverticies


def cycle_detect(graph):
    visited = []

    for v in graph:
        if v not in visited:
            if iscyclic(graph, v, visited, None) == True:
                return True
    
    return False


def iscyclic(graph, vertex, visited, parent):
    visited.append(vertex)

    for v in graph[vertex]:
        if v not in visited:
            if iscyclic(graph, v, visited, vertex) == True:
                return True

            elif parent != v:
                return True

    return False
        



'''
def isCycle(graph, startnode):
    visited = []
    stack = []
    currentVertex = startnode
    prev = None
    visited.append(currentVertex)

    for v in graph:
        verticies = graph.get(v)
        if cyclic(stack, verticies, visited, prev) == True:
            return True
    
    return False
            

def cyclic(stack, vertex, visited, prev):
    visited.append(vertex)
    for adj in vertex:
        stack.insert(0, adj)

    for v in vertex:
        if v in visited:
            if v == prev:
                pass
            else:
                return True
        elif v not in visited:
            cyclic(stack, v, visited, vertex)
    return False

def cycle_detect(graph):
    visited = []
    stack = []
    for v in graph:
        if isCyclic(graph, v, visited, stack, None) == True:
            return True
        return False

def isCyclic(graph, startnode, visited, stack, parent):
    adj = graph.get(startnode)
    for v in adj:
        stack.append(v)
    for v in stack:
        current = stack.pop(0)
        if current not in visited:
            visited.append(current)
            isCyclic(graph, current, visited, stack, v)
            return False
        else:
            if current == parent:
                return True


# def cyclic(graph, vertex, Isvisited, parent):
#     Isvisited[vertex] = True

#     for i in graph[vertex]:
#         if Isvisited[i] == False:
#             if cyclic(graph, i, Isvisited, vertex):
#                 return True
#         elif parent != i:
#             return False
    
#     return False

# def cycle_detect(graph):
#     visited = {}
#     for v in graph:
#         visited[v] = False

#     for v in graph:
#         if visited[v] == False:
#             if cyclic(graph, v, visited, -1) == True:
#                 return True

#     return False

'''

# def iscycle(graph, startVertex):
#     result = False
#     visited = []
#     stack = []
#     currentVertex = startVertex
#     prev = None
#     for v in graph[currentVertex]:
#         stack.insert(0, v)
#     visited.append(currentVertex)

#     while len(stack) != 0:
#         prev = currentVertex
#         currentVertex = stack.pop()
#         if currentVertex not in visited:
#             visited.append(currentVertex)
#             for i in graph[currentVertex]:
#                 if i != prev:
#                     stack.insert(0, i)
#         elif currentVertex in visited:
#             if currentVertex == prev:
#                 pass
#             else: 
#                 result = True
#                 break

    
#     return result
        

