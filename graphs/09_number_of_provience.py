class Solution:
    def countConnected(self, V, edges):
        adj = [[] for i in range(V)]
        for source, dest in edges:
            adj[source].append(dest)
            adj[dest].append(source)
        
        visited = [False]*V
        component = 0
        
        for node in range(V):
            if not visited[node]:
                component += 1
                self.mark(adj, node, visited)
        return component
        
    
    def mark(self, adj, node, visited):
        if visited[node]:
            return
        visited[node] = True
        for neigh in adj[node]:
            self.mark(adj, neigh, visited)
        
