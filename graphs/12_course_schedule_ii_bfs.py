class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        topo_sort = self.get_topo_bfs(numCourses, prerequisites)
        topo_sort.reverse()
        if len(topo_sort) != numCourses:
            return []
        return topo_sort

    def get_topo_bfs(self, numCourses: int, prerequisites: List[List[int]]):
        visited = [False] * numCourses
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for source, dest in prerequisites:
            indegree[dest] += 1
            adj[source].append(dest)
        topo_sort = []
        que = deque([node for node in range(numCourses) if indegree[node] == 0])
        while len(que) != 0:
            node = que.popleft()
            topo_sort.append(node)

            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    que.append(neighbour)
        return topo_sort
        
