from collections import deque

class Solution:
    def isCycle(self, V, edges):
        adj_list = self._get_adj_list(V, edges)
        visited = []
        for i in range(V):
            visited.append(False)
        for node in range(V):
          if not visited[node] and self._has_cycle_bfs(adj_list, node, visited):
                return True
        return False
        
    def _get_adj_list(self, V, edges):
        adj_list = []
        for i in range(V):
            adj_list.append([])
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list
            
    def _has_cycle_bfs(self, adj_list, node, visited):
        que = deque([(node, -1)])

        while len(que) != 0:
            node, parent = que.popleft()
            if visited[node]:
                return True
            visited[node] = True
            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue
                que.append((neighbour, node))
        return False
        
        
           
