class Solution:
    def isEulerCircuitExist(self, V, adj):
        degrees = self.getDegrees(adj)
        startNode, found = self.findStartNode(V, degrees)
        if not found:
            return 2
            
        visited = [False]*V
        self.dfs(adj, startNode, visited)
        # print(visited)
        for index in range(V):
            if degrees[index] > 0 and not visited[index]:
                return 0
        oddCount = 0
        for degree in degrees:
            if degree%2 == 1:
                oddCount += 1
        if oddCount == 0:
            return 2
        if oddCount == 2:
            return 1
        return 0
    
    def getDegrees(self, adj):
        return [len(neighbours) for neighbours in adj]
    
    def findStartNode(self, V, degrees):
        for index in range(V):
            if degrees[index] > 0:
                return index, True
        return 0, False
    
    def dfs(self, adj, node, visited):
        if visited[node]:
            return
        visited[node] = True
        for neigh in adj[node]:
            self.dfs(adj, neigh, visited)
        
