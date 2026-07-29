class Solution:
    def prefixSum2D(self, mat, queries):
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if c > 0:
                    mat[r][c] += mat[r][c-1]
                if r > 0:
                    mat[r][c] += mat[r-1][c]
                if c > 0 and r > 0:
                    mat[r][c] -= mat[r-1][c-1]
        allResults = []
        for query in queries:
            x1, y1, x2, y2 = query
            result = mat[x2][y2]
            if x1 > 0:
                result -= mat[x1-1][y2]
            if y1 > 0:
                result -= mat[x2][y1-1]
            if y1 > 0 and x1 > 0:
                result += mat[x1-1][y1-1]
            allResults.append(result)
        return allResults 
                
        

                      
