'''
    Class representing each node in the graph
'''


class Node:
    def __init__(self, adj, id):
        self.visited = 0
        self.start = 0
        self.adj = adj
        self.end = 0
        self.id = id
        self.prev = None


'''
    Adjacency List representation. G is a list of nodes.
'''


class Graph:
    def __init__(self):
        self.list = []  # list of nodes
        self.list_rev = []
        self.time = 0
        self.stack = []

    def addNode(self, node):
        self.list.append(node)

    def rev(self):
        self.list_rev = [Node([], i.id) for i in self.list]

        for i in range(len(self.list)):
            for j in self.list[i].adj:
                self.list_rev[j].adj.append(i)

    def __SCC_no_print(self, u):
        u.visited = 1
        for v in u.adj:
            n = self.list_rev[v]
            if n.visited == 0:
                n.prev = u
                self.__SCC_no_print(n)
        self.stack.append(u.id)

    def __SCC(self, u):
        u.visited = 1
        u.start = self.time
        self.time += 1
        print('Node {}'.format(u.id))
        for v in u.adj:
            n = self.list[v]
            if n.visited == 0:
                n.prev = u
                self.__SCC(n)
        u.end = self.time
        self.time += 1

    def SCC(self):
        SCC_NUMBER = 1
        self.rev()
        for i in self.list_rev:
            if i.visited == 0:
                self.__SCC_no_print(i)

        while len(self.stack) != 0:
            n = self.stack.pop()
            u = self.list[n]

            while(u.visited == 1):
                if len(self.stack) == 0:
                    exit(0)
                n = self.stack.pop()
                u = self.list[n]

            print("\n-------------SCC {}-------------".format(SCC_NUMBER))
            self.__SCC(u)
            SCC_NUMBER += 1


if __name__ == "__main__":

    G = Graph()

    # Read input from text file
    file = open('./input.txt', 'r')
    id = 0
    for line in file:
        line = line.strip()
        adjacentVertices = []
        first = True
        for node in line.split(' '):
            if first:
                first = False
                continue
            adjacentVertices.append(int(node))
        n = Node(adjacentVertices, id)
        G.addNode(n)
        id += 1
    file.close()

    G.SCC()
