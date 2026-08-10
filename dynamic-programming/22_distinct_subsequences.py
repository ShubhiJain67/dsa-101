class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # return self.getDist(s, t, 0, 0)

        # memo = [[None]*(len(t)+1) for _ in range(len(s)+1)]
        # return self.getDistMemo(s, t, 0, 0, memo)

        # return self.getDistDP(s, t)

        return self.getDistDPV2(s, t)
    
    def getDist(self, s, t, si, ti):
        if ti == len(t):
            return 1
        if si == len(s):
            return 0
        withoutCurr = self.getDist(s, t, si+1, ti)
        withCurr = 0
        if s[si] == t[ti]:
            withCurr = self.getDist(s, t, si+1, ti+1)
        return withoutCurr + withCurr

    def getDistMemo(self, s, t, si, ti, memo):
        if memo[si][ti] != None:
            return memo[si][ti]
        count = 0
        if ti == len(t):
            count = 1
        elif si == len(s):
            count = 0
        else:
            # without curr
            count = self.getDistMemo(s, t, si+1, ti, memo)
            if s[si] == t[ti]:
                # with curr
                count += self.getDistMemo(s, t, si+1, ti+1, memo)
        memo[si][ti] = count
        return memo[si][ti]

    def getDistDP(self, s, t):
        memo = [[None]*(len(t)+1) for _ in range(len(s)+1)]
        for si in range(len(s), -1, -1):
            for ti in range(len(t), -1, -1):
                count = 0
                if ti == len(t):
                    count = 1
                elif si == len(s):
                    count = 0
                else:
                    # without curr
                    count = memo[si+1][ti]
                    if s[si] == t[ti]:
                        # with curr
                        count += memo[si+1][ti+1]
                memo[si][ti] = count
        return memo[0][0]

    def getDistDPV2(self, s, t):
        prev = [None]*(len(t)+1)
        for si in range(len(s), -1, -1):
            curr = [None]*(len(t)+1)
            for ti in range(len(t), -1, -1):
                count = 0
                if ti == len(t):
                    count = 1
                elif si == len(s):
                    count = 0
                else:
                    # without curr
                    count = prev[ti]
                    if s[si] == t[ti]:
                        # with curr
                        count += prev[ti+1]
                curr[ti] = count
            prev = curr
        return curr[0]
