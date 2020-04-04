from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFS(self,v,vertex):
        visited = [False]*vertex
        print(self. graph)
        # print(len(self.graph),"+++")
        self.DFSUtil(v,visited,0)

    def DFSUtil(self,v,visited,count):
        visited[v]=True
        print("count is",count,"vertices",v)
        for i in self.graph[v]:
            if visited[i] == False:
                # print(visited)
                self.DFSUtil(i,visited,count+1)
            
g= Graph()

vertex=9

g.addEdge(2, 1) 
g.addEdge(3, 1) 
g.addEdge(4, 1) 
g.addEdge(5, 1) 
g.addEdge(6, 4) 
g.addEdge(7, 4) 
g.addEdge(8, 2)

g.DFS(1,vertex) 
