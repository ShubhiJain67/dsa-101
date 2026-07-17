class Solution:
	def minOperations(self, s1, s2):
		lcsLen = self.getLongestCommonSubsequence(s1, s2)
		return len(s1) - lcsLen + (len(s2) - lcsLen)
	
	def getLongestCommonSubsequence(self, s1, s2):
	    prev = [None]*(len(s2)+1)
	    for i1 in range(len(s1), -1, -1):
	        curr = [None]*(len(s2)+1)
	        for i2 in range(len(s2), -1, -1):
	            lcsLen = 0
	            if i1 == len(s1) or i2 == len(s2):
	                lcsLen = 0
	            else:
	                if s1[i1] == s2[i2]:
	                    withBoth = 1+prev[i2+1]
	                    lcsLen = lcsLen if withBoth < lcsLen else withBoth
	                else:
	                    s1Ahead = prev[i2]
	                    lcsLen = lcsLen if s1Ahead < lcsLen else s1Ahead
	                    s2Ahead = curr[i2+1]
	                    lcsLen = lcsLen if s2Ahead < lcsLen else s2Ahead
	            curr[i2] = lcsLen
	        prev = curr
	    return prev[0]
	                    
