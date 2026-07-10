class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        directions = [
                [-1, 0],
            [0, -1],    [0, +1],
                [+1, 0]
        ]

        que = deque()

        for r in range(m):
            for c in range(n):
                if isWater[r][c] == 1:
                    que.append([r, c])
                    isWater[r][c] = -1
        levelNodeCount = len(que)
        levelCount = 0
        levelAffected = False
        while que:
            r, c = que.popleft()
            levelNodeCount -= 1
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n and isWater[nr][nc] == 0:
                    isWater[nr][nc] = levelCount + 1
                    que.append([nr, nc])
                    levelAffected = True
            if levelNodeCount == 0 and levelAffected:
                levelAffected = False
                levelNodeCount = len(que)
                levelCount += 1
        for r in range(m):
            for c in range(n):
                if isWater[r][c] == -1:
                    isWater[r][c] = 0
        return isWater
