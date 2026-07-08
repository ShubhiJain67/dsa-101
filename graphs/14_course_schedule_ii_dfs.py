class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        for dest, source in prerequisites:
            adj[source].append(dest)

        visited = [False] * numCourses
        path = [False] * numCourses
        topo = []

        for node in range(numCourses):
            if not visited[node]:
                if not self._topo_dfs(adj, node, visited, topo, path):
                    return []

        topo.reverse()
        return topo

    def _topo_dfs(self, adj, node, visited, topo, path):
        visited[node] = True
        path[node] = True

        for child in adj[node]:
            if not visited[child]:
                if not self._topo_dfs(adj, child, visited, topo, path):
                    path[node] = False
                    return False
            elif path[child]:
                path[node] = False
                return False

        path[node] = False
        topo.append(node)
        return True
