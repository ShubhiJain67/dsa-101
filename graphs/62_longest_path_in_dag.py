from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for src, dst in relations:
            adj[src-1].append(dst-1)
            indegree[dst-1] += 1

        finishTime = time[:]

        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        while q:
            curr = q.popleft()
            for neigh in adj[curr]:
                finishTime[neigh] = max(
                    finishTime[neigh],
                    finishTime[curr] + time[neigh]
                )
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)

        return max(finishTime)
