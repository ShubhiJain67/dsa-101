from collections import deque
class Solution:
    def isCyclic(self, V, edges):
        adj = [[] for _ in range(V)]
        indegree = [0] * V
    
        for source, dest in edges:
            adj[source].append(dest)
            indegree[dest] += 1
    
        queue = deque(i for i in range(V) if indegree[i] == 0)
        topo = []
    
        while queue:
            node = queue.popleft()
            topo.append(node)
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
    
        return len(topo) != V
