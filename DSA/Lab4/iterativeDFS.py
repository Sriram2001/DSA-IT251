'''
    Class representing each node in the graph
'''
class Node:
    def __init__(self,adj):
        self.visited = False
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

    def DFS(self,source):
        stack = []
        s = self.list[source]
        stack.append(s)

        while len(stack)!=0:
            s = stack.pop()
            if not s.visited:
                s.visited = True
                print('Visited node {}'.format(self.list.index(s)))
            
            for node in s.adj:
                v = self.list[node]
                if not v.visited:
                    stack.append(v)           
    

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