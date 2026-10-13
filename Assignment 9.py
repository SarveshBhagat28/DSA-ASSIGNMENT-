class Graph:
    def create(self):
        self.v=0
        self.e=0
        self.g=[]
    def create(self):
        self.v=int(input("Enter number of vertices: "))
        self.e=int(input("Enter number of edges: "))
        self.g=[[0 for i in range(self.v)] for j in range(self.v)]
        for i in range(self.e):
            print("Enter edge",i+1,"(u,v,w): ")
            u,v,w=map(int,input().split())
            self.g[u][v]=self.g[v][u]=w
    def display(self):
         for i in range(self.v):
            for j in range(self.v):
                print(self.g[i][j],end=" ")
            print()

ob=Graph()
ob.create()
ob.display()    
