class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        for source, dest in prerequisites:
            adj[source].append(dest)
        return not self.detect_cycle_dfs(adj)
    
    def detect_cycle_dfs(self, adj: List[List[int]]):
        visited = [False] * len(adj)
        path = [False] * len(adj)
        for node in range(len(adj)):
            if not visited[node] and self.detect_cycle(adj, node, visited, path):
                return True
        return False
    
    def detect_cycle(self, adj: List[List[int]], node: int, visited: List[bool], path: List[bool]):
        visited[node] = True
        path[node] = True
        for neighbour in adj[node]:
            if visited[neighbour] and path[neighbour]:
                return True
            if not visited[neighbour] and self.detect_cycle(adj, neighbour, visited, path):
                return True
        path[node] = False
        return False
        



