class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        store1 = [0]*26
        store2 = [0]*26
        for s in s1:
            store1[ord(s)-ord('a')] += 1
        
        i = 0
        while i < len(s1):
            store2[ord(s2[i])-ord('a')] += 1
            i += 1
        
        if self.isMatch(store1, store2):
            return True

        while i < len(s2):
            indexToRemove = ord(s2[i-len(s1)]) - ord('a')
            indexToAdd = ord(s2[i]) - ord('a')
            # print(f"Removing {i-len(s1)} Adding {indexToAdd}")
            store2[indexToRemove] -= 1
            store2[indexToAdd] += 1
            if self.isMatch(store1, store2):
                return True
            i += 1
        return False
    
    def isMatch(self, s1, s2):
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True
