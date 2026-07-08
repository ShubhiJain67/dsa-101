class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        for source, dest in edges:
            adj[source].append(dest)
        visited = [False]*V
        topo = []
        for node in range(V):
            if not visited[node]:
                self._topo_dfs(adj, node, visited, topo)
        topo.reverse()
        return topo
        
    def _topo_dfs(self, adj, node, visited, topo):
        visited[node] = True
        for child in adj[node]:
            if visited[child]:
                continue
            self._topo_dfs(adj, child, visited, topo)
        topo.append(node)
        
