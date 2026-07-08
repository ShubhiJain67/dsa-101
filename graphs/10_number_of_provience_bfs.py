from collections import deque

class Solution:
    def countConnected(self, V, edges):
        adj = [[] for i in range(V)]
        for source, dest in edges:
            adj[source].append(dest)
            adj[dest].append(source)

        visited = [False] * len(adj)
        count = 0

        for start in range(len(adj)):
            if visited[start]:
                continue
            count += 1
            que = deque([start])
            while que:
                node = que.popleft()

                if visited[node]:
                    continue
                visited[node] = True

                for neighbour in adj[node]:
                    if not visited[neighbour]:
                        que.append(neighbour)
        return count
        
