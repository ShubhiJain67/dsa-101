class Solution:
    def isBipartite(self, V, edges):
        adj = [[] for i in range(V)]
        
        for source, dest in edges:
            adj[source].append(dest)
            adj[dest].append(source)
        colors = [None]*V
        for node in range(V):
            if colors[node] == None and (not self.isBipartiteDFS(adj, node, True, colors)):
                return False
        return True
                    
        
    def isBipartiteDFS(self, adj, node, currColor, colors):
        if colors[node] != None:
            return colors[node] == currColor
        colors[node] = currColor
        for neighbour in adj[node]:
            if (not self.isBipartiteDFS(adj, neighbour, not currColor, colors)):
                return False
        return True
                
