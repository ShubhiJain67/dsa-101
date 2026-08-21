class Solution:
    def countWays(self, s):
        # trueCount, _ = self.count(s, 0, len(s)-1)
        
        # memo = [[None]*len(s) for _ in range(len(s))]
        # trueCount, _ = self.countMemo(s, 0, len(s)-1, memo)
        
        trueCount, _ = self.countDP(s)
        return trueCount
    
    def count(self, s, i, j):
        trueCount = 0
        falseCount = 0
        if i == j:
            if s[i] == 'T':
                trueCount = 1
            else:
                falseCount = 1
        else:
            for part in range(i+1, j, 2):
                prevTrueCount, prevFalseCount = self.count(s, i, part - 1)
                op = s[part]
                nextTrueCount, nextFalseCount = self.count(s, part+1, j)
                
                match op:
                    case '&':
                        trueCount += prevTrueCount*nextTrueCount
                        falseCount += prevTrueCount*nextFalseCount + prevFalseCount*nextTrueCount + prevFalseCount*nextFalseCount
                    case '|':
                        trueCount += prevTrueCount*nextTrueCount + prevTrueCount*nextFalseCount + prevFalseCount*nextTrueCount
                        falseCount += prevFalseCount*nextFalseCount
                    case '^':
                        trueCount += prevTrueCount*nextFalseCount + prevFalseCount*nextTrueCount
                        falseCount += prevFalseCount*nextFalseCount + prevTrueCount*nextTrueCount
        
        return trueCount, falseCount
        
    def countMemo(self, s, i, j, memo):
        if memo[i][j] is not None:
            return memo[i][j]
        trueCount = 0
        falseCount = 0
        if i == j:
            if s[i] == 'T':
                trueCount = 1
            else:
                falseCount = 1
        else:
            for part in range(i+1, j, 2):
                prevTrueCount, prevFalseCount = self.countMemo(s, i, part - 1, memo)
                op = s[part]
                nextTrueCount, nextFalseCount = self.countMemo(s, part+1, j, memo)
                
                match op:
                    case '&':
                        trueCount += prevTrueCount*nextTrueCount
                        falseCount += prevTrueCount*nextFalseCount + prevFalseCount*nextTrueCount + prevFalseCount*nextFalseCount
                    case '|':
                        trueCount += prevTrueCount*nextTrueCount + prevTrueCount*nextFalseCount + prevFalseCount*nextTrueCount
                        falseCount += prevFalseCount*nextFalseCount
                    case '^':
                        trueCount += prevTrueCount*nextFalseCount + prevFalseCount*nextTrueCount
                        falseCount += prevFalseCount*nextFalseCount + prevTrueCount*nextTrueCount
        memo[i][j] = [trueCount, falseCount]
        return memo[i][j]
        
    def countDP(self, s):
        memo = [[None]*len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                trueCount = 0
                falseCount = 0
                if i == j:
                    if s[i] == 'T':
                        trueCount = 1
                    else:
                        falseCount = 1
                else:
                    for part in range(i+1, j, 2):
                        prevTrueCount, prevFalseCount = memo[i][part - 1]
                        op = s[part]
                        nextTrueCount, nextFalseCount = memo[part + 1][j]
                        
                        match op:
                            case '&':
                                trueCount += prevTrueCount*nextTrueCount
                                falseCount += prevTrueCount*nextFalseCount + prevFalseCount*nextTrueCount + prevFalseCount*nextFalseCount
                            case '|':
                                trueCount += prevTrueCount*nextTrueCount + prevTrueCount*nextFalseCount + prevFalseCount*nextTrueCount
                                falseCount += prevFalseCount*nextFalseCount
                            case '^':
                                trueCount += prevTrueCount*nextFalseCount + prevFalseCount*nextTrueCount
                                falseCount += prevFalseCount*nextFalseCount + prevTrueCount*nextTrueCount
                memo[i][j] = [trueCount, falseCount]
        return memo[0][len(s)-1]
          
