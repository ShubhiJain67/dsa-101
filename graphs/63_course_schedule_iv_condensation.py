class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = []
        adj = [[] for _ in range(numCourses)]
        for src, dst in prerequisites:
            adj[dst].append(src)

        memo = [None]*numCourses
        for course in range(numCourses):
            self.getAll(adj, course, memo)
        for potPre, dst in queries:
            ans.append(potPre in memo[dst])
        return ans
    
    def getAll(self, adj, course, memo):
        if memo[course] is not None:
            return memo[course]
        prereq = set()
        for depCourse in adj[course]:
            prereq.add(depCourse)
            prereq.update(self.getAll(adj, depCourse, memo))
        memo[course] = prereq
        return memo[course]
