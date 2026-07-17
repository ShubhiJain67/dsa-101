class Solution:
	def LongestRepeatingSubsequence(self, s):
	    s1 = s
	    s2 = s
		prev = [None]*(len(s2)+1)
        for i1 in range(len(s1), -1, -1):
            curr = [None]*(len(s2)+1)
            for i2 in range(len(s2), -1, -1):
                longestLength = 0
                if i1 == len(s1):
                    longestLength = 0
                elif i2 == len(s2):
                    longestLength = 0
                elif s1[i1] == s2[i2] and i1 != i2:
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
		        
		    
