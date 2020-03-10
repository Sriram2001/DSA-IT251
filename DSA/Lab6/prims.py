import heapq


class Vertex:
    def __init__(self, id, cost, adj):
        self.id = id
        self.cost = cost
        self.parent = self
        self.adj = adj  # List of node id's adjacent to this vertex


def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = []
    heap = []
    Nodes = []
    T = set()
    seen = set()
    s = 0

    file = open('input.txt', 'r')
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
        if u[0] == node.cost and node.id not in seen:
            seen.add(node.id)
            if node != node.parent:
                T.add((node.id, node.parent.id))
            for j in range(len(node.adj)):
                v = Nodes[node.adj[j][0]]
                new_dist = node.adj[j][1]
                if v.cost > new_dist:
                    v.cost = new_dist
                    heapq.heappush(heap, (v.cost, v.id))
                    v.parent = node

    for vertex in T:
        print(vertex)


if __name__ == '__main__':
    main()
