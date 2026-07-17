def findLCS(n: int, m: int, s1: str, s2: str) -> str:
    # return lcsRec(s1, s2, 0, 0)
    
    # memory = [[None]*(len(s2)+1) for _ in range(len(s1)+1)]
    # return lcsRecMemo(s1, s2, 0, 0, memory)
    
    # return lcsDP(s1, s2)
    
    return lcsDPV2(s1, s2)

def lcsRec(s1, s2, i1, i2):
    longestLength = ""
    if i1 == len(s1):
        longestLength = ""
    elif i2 == len(s2):
        longestLength = ""
    elif s1[i1] == s2[i2]:
        includeCurrent = s1[i1]+lcsRec(s1, s2, i1+1, i2+1)
        if len(includeCurrent) > len(longestLength):
            longestLength = includeCurrent
    else:
        s1Ahead = lcsRec(s1, s2, i1+1, i2)
        if len(s1Ahead) > len(longestLength):
            longestLength = s1Ahead
        s2Ahead = lcsRec(s1, s2, i1, i2+1)
        if len(s2Ahead) > len(longestLength):
            longestLength = s2Ahead
    return longestLength
    
def lcsRecMemo(s1, s2, i1, i2, memory):
    longestLength = ""
    if memory[i1][i2] is not None:
        return memory[i1][i2]
    elif i1 == len(s1):
        longestLength = ""
    elif i2 == len(s2):
        longestLength = ""
    elif s1[i1] == s2[i2]:
        includeCurrent = s1[i1]+lcsRecMemo(s1, s2, i1+1, i2+1, memory)
        if len(includeCurrent) > len(longestLength):
            longestLength = includeCurrent
    else:
        s1Ahead = lcsRecMemo(s1, s2, i1+1, i2, memory)
        if len(s1Ahead) > len(longestLength):
            longestLength = s1Ahead
        s2Ahead = lcsRecMemo(s1, s2, i1, i2+1, memory)
        if len(s2Ahead) > len(longestLength):
            longestLength = s2Ahead
    memory[i1][i2] = longestLength
    return memory[i1][i2]
    
def lcsDP(s1, s2):
    memory = [[None]*(len(s2)+1) for _ in range(len(s1)+1)]
    for i1 in range(len(s1), -1, -1):
        for i2 in range(len(s2), -1, -1):
            longestLength = ""
            if i1 == len(s1):
                longestLength = ""
            elif i2 == len(s2):
                longestLength = ""
            elif s1[i1] == s2[i2]:
                includeCurrent = s1[i1]+memory[i1+1][i2+1]
                if len(includeCurrent) > len(longestLength):
                    longestLength = includeCurrent
            else:
                s1Ahead = memory[i1+1][i2]
                if len(s1Ahead) > len(longestLength):
                    longestLength = s1Ahead
                s2Ahead = memory[i1][i2+1]
                if len(s2Ahead) > len(longestLength):
                    longestLength = s2Ahead
            memory[i1][i2] = longestLength
    return memory[0][0]

def lcsDPV2(s1, s2):
    prev = [None]*(len(s2)+1)
    for i1 in range(len(s1), -1, -1):
        curr = [None]*(len(s2)+1)
        for i2 in range(len(s2), -1, -1):
            longestLength = ""
            if i1 == len(s1):
                longestLength = ""
            elif i2 == len(s2):
                longestLength = ""
            elif s1[i1] == s2[i2]:
                includeCurrent = s1[i1]+prev[i2+1]
                if len(includeCurrent) > len(longestLength):
                    longestLength = includeCurrent
            else:
                s1Ahead = prev[i2]
                if len(s1Ahead) > len(longestLength):
                    longestLength = s1Ahead
                s2Ahead = curr[i2+1]
                if len(s2Ahead) > len(longestLength):
                    longestLength = s2Ahead
            curr[i2] = longestLength
        prev = curr
    return prev[0]
