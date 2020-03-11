import heapq


class Vertex:
    def __init__(self, id, dist, adj):
        self.id = id
        self.dist = dist
        self.flag = False  # Flag variable to check if multiple shortest paths exist from source to this vertex. False by default
        self.parent = self
        self.adj = adj  # List of node id's adjacent to this vertex


def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = []
    heap = []
    Nodes = []
    s = int(input())

    file = open('inp.txt', 'r')
    for line in file:
        line = line.strip()
        adjacentVertices = []
        first = True
        for edge in line.split(' '):
            if first:
                first = False
                continue
            node, weight = edge.split(',')
            adjacentVertices.append((int(node), int(weight)))
        G.append(adjacentVertices)

    file.close()

    for i in range(len(G)):
        id = i
        dist = float('inf')
        heap.append((dist, id))
        Nodes.append(Vertex(id, dist, G[id]))

    heap.append((0, s))
    Nodes[s].dist = 0

    heapq.heapify(heap)

    while(len(heap) > 0):
        u = heapq.heappop(heap)
        node = Nodes[u[1]]
        if u[0] == node.dist:
            for j in range(len(node.adj)):
                v = Nodes[node.adj[j][0]]
                new_dist = node.dist+node.adj[j][1]
                if v.dist > new_dist:
                    v.dist = new_dist
                    heapq.heappush(heap, (v.dist, v.id))
                    v.prev = node
                    if v.flag:
                        v.flag = False
                elif v.dist == new_dist:
                    v.flag = True

    for vertex in Nodes:
        print("ID: {}\tMULTIPLE PATHS:{}\tDIST:{}".format(
            vertex.id, 'Yes' if vertex.flag else 'No', vertex.dist))


if __name__ == '__main__':
    main()
