class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        globalWordMap = {}
        for word in words:
            if word not in globalWordMap:
                globalWordMap[word] = 0
            globalWordMap[word] += 1
        
        indexes = []
        wordLen = len(words[0])
        
        for offset in range(wordLen):
            p0 = offset
            p1 = offset
            wordMap = {}
            wordCount = 0
            while p1 < len(s):
                curr = s[p1:p1+wordLen]
                if curr in globalWordMap and (curr not in wordMap or wordMap[curr] < globalWordMap[curr]):
                    p1 += wordLen
                    if curr not in wordMap:
                        wordMap[curr] = 0
                    wordMap[curr] += 1
                    wordCount += 1
                elif curr in globalWordMap:
                    first = s[p0:p0+wordLen]
                    while first != curr:
                        wordMap[first] -= 1
                        wordCount -= 1
                        p0 += wordLen
                        first = s[p0:p0+wordLen]
                    p1 += wordLen
                    p0 += wordLen
                else:
                    p0 = p1+wordLen
                    p1 = p0
                    wordMap = {}
                    wordCount = 0

                if len(words) == wordCount:
                    indexes.append(p0)
                # print(curr)
        
        return indexes
