'''
    Class representing each node in the graph
'''
class Node:
    def __init__(self,adj):
        self.visited = 0
        self.start = 0
        self.adj = adj
        self.end = 0
        self.prev = None

'''
    Adjacency List representation. G is a list of nodes.
'''
class Graph:
    def __init__(self):
        self.list = []
        self.time = 0
    
    def addNode(self,node):
        self.list.append(node)

    def __findCycle(self,u):
        u.visited = 1
        u.start = self.time
        self.time += 1
        for v in u.adj:
            n = self.list[v]
            if n.visited == 0:
                n.prev = u
                self.__findCycle(n)
            elif n != u.prev:
                print("Cycle found")
                exit(0)
        u.end = self.time
        self.time += 1
    
    def findCycle(self,source):
        self.__findCycle(self.list[source])
    

def main():
    
    G = Graph() 

    # Read input from text file
    file=open('./input.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for node in line.split(' '):
            if first:
                first=False
                continue
            adjacentVertices.append(int(node))
        n = Node(adjacentVertices)
        G.addNode(n)
    file.close()

    # Call the findCycle on the graph by passing source vertex as argument
    G.findCycle(1)

    print("Cylcle not found")

main()