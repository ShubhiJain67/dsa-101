class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == "0" or "00" in s:
            return 0

        # combinations = self.decodeRec(s, 0)

        # memo = [None]*len(s)
        # combinations = self.decodeRecMemo(s, 0, memo)

        # combinations = self.decodeRecDP(s)

        combinations = self.decodeRecDPOptimised(s)

        return combinations
    
    def decodeRec(self, s, index):
        if index == len(s):
            return 1
        combinations = 0
        if s[index] != "0":
            withSingle = self.decodeRec(s, index+1)
            combinations += withSingle
        if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
            withDouble = self.decodeRec(s, index+2)
            combinations += withDouble
        return combinations
    
    def decodeRecMemo(self, s, index, memo):
        if index == len(s):
            return 1
        if memo[index] is not None:
            return memo[index]
        combinations = 0
        if s[index] != "0":
            withSingle = self.decodeRecMemo(s, index+1, memo)
            combinations += withSingle
        if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
            withDouble = self.decodeRecMemo(s, index+2, memo)
            combinations += withDouble
        memo[index] = combinations
        return combinations
    

    def decodeRecDP(self, s):
        dp = [0]*(len(s)+1)
        for index in range(len(s), -1, -1):
            combinations = 0
            if index == len(s):
                combinations = 1
            else:
                if s[index] != "0":
                    withSingle = dp[index+1]
                    combinations += withSingle
                if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
                    withDouble = dp[index+2]
                    combinations += withDouble
            dp[index] = combinations
        return dp[0]
    

    def decodeRecDPOptimised(self, s):
        p1 = 0
        p2 = 0
        for index in range(len(s), -1, -1):
            combinations = 0
            if index == len(s):
                combinations = 1
            else:
                if s[index] != "0":
                    withSingle = p2
                    combinations += withSingle
                if index + 1 < len(s) and 10 <= int(s[index:index+2]) <= 26:
                    withDouble = p1
                    combinations += withDouble
            p1 = p2
            p2 = combinations
        return p2
