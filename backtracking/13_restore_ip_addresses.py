from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        return self.restore(s, 0, 4)

    def restore(self, s, index, pointsLeft):
        if index >= len(s) and pointsLeft == 0:
            return [""]
        if index >= len(s) or pointsLeft == 0:
            return []
        allAddresses = []
        for i in range(1,4):
            if index + i <= len(s):
                currSubStr = s[index: index+i]
                if s[index] == "0" and i > 1:
                    continue
                if int(currSubStr) > 255:
                    continue
                subStrs = self.restore(s, index+i, pointsLeft-1)
                for subStr in subStrs:
                    if subStr == "":
                        newSubStr = currSubStr
                    else:
                        newSubStr = f"{currSubStr}.{subStr}"
                    allAddresses.append(newSubStr)
        return allAddresses
