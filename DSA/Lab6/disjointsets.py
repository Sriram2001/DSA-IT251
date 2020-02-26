class Node:
    def __init__(self, x):
        self.val = x
        self.parent = self
        self.rank = 0

    def __str__(self):
        return str(self.val)


class DisjointSets:
    def __init__(self):
        pass

    def makeset(self, x):
        return Node(x)

    def findset(self, x: Node) -> Node:
        if x.parent == x:
            return x
        x.parent = self.findset(x.parent)
        return x.parent

    def union(self, x: Node, y: Node) -> None:
        a = self.findset(x)
        b = self.findset(y)
        if a.rank > b.rank:
            b.parent = a
        elif b.rank > a.rank:
            a.parent = b
        else:
            a.parent = b
            b.rank += 1


def main():
    ds = DisjointSets()

    nodes = []
    for i in range(10):
        node = ds.makeset(i)
        nodes.append(node)

    ds.union(nodes[0], nodes[1])
    print(ds.findset(nodes[0]))    # Should print 1
    ds.union(nodes[0], nodes[2])
    print(ds.findset(nodes[2]))    # Should print 1
    ''' Add more tests!'''


if __name__ == '__main__':
    main()
