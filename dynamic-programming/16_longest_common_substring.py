class Solution:
    def longCommSubstr(self, s1, s2):
        # ans = 0
        # for i in range(len(s1)):
        #     for j in range(len(s2)):
        #         ans = max(ans, self.lcsRec(s1, s2, i, j))

        # return ans
        
        # ans = 0
        # memory = [[None]*(len(s2)) for _ in range(len(s1))]
        # for i in range(len(s1)):
        #     for j in range(len(s2)):
        #         ans = max(ans, self.lcsRecMemo(s1, s2, i, j, memory))
                
        
        # ans = self.lcsDP(s1, s2)
        
        ans = self.lcsDPV2(s1, s2)

        return ans

    def lcsRec(self, s1, s2, i1, i2):
        if i1 == len(s1) or i2 == len(s2):
            return 0

        if s1[i1] == s2[i2]:
            return 1 + self.lcsRec(s1, s2, i1 + 1, i2 + 1)

        return 0
        
    def lcsRecMemo(self, s1, s2, i1, i2, memory):
        if i1 == len(s1) or i2 == len(s2):
            return 0
        if memory[i1][i2] != None:
            return memory[i1][i2]
        
        count = 0
        if s1[i1] == s2[i2]:
            count = 1 + self.lcsRecMemo(s1, s2, i1 + 1, i2 + 1, memory)
        memory[i1][i2] = count
        return count
        
    def lcsDP(self, s1, s2):
        ans = 0
        memory = [[None]*(len(s2)+1) for _ in range(len(s1)+1)]
        for i1 in range(len(s1), -1, -1):
            for i2 in range(len(s2), -1, -1):
                count = 0
                if i1 == len(s1) or i2 == len(s2):
                    count = 0
                elif s1[i1] == s2[i2]:
                    count = 1 + memory[i1+1][i2+1]
                memory[i1][i2] = count
                ans = max(ans, count)
        return ans
    
    def lcsDPV2(self, s1, s2):
        ans = 0
        prev = [None]*(len(s2)+1)
        for i1 in range(len(s1), -1, -1):
            curr = [None]*(len(s2)+1)
            for i2 in range(len(s2), -1, -1):
                count = 0
                if i1 == len(s1) or i2 == len(s2):
                    count = 0
                elif s1[i1] == s2[i2]:
                    count = 1 + prev[i2+1]
                curr[i2] = count
                ans = max(ans, count)
            prev = curr
        return ans
