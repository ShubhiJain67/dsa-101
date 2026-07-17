class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        i1, i2, lcs = self.findLongestSubsequence(str1, str2)
        arr1 = [False]*len(str1)
        arr2 = [False]*len(str2)
        if i1 == None or i2 == None:
            return str1+str2
        p1 = i1
        p2 = 0
        while p1 < len(str1) and p2 < len(lcs):
            if str1[p1] == lcs[p2]:
                arr1[p1] = True
                p2+=1
            p1+=1

        p1 = i2
        p2 = 0
        while p1 < len(str2) and p2 < len(lcs):
            if str2[p1] == lcs[p2]:
                arr2[p1] = True
                p2+=1
            p1+=1

        p1 = 0
        p2 = 0
        finalStr = ""
        while p1 < len(str1) and p2 < len(str2):
            while p1 < len(str1) and arr1[p1] == False:
                finalStr = finalStr + str1[p1]
                p1+=1
            while p2 < len(str2) and arr2[p2] == False:
                finalStr = finalStr + str2[p2]
                p2+=1
            while p1 < len(str1) and p2 < len(str2) and arr1[p1] and arr2[p2]:
                finalStr = finalStr + str2[p2]
                p2+=1
                p1+=1
        while p1 < len(str1) and arr1[p1] == False:
            finalStr = finalStr + str1[p1]
            p1+=1
        while p2 < len(str2) and arr2[p2] == False:
            finalStr = finalStr + str2[p2]
            p2+=1
        # print(i1, i2, lcs, finalStr)
        return finalStr

    def findLongestSubsequence(self, str1, str2):
        s1Longer = True
        if len(str2) > len(str1):
            s1Longer = False
        prev = [(None, None, "")]*(len(str2)+1)
        for i1 in range(len(str1), -1, -1):
            curr = [(None, None, "")]*(len(str2)+1)
            for i2 in range(len(str2), -1, -1):
                longestSubsequence = ""
                startIndex1 = None
                startIndex2 = None
                if i1 == len(str1) or i2 == len(str2):
                    longestSubsequence = ""
                else:
                    if str1[i1] == str2[i2]:
                        wBI1, wBI2, withBoth = prev[i2+1]
                        withBoth = str1[i1]+withBoth
                        if len(longestSubsequence) <= len(withBoth):
                            longestSubsequence = withBoth
                            startIndex1 = i1
                            startIndex2 = i2
                    else:
                        ws1I1, ws1I2, withS1 = prev[i2]
                        if len(longestSubsequence) <= len(withS1):
                            longestSubsequence = withS1
                            startIndex1 = ws1I1
                            startIndex2 = ws1I2
                        ws2I1, ws2I2, withS2 = curr[i2+1]
                        if len(longestSubsequence) <= len(withS2):
                            longestSubsequence = withS2
                            startIndex1 = ws2I1
                            startIndex2 = ws2I2
                curr[i2] = [startIndex1, startIndex2, longestSubsequence]
            prev = curr
        return prev[0]
