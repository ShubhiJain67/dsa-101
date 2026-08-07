class Solution:
    def isEulerCircuitExist(self, V, adj):
        degrees = [len(adj[i]) for i in range(V)]

        start = -1
        for i in range(V):
            if degrees[i] > 0:
                start = i
                break
        if start == -1:
            return 2
        visited = [False] * V
        self.dfs(start, visited, adj)

        for i in range(V):
            if degrees[i] > 0 and not visited[i]:
                return 0

        odd = 0
        for degree in degrees:
            if degree % 2 == 1:
                odd += 1

        if odd == 0:
            return 2
        elif odd == 2:
            return 1
        else:
            return 0
    
    def dfs(self, node, visited, adj):
        visited[node] = True
        for nei in adj[node]:
            if not visited[nei]:
                self.dfs(nei, visited, adj)
