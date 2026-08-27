class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()
        
        # return self.getMax(envelopes, 0, -1)

        # memo = [[None]*len(envelopes) for _ in envelopes]
        # return len(self.getMaxMemo(envelopes, 0, -1, memo))

        return self.getMaxDP(envelopes)
        
    def getMax(self, envelopes, index, prev):
        if index == len(envelopes):
            return 0
        currMax = self.getMax(envelopes, index + 1, prev)
        if prev == -1 or ((envelopes[index][0] > envelopes[prev][0] and  envelopes[index][1] > envelopes[prev][1])):
            currMax = max(currMax, 1 + self.getMax(envelopes, index + 1, index))
        return currMax

    def getMaxMemo(self, envelopes, index, prev, memo):
        if index == len(envelopes):
            return 0
        if memo[index][prev+1] is not None:
            return memo[index][prev+1]
        currMax = self.getMaxMemo(envelopes, index + 1, prev, memo)
        if prev == -1 or ((envelopes[index][0] > envelopes[prev][0] and  envelopes[index][1] > envelopes[prev][1])):
            currMax = max(currMax, 1 + self.getMaxMemo(envelopes, index + 1, index, memo))
        memo[index][prev+1] = currMax
        return memo[index][prev+1]

    def getMaxDP(self, envelopes):
        memo = [[0]*(len(envelopes)+1) for _ in range((len(envelopes)+1))]
        for index in range(len(envelopes)-1, -1, -1):
            for prev in range(index-1, -2, -1):
                currMax = memo[index + 1][prev + 1]
                if prev == -1 or ((envelopes[index][0] > envelopes[prev][0] and  envelopes[index][1] > envelopes[prev][1])):
                    currMax = max(currMax, 1 + memo[index + 1][index + 1])
                memo[index][prev + 1] = currMax
        return memo[0][0]
        
