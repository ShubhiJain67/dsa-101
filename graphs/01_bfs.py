from collections import deque

class Solution:
    def bfs(self, adj):
        que = deque([0])
        visited = []
        traversal = []
        
        for i in range(len(adj)):
            visited.append(False)
        while len(que) != 0:
            node = que.popleft()
            if visited[node]:
                continue
            visited[node] = True
            traversal.append(node)
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    que.append(neighbour)
        # print(traversal)
        return traversal
