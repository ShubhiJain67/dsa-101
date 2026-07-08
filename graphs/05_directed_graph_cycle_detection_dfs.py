class Solution:
    def isCyclic(self, V, edges):
        adj_list = self._get_adj_list(V, edges)
        visited = [False] * V
        path_visited = [False] * V
        for node in range(V):
            if not visited[node] and self._has_cycle_dfs(adj_list, node, visited, path_visited):
                return True
        return False

    def _get_adj_list(self, V, edges):
        adj_list = [[] for _ in range(V)]
        for u, v in edges:
            adj_list[u].append(v)

        return adj_list

    def _has_cycle_dfs(self, adj_list, node, visited, path_visited):
        visited[node] = True
        path_visited[node] = True

        for neighbour in adj_list[node]:
            if not visited[neighbour] and self._has_cycle_dfs(adj_list, neighbour, visited, path_visited):
                return True
            if path_visited[neighbour]:
                return True

        path_visited[node] = False
        return False
