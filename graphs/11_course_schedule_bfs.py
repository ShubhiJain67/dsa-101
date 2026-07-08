from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        topo_sort = self.get_topo_bfs(numCourses, prerequisites)
        return len(topo_sort) == numCourses

    def get_topo_bfs(self, numCourses: int, prerequisites: List[List[int]]):
        visited = [False] * numCourses
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for source, dest in prerequisites:
            indegree[dest] += 1
            adj[source].append(dest)
        topo_sort = []
        # print(indegree)
        que = deque([node for node in range(numCourses) if indegree[node] == 0])
        while len(que) != 0:
            # print(que)
            node = que.popleft()
            topo_sort.append(node)

            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    que.append(neighbour)
        return topo_sort
