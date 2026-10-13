class Graph:
    def __init__(self):
        self.v = 0
        self.e = 0
        self.g = []

    def create(self):
        self.v = int(input("Enter number of vertices: "))
        self.e = int(input("Enter number of edges: "))
        self.g = [[0 for _ in range(self.v)] for _ in range(self.v)]

        for _ in range(self.e):
            print("\nEnter edge details:")
            u = int(input("Enter start vertex: "))
            v = int(input("Enter the end vertex: "))
            w = int(input("Enter weight: "))
            self.g[u][v] = self.g[v][u] = w

    def display(self):
        for i in range(self.v):
            for j in range(self.v):
                print(self.g[i][j], end=" ")
            print()

    def prims(self):
        selected = [False] * self.v
        keys = [999] * self.v
        parent = [-1] * self.v
        keys[0] = 0
        total = 0

        for _ in range(self.v):
            min_key = 999
            u = -1

            for j in range(self.v):
                if not selected[j] and keys[j] < min_key:
                    min_key = keys[j]
                    u = j

            if u == -1:
                break

            selected[u] = True

            for v in range(self.v):
                if self.g[u][v] != 0 and not selected[v] and self.g[u][v] < keys[v]:
                    keys[v] = self.g[u][v]
                    parent[v] = u

        for i in range(1, self.v):
            if parent[i] != -1:
                print(parent[i], "-", i, "weight:", self.g[i][parent[i]])
                total += self.g[i][parent[i]]

        print("Total weight of MST:", total)


ob = Graph()
ob.create()
ob.display()
ob.prims()
