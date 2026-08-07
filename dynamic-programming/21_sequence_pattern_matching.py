class Solution:
    def hasMatch(self, s1:str, s2: str) -> bool:
        # for i in range(len(s1)):
        #     if self.lcsRec(s1, s2, i, 0):
        #         return True
        
        # for i in range(len(s1)):
        #     memory = [[None]*(len(s2)+1) for _ in range(len(s1)+1)]
        #     if self.lcsRecMemo(s1, s2, i, 0, memory):
        #         return True
                
        
        # for i in range(len(s1)):
        #     if self.lcsDP(s1, s2, i):
        #         return True
        
        for i in range(len(s1)):
            if self.lcsDPV2(s1, s2, i):
                return True

        return False

    def lcsRec(self, s1, s2, i1, i2):
        if i2 == len(s2):
            return True
        if i1 == len(s1):
            while i2 < len(s2) and s2[i2] == "*":
                i2 += 1
            return i2 == len(s2)
        if s1[i1] == s2[i2]:
            return self.lcsRec(s1, s2, i1 + 1, i2 + 1)
        elif s2[i2] == '*':
            return self.lcsRec(s1, s2, i1+1, i2) or self.lcsRec(s1, s2, i1+1, i2+1) or self.lcsRec(s1, s2, i1, i2+1)
        return False
        
    def lcsRecMemo(self, s1, s2, i1, i2, memory):
        isMatch = False
        if i2 == len(s2):
            isMatch = True
        elif i1 == len(s1):
            while i2 < len(s2) and s2[i2] == "*":
                i2 += 1
            isMatch = i2 == len(s2)
        elif memory[i1][i2] is not None:
            isMatch = memory[i1][i2]
        elif s1[i1] == s2[i2]:
            isMatch = self.lcsRecMemo(s1, s2, i1 + 1, i2 + 1, memory)
        elif s2[i2] == '*':
            isMatch = self.lcsRecMemo(s1, s2, i1+1, i2, memory) or self.lcsRecMemo(s1, s2, i1+1, i2+1, memory) or self.lcsRecMemo(s1, s2, i1, i2+1, memory)
        memory[i1][i2] = isMatch
        return memory[i1][i2]
        
    def lcsDP(self, s1, s2, i):
        memory = [[None]*(len(s2)+1) for _ in range(len(s1)+1)]
        for i1 in range(len(s1), i-1, -1):
            for i2 in range(len(s2), -1, -1):
                isMatch = False
                if i2 == len(s2):
                    isMatch = True
                elif i1 == len(s1):
                    t = i2
                    while t < len(s2) and s2[t] == "*":
                        t += 1
                    isMatch = t == len(s2)
                elif s1[i1] == s2[i2]:
                    isMatch = memory[i1 + 1][i2 + 1]
                elif s2[i2] == '*':
                    isMatch = memory[i1 + 1][i2] or memory[i1 + 1][i2 + 1] or memory[i1][i2 + 1]
                memory[i1][i2] = isMatch
        return memory[i][0]
    
    def lcsDPV2(self, s1, s2, i):
        prev = [None]*(len(s2)+1)
        for i1 in range(len(s1), i-1, -1):
            curr = [None]*(len(s2)+1)
            for i2 in range(len(s2), -1, -1):
                isMatch = False
                if i2 == len(s2):
                    isMatch = True
                elif i1 == len(s1):
                    t = i2
                    while t < len(s2) and s2[t] == "*":
                        t += 1
                    isMatch = t == len(s2)
                elif s1[i1] == s2[i2]:
                    isMatch = prev[i2 + 1]
                elif s2[i2] == '*':
                    isMatch = prev[i2] or prev[i2 + 1] or curr[i2 + 1]
                curr[i2] = isMatch
            prev = curr
        return curr[0]
