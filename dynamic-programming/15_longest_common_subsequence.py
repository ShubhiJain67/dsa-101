class Solution:
    def lcs(self, s1, s2):
        # return self.lcsRec(s1, s2, 0, 0)
        
        # memory = [[None]*(len(s2)+1) for _ in range(len(s1)+1)]
        # return self.lcsRecMemo(s1, s2, 0, 0, memory)
        
        # return self.lcsDP(s1, s2)
        
        return self.lcsDPV2(s1, s2)
    
    def lcsRec(self, s1, s2, i1, i2):
        longestLength = 0
        if i1 == len(s1):
            longestLength = 0
        elif i2 == len(s2):
            longestLength = 0
        elif s1[i1] == s2[i2]:
            includeCurrent = 1+self.lcsRec(s1, s2, i1+1, i2+1)
            longestLength = max(longestLength, includeCurrent)
        else:
            s1Ahead = self.lcsRec(s1, s2, i1+1, i2)
            longestLength = max(longestLength, s1Ahead)
            s2Ahead = self.lcsRec(s1, s2, i1, i2+1)
            longestLength = max(longestLength, s2Ahead)
        return longestLength
        
    def lcsRecMemo(self, s1, s2, i1, i2, memory):
        longestLength = 0
        if memory[i1][i2] is not None:
            return memory[i1][i2]
        elif i1 == len(s1):
            longestLength = 0
        elif i2 == len(s2):
            longestLength = 0
        elif s1[i1] == s2[i2]:
            includeCurrent = 1+self.lcsRecMemo(s1, s2, i1+1, i2+1, memory)
            longestLength = max(longestLength, includeCurrent)
        else:
            s1Ahead = self.lcsRecMemo(s1, s2, i1+1, i2, memory)
            longestLength = max(longestLength, s1Ahead)
            s2Ahead = self.lcsRecMemo(s1, s2, i1, i2+1, memory)
            longestLength = max(longestLength, s2Ahead)
        memory[i1][i2] = longestLength
        return memory[i1][i2]
        
    def lcsDP(self, s1, s2):
        memory = [[None]*(len(s2)+1) for _ in range(len(s1)+1)]
        for i1 in range(len(s1), -1, -1):
            for i2 in range(len(s2), -1, -1):
                longestLength = 0
                if i1 == len(s1):
                    longestLength = 0
                elif i2 == len(s2):
                    longestLength = 0
                elif s1[i1] == s2[i2]:
                    includeCurrent = 1+memory[i1+1][i2+1]
                    longestLength = max(longestLength, includeCurrent)
                else:
                    s1Ahead = memory[i1+1][i2]
                    longestLength = max(longestLength, s1Ahead)
                    s2Ahead = memory[i1][i2+1]
                    longestLength = max(longestLength, s2Ahead)
                memory[i1][i2] = longestLength
        return memory[0][0]
    
    def lcsDPV2(self, s1, s2):
        prev = [None]*(len(s2)+1)
        for i1 in range(len(s1), -1, -1):
            curr = [None]*(len(s2)+1)
            for i2 in range(len(s2), -1, -1):
                longestLength = 0
                if i1 == len(s1):
                    longestLength = 0
                elif i2 == len(s2):
                    longestLength = 0
                elif s1[i1] == s2[i2]:
                    includeCurrent = 1+prev[i2+1]
                    longestLength = max(longestLength, includeCurrent)
                else:
                    s1Ahead = prev[i2]
                    longestLength = max(longestLength, s1Ahead)
                    s2Ahead = curr[i2+1]
                    longestLength = max(longestLength, s2Ahead)
                curr[i2] = longestLength
            prev = curr
        return prev[0]
