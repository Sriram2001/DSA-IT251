class UndirectedGraph:
    def __init__(self,n):
        self.matrix=[[0 for i in range(n)] for j in range(n)]
        self.list=[[] for j in range(n)]
    
    def addEdge(self,a,b):
        self.matrix[a][b]=1
        self.matrix[b][a]=1
        self.list[a].append(b)
        self.list[b].append(a)
    
    def output(self):
        print("The adjacency matrix is")
        for i in self.matrix:
            for j in i:
                print(j,end=" ")
            print()

        print("\nThe adjacency list is:")
        for i in range(len(self.list)):
            print("Vertex {}:".format(i),end=" ")
            for j in self.list[i]:
                print(j,end=" ")
            print()

if __name__ == "__main__":
    matrix=UndirectedGraph(int(input("Enter the number of vertices: ")))
    print("Enter the edges:")
    inp = input()
    while inp != "":
        a,b=[int(x) for x in inp.split()]
        matrix.addEdge(a,b)
        inp=input()
    matrix.output()