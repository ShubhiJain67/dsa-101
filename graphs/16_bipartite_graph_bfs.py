from collections import deque

class Solution:
    def isBipartite(self, V, edges):
        adj = [[] for i in range(V)]
        
        for source, dest in edges:
            adj[source].append(dest)
            adj[dest].append(source)
        colors = [None]*V
        for node in range(V):
            if colors[node] == None and (not self.isBipartiteBFS(adj, node, colors)):
                return False
        return True
        
    def isBipartiteBFS(self, adj, node, colors):
        que = deque([(node, True)])
        while len(que) != 0:
            node, currColor = que.popleft()
            colors[node] = currColor
            for neighbour in adj[node]:
                if colors[neighbour] != None:
                    if colors[neighbour] == currColor:
                        return False
                    else:
                        continue
                else:
                    que.append((neighbour, not currColor))
        
        return True
            
            
        
                
