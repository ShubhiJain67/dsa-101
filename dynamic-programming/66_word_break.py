class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        wordLens = list(set(len(word) for word in words))
        wordLens.sort()
        
        # return self.find(s, words, wordLens, 0)

        # memo = [None]*(len(s)+1)
        # return self.findMemo(s, words, wordLens, 0, memo)

        return self.findDP(s, words, wordLens)
        
    def find(self, s, words, wordLens, i):
        if i == len(s):
            return True
        canMake = False
        for wordLen in wordLens:
            if i + wordLen > len(s):
                break
            if s[i:i+wordLen] in words:
                canMake = canMake or self.find(s, words, wordLens, i+wordLen)
                if canMake:
                    return True
        return False

    def findMemo(self, s, words, wordLens, i, memo):
        canMake = False
        if memo[i] is not None:
            return memo[i]
        if i == len(s):
            canMake = True
        else:
            for wordLen in wordLens:
                if i + wordLen > len(s):
                    break
                if s[i:i+wordLen] in words:
                    canMake = canMake or self.findMemo(s, words, wordLens, i+wordLen, memo)
                    if canMake:
                        break
        memo[i] = canMake
        return canMake

    def findDP(self, s, words, wordLens):
        memo = [None]*(len(s)+1)
        for i in range(len(s), -1, -1):
            canMake = False
            if i == len(s):
                canMake = True
            else:
                for wordLen in wordLens:
                    if i + wordLen > len(s):
                        break
                    if s[i:i+wordLen] in words:
                        canMake = canMake or memo[i+wordLen]
                        if canMake:
                            break
            memo[i] = canMake
        return memo[0]

