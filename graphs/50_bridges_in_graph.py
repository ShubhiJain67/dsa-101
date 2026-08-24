class Solution:
    def isBridge(self, V: int, edges: list[list[int]], c: int, d: int) -> bool:
        # code here
        adj = [[] for _ in range(V)]
        for src, dst in edges:
            if src == c and dst == d:
                continue
            adj[src].append(dst)
            adj[dst].append(src)
        
        # return self.naive(V, adj, c, d)
        return optimised(V, adj, c, d)
        
    def optimised(self, V, adj, c, d):
        visited = [False]*V
        self.mark(adj, c, visited)
        return not visited[d]
        
            
            
    def naive(self, V, adj, c, d):
        countAfter = self.componentCount(V, adj)
        adj[c].append(d)
        adj[d].append(c)
        countBefore = self.componentCount(V, adj)
        return countAfter != countBefore
        
        
    def componentCount(self, V, adj):
        components = 0
        visited = [False]*V
        for node in range(V):
            if not visited[node]:
                components += 1
                self.mark(adj, node, visited)
        return components
        
    def mark(self, adj, src, visited):
        if visited[src]:
            return
        visited[src] = True
        for neigh in adj[src]:
            if not visited[neigh]:
                self.mark(adj, neigh, visited)
        
