class Solution:
    def climbStairs(self, n: int) -> int:
        # return self.climbRec(n)
        # return self.climbDP(n)
        return self.climbDPOptimised(n)
        
    def climbRec(self, n):
        if n == 0:
            return 1
        if n < 0:
            return 0
        via1 = self.climbRec(n-1)
        via2 = self.climbRec(n-2)
        return via1 + via2
    
    def climbDP(self, n):
        dp = [0]*(n+1)
        for i in range(n+1):
            if i == 0:
                count = 1
            else:
                count = dp[i-1]
                if i > 1:
                    count += dp[i-2]
            dp[i] = count
        return dp[n]
    
    def climbDPOptimised(self, n):
        p1 = 0
        p2 = 0
        for i in range(n+1):
            if i == 0:
                count = 1
            else:
                count = p2
                if i > 1:
                    count += p1
            p1 = p2
            p2 = count
        return p2
