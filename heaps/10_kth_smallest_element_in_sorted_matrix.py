class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        i = 0
        j = 0
        heap = [[matrix[0][0], [0,0]]]
        num = 0
        visited = {(0, 0)}
        while k > 0:
            curr = heapq.heappop(heap)
            num = curr[0]
            i, j = curr[1]
            if i+1 < len(matrix) and (i + 1, j) not in visited:
                visited.add((i + 1, j))
                heapq.heappush(heap, [matrix[i+1][j], [i+1,j]])
            if j+1 < len(matrix[0]) and (i, j+1) not in visited:
                visited.add((i, j+1))
                heapq.heappush(heap, [matrix[i][j+1], [i,j+1]])
            k -= 1
        return num
