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

    def __DFS(self,u):
        u.visited = 1
        u.start = self.time
        self.time += 1
        print('Visited node {}\n'.format(self.list.index(u)))
        for v in u.adj:
            n = self.list[v]
            if n.visited == 0:
                n.prev = u
                self.__DFS(n)
        u.end = self.time
        self.time += 1
    
    def DFS(self,source):
        self.__DFS(self.list[source])
    

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

    # Call the DFS on the graph by passing source vertex as argument
    G.DFS(1)

main()