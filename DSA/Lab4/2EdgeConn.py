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
    Adjacency List representation. G is a list of lists.
'''
class Graph:
    def __init__(self):
        self.list = []
        self.time = 0
        self.source = None
    
    def addNode(self,node):
        self.list.append(node)

    def __TEC(self,u):
        u.visited = 1
        u.start = self.time
        self.time += 1
        sst = u.start

        # print('Visited node {}\n'.format(self.list.index(u)))

        for v in u.adj:
            n = self.list[v]
            if n.visited == 0:
                n.prev = u
                sst=min(self.__TEC(n),sst)
            elif n != u.prev:
                sst = min(sst,n.start)
        u.end = self.time
        self.time += 1

        if sst == u.start and u != self.source:
            print("The graph is not two edge connected")
            exit(0)
        
        return sst
    
    def TEC(self,source):
        self.source = self.list[source]
        self.__TEC(self.list[source])
    

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

    # Call the TEC on the graph by passing source vertex as argument
    G.TEC(1)
    print("Thr graph is two edge connected")

main()