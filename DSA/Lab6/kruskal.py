from disjointsets import DisjointSets

def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = []
    V = []
    E = set()
    T = set()
    id = 0

    ds = DisjointSets()

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
            E.add((frozenset([id, int(node)]), int(weight)))
        G.append(adjacentVertices)
        id += 1

    file.close()

    E = sorted(E, key=lambda x: x[1])

    for i in range(len(G)):
        v = ds.makeset(i)
        V.append(v)

    for edge in E:
        [a, b] = edge[0]
        if len(T) == len(G)-1:
            break
        if ds.findset(V[a]) != ds.findset(V[b]):
            T.add(edge[0])
            ds.union(V[a], V[b])

    print("The edges in the minimum spanning tree are:")
    for edge in T:
        [a, b] = edge
        print(a, b)


if __name__ == '__main__':
    main()
