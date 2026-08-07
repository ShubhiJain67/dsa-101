class Solution:
    directions = [[1,0],[0,1]]
    def uniquePaths(self, m: int, n: int) -> int:
        # return self.move(0, 0, m-1, n-1)

        # memo = [[None]*n for _ in range(m)]
        # return self.moveMemo(0, 0, m-1, n-1, memo)

        return self.moveDP(m, n)
    
    def move(self, i, j, ti, tj):
        if i == ti and j == tj:
            return 1
        if i > ti or j > tj:
            return 0
        paths = 0
        for dirc in self.directions:
            paths += self.move(i+dirc[0], j+dirc[1], ti, tj)
        return paths
    
    def moveMemo(self, i, j, ti, tj, memo):
        if i == ti and j == tj:
            return 1
        if i > ti or j > tj:
            return 0
        if memo[i][j] is not None:
            return memo[i][j]
        paths = 0
        for dirc in self.directions:
            paths += self.moveMemo(i+dirc[0], j+dirc[1], ti, tj, memo)
        memo[i][j] = paths
        return memo[i][j]

    def moveDP(self, m, n):
        memo = [[None]*n for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                paths = 0
                if i == m-1 and j == n-1:
                    paths = 1
                else:
                    for dirc in self.directions:
                        if 0 <= i+dirc[0] < m and 0 <= j+dirc[1] < n:
                            paths += memo[i+dirc[0]][j+dirc[1]]
                memo[i][j] = paths
        return memo[0][0]
