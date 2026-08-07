from typing import List
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        connectComponents = self.getConnectedComponentsDFS(n, edges)
        count = 0
        # TIME CONSUMING
        # for i in range(len(connectComponents)):
        #     for j in range(i+1, len(connectComponents)):
        #         count += len(connectComponents[i])*len(connectComponents[j])
        remaining = n
        for component in connectComponents:
            size = len(component)
            remaining -= size
            count += size * remaining
        return count

    def getAdjList(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        return adj

    def getConnectedComponentsDFS(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = self.getAdjList(n, edges)
        visited = [False] * n
        components = []
        for i in range(n):
            if not visited[i]:
                group = []
                self.dfs(adj, i, visited, group)
                components.append(group)
        return components
    
    def dfs(self, adj, node, visited, group):
        visited[node] = True
        group.append(node)
        for neigh in adj[node]:
            if not visited[neigh]:
                self.dfs(adj, neigh, visited, group)
